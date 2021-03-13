from src.stock_management import stock_management
from src.seller_management import seller_management
import mysql.connector
def test_adding_new_stock():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="param_super_mart"
    )
    my_cursor = mydb.cursor()
    print("hi")
    stock_management.adding_new_type("Coconut")
    seller_management.add_new_seller("Singapore Farm", "", "", "")
    mydb.commit()
    stock_management.adding_new_stock("Sammy's coconut", "coconut", 50, 2.50, "Singapore Farm", 3.00)
    mydb.commit()
    my_cursor.execute("SELECT * FROM stock_details;")
    values = my_cursor.fetchall()
    print("done")
    return (1, "sammy's coconut", 1, 50, 2.50, 1, 3.00) in values

test_adding_new_stock()