import mysql.connector

class Customer:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )
        self.my_cursor = self.my_db.cursor()
    def add_new_customer(self):
        command = "insert into customer_details(name, phone, email, address) values (\'{0}\', \'{1}\', \'{2}\', \'{3}\');".format(
            self.name, self.phone, self.email, self.address)
        self.my_cursor.execute(command)
        self.my_db.commit()
    def update_customer_contact(self, finder_keys, finder_values, tbc_keys, new_values):
        command = "UPDATE customer_details set "
        for tbc_key in tbc_keys:
            command += tbc_key
            command += '='
            command += '\''
            command += new_values[tbc_keys.index(tbc_key)]
            command += '\''
            if tbc_keys[-1] != tbc_key:
                command += ', '
        command += ' WHERE '
        for finder_key in finder_keys:
            command += finder_key
            command += '='
            command += '\''
            command += finder_values[finder_keys.index(finder_key)]
            command += '\''
            if tbc_keys[-1] != tbc_key:
                command += ', '
            else:
                command += ';'
        self.my_cursor.execute(command)
        self.my_db.commit()
    def sell_item_to_customer(self, customer_id, items_bought_stock_id, qty_of_items):
        net_cost = 0

        for item_stock_id in items_bought_stock_id:
            cost = 0
            item_price = self.my_cursor.execute("select sale_price from stock_details where stock_id={0};".format(item_stock_id))

            if qty_of_items[items_bought_stock_id.index(item_stock_id)] is not None and item_price is not None:
                cost += item_price * qty_of_items[items_bought_stock_id.index(item_stock_id)]
            net_cost += cost
            command = "insert into customer_purchase_details(customer_id, item_bought, quantity, net_price) values({0}, {1}, {2}, {3});".format(customer_id, item_stock_id, qty_of_items[items_bought_stock_id.index(item_stock_id)], cost)
            self.my_cursor.execute(command)
            self.my_db.commit()
        return(net_cost)
