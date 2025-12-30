
import pandas as pd
from load.olap_schema import *

def build_dim_date(df_orders):

    create_dim_date()

    df_orders["order_date"] = pd.to_datetime(df_orders["order_date"]).dt.normalize()

    dim_date = (df_orders[['order_date']]
                .drop_duplicates()
                .rename(columns={'order_date':'full_date'})
            )
    
    # Creating new columns for dim_date

    dim_date["date_key"] = dim_date["full_date"].dt.strftime("%Y%m%d").astype(int)
    dim_date["day"] = dim_date["full_date"].dt.day
    dim_date["month"] = dim_date["full_date"].dt.month
    dim_date["month_name"] = dim_date["full_date"].dt.month_name()
    dim_date["quarter"] = dim_date["full_date"].dt.quarter
    dim_date["year"] = dim_date["full_date"].dt.year
    dim_date["weekday"] = dim_date["full_date"].dt.weekday
    dim_date["weekday_name"] = dim_date["full_date"].dt.day_name()


    return dim_date


def build_dim_customer(df_customers, df_loyalty_program):

    dim_customer =  (
        df_customers.merge(df_loyalty_program[["customer_id","membership_tier"]], 
                           on = 'customer_id', 
                           how= 'left'
                        )
    )

    dim_customer["customer_key"] = dim_customer.index + 1

    dim_customer = dim_customer[
        ["customer_key", "customer_id", "first_name", 
         "last_name", "gender", "city", "state", "country", "join_date", "membership_tier"]
    ]

    return dim_customer

def build_dim_product(df_products):


    dim_product = (
        df_products[
                ["product_id", "product_name", "category","brand", "cost", "price", "is_active"]
            ]
    )

    dim_product["product_key"] = df_products.index + 1

    dim_product = dim_product[
        ["product_key", "product_id", "product_name", "category","brand", "cost", "price", "is_active"]
    ]

    return dim_product

def build_dim_stores(df_stores):

    dim_stores = (
        df_stores[
            ["store_id", "store_name","city", "state", "region"]
        ]
    )

    dim_stores.loc[:, "store_key"] = dim_stores.index + 1

    dim_stores = dim_stores[["store_key", "store_id", "store_name","city", "state", "region"]]

    return dim_stores

def build_fact_sales(df_order_items, df_orders, dim_date, dim_customer, dim_products, dim_stores):

    df_orders["order_date"] = pd.to_datetime(df_orders["order_date"])

    fact = (
        df_order_items.merge(
        df_orders[["order_id", "customer_id","store_id", "order_date"]],
        on = "order_id",
        how= "left"
        )
    )

    fact = fact.merge(dim_customer[["customer_key", "customer_id"]], on="customer_id")
    fact = fact.merge(dim_products[["product_key", "product_id","cost"]], on = "product_id")
    fact = fact.merge(dim_stores[["store_key", "store_id"]], on="store_id")
    fact = fact.merge(dim_date[["date_key", "full_date"]], left_on = "order_date", right_on = "full_date")

    fact["total_price"] = fact["quantity"] * fact["unit_price"] - fact["discount"]
    fact["profit"] = (fact["unit_price"] - fact["cost"]) * fact["quantity"]

    fact = fact[
        ["order_id", "date_key", "customer_key", "product_key", "store_key", "quantity", "unit_price","discount",
         "total_price", "profit"]
    ]

    return fact
