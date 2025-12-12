from extract.oltp_extract import *


def main():
    print(extract_orders())
    print(extract_customers())
    print(extract_order_item())
    print(extract_stores())
    print(extract_products())
    print(extract_loyalty_program())


if __name__ == "__main__":
    main()