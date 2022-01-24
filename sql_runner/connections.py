import pyodbc

from config import get_settings


def get_cursor():
    settings = get_settings()
    try:
        conn_tk = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; '
            'SERVER=' + settings.db_server + '; '
            'DATABASE=' + settings.db_database + '; '
            'UID=' + settings.db_username + '; '
            'PWD=' + settings.db_password,

            timeout=5,
        )
        cursor = conn_tk.cursor()
        return cursor

    except Exception as err:
        raise ConnectionError(err.__str__())
