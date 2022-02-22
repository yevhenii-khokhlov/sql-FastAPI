import json

from fastapi import FastAPI, Request, BackgroundTasks

from config import get_settings
from services import is_token_valid, generate_response_id, get_response_by_id
from sql_runner.manager import run_sql

settings = get_settings()

app = FastAPI()


@app.get("/")
async def root_endpoint():
    """
    :return:

        "success": bool
    """
    return {"success": True}


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


@app.get("/run-sql-background")
async def run_sql_endpoint_background(request: Request, background_tasks: BackgroundTasks):
    """
    Supports queries that return data as a two-dimensional table.
    Does not support multiply query like:
    'select * from users; select * from posts;'

    param background_tasks:

        BackgroundTasks

    param request:

        "selector": str

    :return:

        "success": bool,
        "response_id": str
    """
    raw_body = await request.body()

    try:
        if not is_token_valid(request.headers):
            return {"success": False, "error": "invalid api_token"}

        body = json.loads(raw_body)
        selector = body.get('selector')
        response_id = generate_response_id()

        background_tasks.add_task(run_sql, selector, background=True, response_id=response_id)

        return {"success": True, "response_id": response_id}

    except Exception as err:
        return {"success": False, "error": err.__str__()}


@app.get("/sql-background-response/{response_id}")
async def sql_background_response_endpoint(response_id, request: Request):
    """
    Returns the result of the operation of the SQL request by ID in url

    :return:

        "success": bool,
        "status": int (1 or 0)
        "request": [[]]
    """
    try:
        if not is_token_valid(request.headers):
            return {"success": False, "error": "invalid api_token"}

        response = get_response_by_id(response_id)

        if response:
            return {"success": True, "status": 1, "response": response}
        else:
            return {"success": True, "status": 0}

    except Exception as err:
        return {"success": False, "error": err.__str__()}

