from extract.oltp_extract import *
from transform.oltp_transformations import *
from load.loader import copy_dataframe
from load.olap_schema import *
import pandas as pd



def main():

    # Extracting and Transforming from Source
    # Dimention Tables
    print("Extraction started......")
    dim_date = build_dim_date(extract_orders())
    dim_customer = build_dim_customer(extract_customers(), extract_loyalty_program())
    dim_store = build_dim_stores(extract_stores())
    dim_product = build_dim_product(extract_products())

    # Fact Tables
    df_orders = extract_orders()
    df_order_item = extract_order_item()
    fact_sales = build_fact_sales(df_order_item, df_orders, dim_date, dim_customer, dim_product, dim_store)



    # Creating OLAP schema.
    create_dim_date()
    create_dim_customer()
    create_dim_product()
    create_dim_store()
    create_fact_sales()

    # Truncating the dimensional table.
    truncate_dw_olap()

    # Loading to the target.
    # Dimension Tables
    copy_dataframe(dim_date, f"{olapSchema}.dim_date")
    copy_dataframe(dim_product, f"{olapSchema}.dim_product")
    copy_dataframe(dim_customer, f"{olapSchema}.dim_customer")
    copy_dataframe(dim_store, f"{olapSchema}.dim_store")

    # Fact Tables
    copy_dataframe(fact_sales, f"{olapSchema}.fact_sales")

    print("ETL Completed Successfully......")


if __name__ == "__main__":
    main()