import unittest
import mysql.connector
from src.customer_management import Customer
from src.stock_management import StockManagement
from src.seller_management import SellerManagement
class Testing_Customer_Management(unittest.TestCase):
    def setUp(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )
        self.my_cursor = self.my_db.cursor(buffered=True)
        self.customer = Customer("Param", "+65 9427 6963", "", "")
    def tearDown(self):
        self.my_cursor.execute("delete from customer_purchase_details;")
        self.my_db.commit()
        self.my_cursor.execute(
            "ALTER TABLE customer_purchase_details AUTO_INCREMENT;")
        self.my_db.commit()
        self.my_cursor.execute("delete from customer_details;")
        self.my_db.commit()
        self.my_cursor.execute(
            "ALTER TABLE customer_details AUTO_INCREMENT;")
        self.my_db.commit()
        self.my_cursor.execute("delete from income_management;")
        self.my_db.commit()
        self.my_cursor.execute(
            "ALTER TABLE income_management AUTO_INCREMENT;")
        self.my_db.commit()
        self.my_cursor.execute("delete from stock_details;")
        self.my_db.commit()
        self.my_cursor.execute(
            "ALTER TABLE stock_details AUTO_INCREMENT;")
        self.my_db.commit()
        self.my_cursor.execute("delete from stock_type;")
        self.my_db.commit()
        self.my_cursor.execute(
            "ALTER TABLE stock_type AUTO_INCREMENT;")
        self.my_db.commit()
        self.my_cursor.execute("delete from seller_details;")
        self.my_db.commit()
        self.my_cursor.execute(
            "ALTER TABLE seller_details AUTO_INCREMENT;")
        self.my_db.commit()
    def test_add_new_customer(self):
        Customer.add_new_customer(self.customer)
        self.my_db.commit()
        self.my_cursor.execute("SELECT * FROM customer_details;")
        values = self.my_cursor.fetchall()
        self.assertIn((1, 'Param', '+65 9427 6963', '', ''), values)
    def test_update_customer_contact(self):
        Customer.add_new_customer(self.customer)
        self.my_db.commit()
        Customer.update_customer_contact(self.customer, ['name'], ['Param'], ['email'], ['param@gmail.com'])
        self.my_db.commit()
        self.my_cursor.execute("SELECT * FROM customer_details;")
        values = self.my_cursor.fetchall()
        self.assertNotIn((1, 'Param', '+65 9427 6963', '', ''), values)
        self.assertIn((3, 'Param', '+65 9427 6963', 'param@gmail.com', ''), values)
    def test_sell_item_to_customer(self):
        Customer.add_new_customer(self.customer)
        self.my_db.commit()
        StockManagement.adding_new_type(self, "Coconut")
        self.my_db.commit()
        # create new seller
        SellerManagement.add_new_seller(self.customer, 'Raj', '', '', '')
        self.my_db.commit()
        # add new stock...
        StockManagement.adding_new_stock(self, "Raj Coconut", "Coconut", 50, 5.00, 1, 5.50)
        self.my_db.commit()

        # conducting transaction
        Customer.sell_item_to_customer(1, 1, [1], [50])

        self.my_db.commit()

        self.my_cursor.execute("SELECT * FROM customer_purchase_details;")
        values = self.my_cursor.fetchall()
        self.assertIn((1, 1, 1, 50, 50), values)

if __name__ == '__main__':
    unittest.main()

# done