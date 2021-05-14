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

