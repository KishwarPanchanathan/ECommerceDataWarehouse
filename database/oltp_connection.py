import psycopg2
from config.oltp_config import OLTP_DB

def get_oltp_conn():
    with psycopg2.connect(
        host = OLTP_DB["host"],
        port = OLTP_DB["port"],
        dbname = OLTP_DB["dbname"],
        user = OLTP_DB["user"],
        password = OLTP_DB["password"]
    ) as conn:
        print("OLTP Connected Successfully.")
        
        return conn