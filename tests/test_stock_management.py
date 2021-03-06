import unittest
import mysql.connector
from src.stock_management import StockManagement
from src.seller_management import SellerManagement
class Testing_Stock_Management(unittest.TestCase):
    def setUp(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )
        self.my_cursor = self.my_db.cursor()

    def tearDown(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )
        self.my_cursor = self.my_db.cursor()
        self.my_cursor.execute("delete from stock_details;")
        self.my_cursor.execute(
            "ALTER TABLE stock_details AUTO_INCREMENT = 1;")
        self.my_cursor.execute("delete from seller_details;")
        self.my_cursor.execute(
            "ALTER TABLE seller_details AUTO_INCREMENT = 1;")
        self.my_cursor.execute("delete from stock_type;")
        self.my_cursor.execute(
            "ALTER TABLE stock_type AUTO_INCREMENT = 1;")
        self.my_db.commit()


    def test_adding_new_type(self):
        StockManagement.adding_new_type(self, "Coconut")
        self.my_cursor.execute("SELECT * FROM stock_type;")
        values = self.my_cursor.fetchall()
        self.assertIn((1, 'Coconut'), values)
        # done
    def test_adding_new_stock(self):
       # create new stock type
       StockManagement.adding_new_type(self, "Coconut")
       self.my_db.commit()

       # create new seller
       SellerManagement.add_new_seller(self, "Raj", "","", "")
       self.my_db.commit()

       # add new stock...
       StockManagement.adding_new_stock(self, "Raj Coconut", "Coconut", 50, 5.00, 1, 5.00)
       self.my_db.commit()

       # test
       self.my_cursor.execute("SELECT * FROM stock_details;")
       values = self.my_cursor.fetchall()
       self.assertIn((1, 'Raj Coconut', 1, 50, 5.0, 1, 5.0), values)
        # done
    def test_replenishing_stock(self):
        # create new stock type
        StockManagement.adding_new_type(self, "Coconut")
        self.my_db.commit()
        # create new seller
        SellerManagement.add_new_seller(self, 'Raj', '', '', '')
        self.my_db.commit()
        # add new stock...
        StockManagement.adding_new_stock(self, "Raj Coconut", "Coconut", 50, 5.00, 1, 5.50)
        self.my_db.commit()

        StockManagement.replenishing_stock(self, "Raj Coconut", 50)
        self.my_db.commit()

        self.my_cursor.execute("select quantity from stock_details;")
        qty = self.my_cursor.fetchall()
        self.assertEqual(qty[0][0], 100)
    def test_finding_stock(self):
        # create new stock type
        StockManagement.adding_new_type(self, "Coconut")
        self.my_db.commit()
        # create new seller
        SellerManagement.add_new_seller(self, 'Raj', None, None, None)
        self.my_db.commit()
        # add new stock...
        StockManagement.adding_new_stock(self, "Raj Coconut", "Coconut", 50, 5.00, 1, 5.50)
        self.my_db.commit()
        # finding stock by name
        stock = StockManagement.finding_stock(self, ["stock_name"], ["Raj Coconut"])
        self.assertIn((1, "Raj Coconut", 1, 50, 5.5, 1, 5.0), stock)
        # finding stock by seller
        stock = StockManagement.finding_stock(self, ["seller_id"], [1])
        self.assertIn((1, "Raj Coconut", 1, 50, 5.5, 1, 5.0), stock)
        # finding stock by type
        stock = StockManagement.finding_stock(self, ["type_id"], [1])
        self.assertIn((1, "Raj Coconut", 1, 50, 5.5, 1, 5.0), stock)

if __name__ == '__main__':
    unittest.main()