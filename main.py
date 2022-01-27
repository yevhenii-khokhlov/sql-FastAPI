import json

from fastapi import FastAPI, Request

from sql_runner.manager import run_sql

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
    :param request:

        "selector": str

    :return:

        "success": bool,
        "query_result": [[]] or "error": str
    """
    try:
        raw_body = await request.body()
        body = json.loads(raw_body)
        selector = body.get('selector')
        result = run_sql(selector)

        return {"success": True, "query_result": result}

    except Exception as err:
        return {"success": False, "error": err.__str__()}
