from extract.oltp_extract import *
from transform.oltp_transformations import build_dim_date, build_dim_customer


def main():
    # print(build_dim_date(extract_orders()))
    print(build_dim_customer(extract_customers(), extract_loyalty_program()))
    # print(extract_order_item())
    # print(extract_stores())
    # print(extract_products())
    # print(extract_loyalty_program())


if __name__ == "__main__":
    main()