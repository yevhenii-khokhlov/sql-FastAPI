import pyodbc

from config import get_settings

settings = get_settings()


def get_cursor():
    try:
        conn_tk = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; '
            'PORT=1433;'
            f'SERVER={settings.db_server}; '
            f'DATABASE={settings.db_database}; '
            f'UID={settings.db_username}; '
            f'PWD={settings.db_password}',
        )
        cursor = conn_tk.cursor()
        return cursor

    except Exception as err:
        raise ConnectionError(err.__str__())
