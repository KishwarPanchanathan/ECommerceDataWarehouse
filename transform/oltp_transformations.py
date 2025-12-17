
import pandas as pd

def build_dim_date(df_orders):
    df_orders["order_date"] = pd.to_datetime(df_orders["order_date"])

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