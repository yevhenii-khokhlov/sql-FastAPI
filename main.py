from fastapi import FastAPI

from services import get_ip
from sql_runner.manager import run_sql

app = FastAPI()


@app.get("/")
async def root_endpoint():
    return {"message": "Hello World"}


@app.get("/run-sql")
def run_sql_endpoint():
    result = run_sql()
    ip = get_ip()
    return {"message": result, "ip": ip}
