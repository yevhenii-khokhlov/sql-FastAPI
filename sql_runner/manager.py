from sql_runner.connections import get_cursor
from sql_runner.requests import simple_sql_request


def run_sql():
    data = []
    cursor = get_cursor()

    if cursor:
        cursor.execute(simple_sql_request)
        res = cursor.fetchall()
        data = [item[1] for item in res]

    return data
