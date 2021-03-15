import unittest
import mysql.connector
from src.stock_management import stock_management
from src.seller_management import seller_management
class Testing_Stock_Management(unittest.TestCase):
    def setUp(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )
        self.my_cursor = self.mydb.cursor()
    def tearDown(self):
        self.my_cursor.execute("delete from stock_type;")
        self.my_cursor.execute(
            "ALTER TABLE stock_type AUTO_INCREMENT = 1;")
        self.my_cursor.execute("delete from stock_details;")
        self.my_cursor.execute(
            "ALTER TABLE stock_details AUTO_INCREMENT = 1;")
        self.my_cursor.execute("delete from seller_details;")
        self.my_cursor.execute(
            "ALTER TABLE seller_details AUTO_INCREMENT = 1;")
        self.mydb.commit()

    def test_adding_new_type(self):
        stock_management.adding_new_type("Coconut")
        self.my_cursor.execute("SELECT * FROM stock_type;")
        values = self.my_cursor.fetchall()
        self.assertIn((1, 'Coconut'), values)
        # done
    def test_adding_new_stock(self):
# STILL NEED TO WORK ON THIS
       # create new stock type
       stock_management.adding_new_type("Coconut")
       self.mydb.commit()
       # create new seller
       seller_management.add_new_seller('Raj', None, None, None)
       self.mydb.commit()
       # add new stock...
       stock_management.adding_new_stock("Raj's Coconut", "Coconut", 50, 5.00, "Raj", 5.50)
       self.mydb.commit()
       self.my_cursor.execute("SELECT * FROM stock_details;")
       values = self.my_cursor.fetchall()
       self.assertIn([1, "Raj's Coconut", 1, 50, 5.00, 1, 5.50], values)
    def test_replenishing_stock(self):
        # create new stock type
        stock_management.adding_new_type("Coconut")
        self.mydb.commit()
        # create new seller
        seller_management.add_new_seller('Raj', None, None, None)
        self.mydb.commit()
        # add new stock...
        stock_management.adding_new_stock("Raj's Coconut", "Coconut", 50, 5.00, "Raj", 5.50)
        self.mydb.commit()
        stock_management.replenishing_stock("Raj's Coconut", 50)
        qty = self.my_cursor.execute("select quantity from stock_details;")
        self.assertEqual(qty, 100)
if __name__ == '__main__':
    unittest.main()