from extract.oltp_extract import *
from transform.oltp_transformations import *
from load.loader import copy_dataframe
from load.olap_schema import *
import pandas as pd

def main():

    olapSchema = "ecommerceolap_dw"

    # df_orders = extract_orders()
    # df_order_item = extract_order_item()
    dim_date = build_dim_date(extract_orders())
    # dim_customer = build_dim_customer(extract_customers(), extract_loyalty_program())
    # dim_store = build_dim_stores(extract_stores())
    # dim_product = build_dim_product(extract_products())


    # fact_sales = build_fact_sales(df_order_item, df_orders, dim_date, dim_customer, dim_product, dim_store)

    copy_dataframe(dim_date, f"{olapSchema}.dim_date")
    # print(create_olap_schema())
    # print(create_dim_date())








if __name__ == "__main__":
    main()