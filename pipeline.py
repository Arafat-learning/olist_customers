# import libraries
import polars as pl

# read data 
items = pl.read_csv("../data/order_items.csv")
orders = pl.read_csv("../data/orders.csv")

# get list of Mikey's orders
def get_orders():
    df = items.filter(pl.col("seller_id") == "4869f7a5dfa277a7dca6462dcf3b52b2")
    df = df.select(["order_id", "order_item_id", "product_id", "price"])
    return df

# add customer info to Mikey's orders
def get_customers():
    df = get_orders()
    df = df.join(orders, on = "order_id", how = "left")
    df = df.select(["order_id", "order_item_id", "product_id", "price", "customer_id", "order_purchase_timestamp"])
    return df
