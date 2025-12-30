from database.olap_connection import get_olap_conn


conn = get_olap_conn()


cur = conn.cursor()

def create_olap_schema():

    cur.execute("""
            CREATE SCHEMA IF NOT EXISTS ecommerceolap_dw;
                """)
    
    conn.commit()
    
    return "Schema Created Successfully."


def create_dim_date():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ecommerceolap_dw.dim_date(
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL,
	day INT,
	month INT,
	month_name VARCHAR(20),
	quarter INT,
	year INT,
	weekday INT,
	weekday_name VARCHAR(20)
    );
    """)

    conn.commit()

    return "Dim_Date table has been created."