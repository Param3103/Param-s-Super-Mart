import unittest
import mysql.connector
from src.stock_management import stock_management
class Testing_Stock_Management(unittest.TestCase):
    def setUp(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )
        self.my_cursor = self.my_db.cursor()
    def tearDown(self):
        self.my_cursor.execute("delete from stock_type;")
        self.my_cursor.execute(
            "ALTER TABLE stock_type AUTO_INCREMENT = 1;")
        self.my_cursor.execute("delete from stock_details;")
        self.my_cursor.execute(
            "ALTER TABLE stock_details AUTO_INCREMENT = 1;")
        self.my_db.commit()

    def test_adding_new_type(self):
        stock_management.adding_new_type("Coconut")
        self.my_db.commit()
        self.my_cursor.execute("SELECT * FROM stock_type;")
        values = self.my_cursor.fetchall()
        self.assertIn((1, 'Coconut'), values)
    def test_adding_new_stock(self):
        stock_management.adding_new_type("Coconut")
        self.my_db.commit()
        stock_management.adding_new_stock("sammy's coconut", "coconut", 50, 2.50, "Singapore Farm", 3.00)
        self.my_db.commit()
        self.my_cursor.execute("SELECT * FROM stock_details;")
        values = self.my_cursor.fetchall()
        self.assertIn(("sammy's coconut", "coconut", 50, 2.50, "Singapore Farm", 3.00), values)
    def test_replenishing_stock(self):
        pass
if __name__ == '__main__':
    unittest.main()