import unittest
import mysql.connector
from src.seller_management import SellerManagement
class Testing_Seller_Management(unittest.TestCase):
    def setUp(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )
        self.my_cursor = self.my_db.cursor()
    def tearDown(self):
        self.my_cursor.execute("delete from seller_details;")
        self.my_cursor.execute(
            "ALTER TABLE seller_details AUTO_INCREMENT = 1;")
        self.my_db.commit()

    def test_add_new_seller(self):
        SellerManagement.add_new_seller("Param", "+65 9427 6963", "", "")
        self.my_db.commit()
        self.my_cursor.execute("SELECT * FROM seller_details;")
        values = self.my_cursor.fetchall()
        self.assertIn((1, 'Param', '+65 9427 6963', '', ''), values)
    def test_update_seller_contact(self):
        SellerManagement.add_new_seller("Param", "+65 9427 6963", "", "")
        self.my_db.commit()
        SellerManagement.update_seller_contact(['Name'], ['Param'], ['Email'], ['param@gmail.com'])
        self.my_db.commit()
        self.my_cursor.execute("SELECT * FROM seller_details;")
        values = self.my_cursor.fetchall()
        self.assertNotIn((1, 'Param', '+65 9427 6963', '', ''), values)
        self.assertIn((1, 'Param', '+65 9427 6963', 'param@gmail.com', ''), values)
if __name__ == '__main__':
    unittest.main()

# done