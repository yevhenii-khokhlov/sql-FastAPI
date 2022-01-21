from fastapi import FastAPI

from services import get_ip
from sql_runner.manager import run_sql

app = FastAPI()


@app.get("/")
async def root_endpoint():
    return {"success": True}


@app.get("/run-sql")
def run_sql_endpoint():
    result = run_sql()
    ip = get_ip()
    return {"success": True, "ip": ip, "sql": result}
