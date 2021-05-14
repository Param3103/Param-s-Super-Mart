import unittest
import mysql.connector
from src.customer_management import Customer
class Testing_Customer_Management(unittest.TestCase):
    def setUp(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )
        self.my_cursor = self.my_db.cursor()
        self.customer = Customer("Param", "+65 9427 6963", "", "")
    def tearDown(self):
        self.my_cursor.execute("delete from customer_details;")
        self.my_cursor.execute(
            "ALTER TABLE customer_details AUTO_INCREMENT = 1;")
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
        self.assertIn((1, 'Param', '+65 9427 6963', 'param@gmail.com', ''), values)
if __name__ == '__main__':
    unittest.main()

# done