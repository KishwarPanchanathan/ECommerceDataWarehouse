import psycopg2
from config.olap_config import OLAP_DB

def get_olap_conn():
    with  psycopg2.connect(
        host = OLAP_DB["host"],
        port = OLAP_DB["port"],
        dbname = OLAP_DB["dbname"],
        user = OLAP_DB["user"],
        password = OLAP_DB["password"]
    ) as conn:
        
        print("OLAP Connected Successfully.")
        
        return conn