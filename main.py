import json
import bmemcached

from fastapi import FastAPI, Request

from config import get_settings
from services import is_token_valid
from sql_runner.manager import run_sql

settings = get_settings()

mc = bmemcached.Client(
    settings.memcachier_servers,
    username=settings.db_username,
    password=settings.memcachier_password
)
mc.enable_retry_delay(True)

app = FastAPI()


@app.get("/")
def root_endpoint():
    mc.set("foo", "bar")
    print(mc.get("foo"))
    print(settings.memcachier_servers)


# @app.get("/")
# async def root_endpoint():
#     """
#     :return:
#
#         "success": bool
#     """
#     return {"success": True}


@app.get("/run-sql")
async def run_sql_endpoint(request: Request):
    """
    Supports queries that return data as a two-dimensional table.
    Does not support multiply query like:
    'select * from users; select * from posts;'

    :param request:

        "selector": str

    :return:

        "success": bool,
        "query_result": [[]] or "error": str
    """
    raw_body = await request.body()

    try:
        if not is_token_valid(request.headers):
            return {"success": False, "error": "invalid api_token"}

        body = json.loads(raw_body)
        selector = body.get('selector')

        result = run_sql(selector)

        return {"success": True, "query_result": result}

    except Exception as err:
        return {"success": False, "error": err.__str__()}
