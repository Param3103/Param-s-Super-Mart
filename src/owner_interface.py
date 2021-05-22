from stock_management import StockManagement
from seller_management import SellerManagement
import mysql.connector
from constants import *

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="param_super_mart"
)

my_cursor = my_db.cursor()


if task == 1:
    print("Adding new type of item to store.")
    StockManagement.adding_new_type(str(stock_type))
elif task == 2:
    print("Replenishing existing stock. ")
    StockManagement.replenishing_stock(stock_name, qty)
elif task == 3:
    print("Adding new vendors.")
    name = input("What is the name of this vendor? ")
    SellerManagement.add_new_seller(name, phone, email, address)
elif task == 4:
    print("Updating details of vendors.")
    identifying_keys = []
    identifying_values = []
    for num in range(num_identifying_keys):
        identifying_keys.append(identifying_key)
        identifying_values.append(identifying_value)
    tbc_keys = []
    new_values = []
    for num in range(num_tbc_keys):
        tbc_keys.append(tbc_key)
        new_values.append(new_value)
    SellerManagement.update_seller_contact(identifying_keys, identifying_values, tbc_keys, new_values)
elif task == 5:
    my_cursor.execute("select seller_id from seller_details where name='{0}';".format(seller))
    seller_id = my_cursor.fetchall()[0]
    StockManagement.adding_new_stock(stock_name, type, quantity, price_when_bought, seller_id, price_for_customers)
elif task == 6:
    keys = []
    values = []
    for i in range(qty):
        keys.append(key)
        values.append(value)
    items = StockManagement.finding_stock(keys, values)
    for item in items:
        print(item)