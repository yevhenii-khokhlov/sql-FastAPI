from fastapi import FastAPI

from services import get_ip
from sql_runner.manager import run_sql

app = FastAPI()


@app.get("/")
async def root_endpoint():
    ip = get_ip()
    return {"success": True, "ip": ip}


@app.get("/run-sql")
def run_sql_endpoint():
    result = run_sql()
    return {"success": True, "sql": result}
