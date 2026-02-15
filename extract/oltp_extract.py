from database.oltp_connection import get_oltp_conn
import pandas as pd

def extract_customers():
    conn = get_oltp_conn()
    query = "SELECT * FROM customers ;"
    df = pd.read_sql(query, conn)
    conn.close()
    print("Data Extracted from Customers Table\n")
    return df

def extract_orders():
    conn = get_oltp_conn()
    query = "SELECT * FROM orders ;"
    df = pd.read_sql(query, conn)
    conn.close()
    print("Data Extracted from Orders Table\n")
    return df

def extract_order_item():
    conn = get_oltp_conn()
    query = "SELECT * FROM order_items ;"
    df = pd.read_sql(query, conn)
    print("Data Extracted from Order Item Table\n")
    return df

def extract_stores():
    conn = get_oltp_conn()
    query = "SELECT * FROM stores ;"
    df = pd.read_sql(query, conn)
    print("Data Extracted from Stores Table\n")
    return df

def extract_products():

    conn = get_oltp_conn()
    query = "SELECT * FROM products ;"
    df = pd.read_sql(query, conn)
    print("Data Extracted from Products Table\n")
    return df


def extract_loyalty_program():

    conn = get_oltp_conn()
    query = "SELECT * FROM loyalty_program ;"
    df = pd.read_sql(query, conn)
    print("Data Extracted from Loyalty Program Table\n")
    return df