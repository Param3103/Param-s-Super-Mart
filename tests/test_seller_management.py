import unittest
import mysql.connector
from src.seller_management import seller_management
class Testing_Project(unittest.TestCase):
    def setUp(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )
        self.my_cursor = self.my_db.cursor()
    def tearDown(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )
        self.my_cursor = self.my_db.cursor()
        self.my_cursor.execute("DELETE FROM stock_type;")
        self.my_cursor.execute("ALTER TABLE stock_type AUTO_INCREMENT = 1;")
        self.my_cursor.execute("DELETE FROM stock_details;")
        self.my_cursor.execute("ALTER TABLE stock_details AUTO_INCREMENT = 1;")
        self.my_cursor.execute("DELETE FROM seller_details;")
        self.my_cursor.execute("ALTER TABLE seller_details AUTO_INCREMENT = 1;")
        self.my_db.commit()



    def test_add_new_seller(self):
        seller_management.add_new_seller("Param", "+65 9427 6963", "", "")
        values = self.my_cursor.execute("select * from seller_details;")
        print(values)
        self.assertIn(["Param", "+65 9427 6963", "", ""], values)
    def test_update_seller_contact(self):
        pass

if __name__ == '__main__':
    unittest.main()