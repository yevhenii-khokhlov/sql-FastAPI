import json

from fastapi import FastAPI, Request

from services import is_token_valid
from sql_runner.manager import run_sql

app = FastAPI()


@app.get("/")
async def root_endpoint():
    """
    :return:

        "success": bool
    """
    return {"success": True}


@app.post("/run-sql")
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
