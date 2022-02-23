import socket

from services import save_response_to_cache
from sql_runner.connections import get_cursor


def run_sql(selector, background=False, response_id=None):
    """Select data from TK database and return it as [[]]"""
    cursor = get_cursor()
    cursor.execute(selector)
    res = cursor.fetchall()
    data = [list(item) for item in res]

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print('local_ip', local_ip)

    if background:
        save_response_to_cache(data, response_id)
    else:
        return data
