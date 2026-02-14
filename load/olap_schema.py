from database.olap_connection import get_olap_conn


conn = get_olap_conn()


cur = conn.cursor()

def create_olap_schema():

    cur.execute("""
            CREATE SCHEMA IF NOT EXISTS ecommerceolap_dw;
                """)
    
    
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


def create_dim_product():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ecommerceolap_dw.dim_product(
                product_key SERIAL PRIMARY KEY,
                product_id VARCHAR(50),
                product_name VARCHAR(100),
                category VARCHAR(50),
                brand VARCHAR(50),
                cost NUMERIC(10,2),
                price NUMERIC(10,2),
                is_active BOOLEAN,
                stock_qty INT
                );     
        """)
    
    conn.commit()
    
    return "Dim_Product table has been created."

def create_dim_customer():

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ecommerceolap_dw.dim_customer(
        customer_key SERIAL PRIMARY KEY,
        customer_id VARCHAR(50),
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        gender VARCHAR(10),
        city VARCHAR(50),
        state VARCHAR(50),
        country VARCHAR(50),
        join_date DATE,
        membership_tier VARCHAR(20)
    ); """
    )

    conn.commit()

    return "Dim_Customer table has been created."

def create_dim_store():

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ecommerceolap_dw.dim_store(
        store_Key SERIAL PRIMARY KEY,
        store_id VARCHAR(50),
        store_name VARCHAR(100),
        city VARCHAR(50),
        state VARCHAR(50),
        region VARCHAR(50)
        );
        """
    )

    conn.commit()
    return "Dim_Store table has been cretaed."


def truncate_dw_olap():


    cur.execute(
        """
            TRUNCATE 
                ecommerceolap_dw.fact_sales,
                ecommerceolap_dw.dim_date,
                ecommerceolap_dw.dim_customer,
                ecommerceolap_dw.dim_product,
                ecommerceolap_dw.dim_store;
        """
    )

    conn.commit()

    return "Fact and Dimension tables are truncated."


def create_fact_sales():

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ecommerceolap_dw.fact_sales(
            sales_key SERIAL PRIMARY KEY,
            order_id VARCHAR(10),
            date_key INT REFERENCES ecommerceolap_dw.dim_date(date_key),
            customer_key INT REFERENCES ecommerceolap_dw.dim_customer(customer_key),
            product_key INT REFERENCES ecommerceolap_dw.dim_product(product_key),
            store_key INT REFERENCES ecommerceolap_dw.dim_store(store_key),
            quantity INT,
            unit_price NUMERIC(10,2),
            discount NUMERIC(10,2),
            total_price NUMERIC(10,2),
            profit NUMERIC(10,2)
            );
        """
    )

    conn.commit()

    return "Fact Sales table has been created."