from sql_runner.connections import get_cursor


def run_sql(selector):
    """Select data from TK database and return it as [[]]"""
    cursor = get_cursor()
    cursor.execute(selector)
    res = cursor.fetchall()
    data = [list(item) for item in res]

    return data
