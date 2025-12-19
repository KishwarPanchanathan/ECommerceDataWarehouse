from database.oltp_connection import get_oltp_conn
import pandas as pd

def extract_customers():
    conn = get_oltp_conn()
    query = "SELECT * FROM customers ;"
    df = pd.read_sql(query, conn)
    conn.close()
    print("Customers Table")
    return df

def extract_orders():
    conn = get_oltp_conn()
    query = "SELECT * FROM orders ;"
    df = pd.read_sql(query, conn)
    conn.close()
    print("Orders Table\n")
    return df

def extract_order_item():
    conn = get_oltp_conn()
    query = "SELECT * FROM order_items ;"
    df = pd.read_sql(query, conn)
    print("Order Item Table")
    return df

def extract_stores():
    conn = get_oltp_conn()
    query = "SELECT * FROM stores ;"
    df = pd.read_sql(query, conn)
    print("Stores Table")
    return df

def extract_products():

    conn = get_oltp_conn()
    query = "SELECT * FROM products ;"
    df = pd.read_sql(query, conn)
    print("Products Table")
    return df


def extract_loyalty_program():

    conn = get_oltp_conn()
    query = "SELECT * FROM loyalty_program ;"
    df = pd.read_sql(query, conn)
    print("Loyalty Program Table")
    return df