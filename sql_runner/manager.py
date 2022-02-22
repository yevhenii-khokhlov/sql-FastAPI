from services import mc
from sql_runner.connections import get_cursor


def run_sql(selector, background=False, response_id=None):
    """Select data from TK database and return it as [[]]"""
    cursor = get_cursor()
    cursor.execute(selector)
    res = cursor.fetchall()
    data = [list(item) for item in res]

    if background:
        mc.set(response_id, data)
    else:
        return data
