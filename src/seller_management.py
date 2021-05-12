import mysql.connector



class SellerManagement:
    def add_new_seller(name, phone, email, address):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )

        my_cursor = my_db.cursor()
        command = "insert into seller_details(name, phone, email, address) values (\'{0}\', \'{1}\', \'{2}\', \'{3}\');".format(name, phone, email, address)
        my_cursor.execute(command)
        my_db.commit()

    def update_seller_contact(finder_keys, finder_values, tbc_keys, new_values):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )

        my_cursor = my_db.cursor()
        command = "UPDATE seller_details set "
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
            if finder_keys[-1] != finder_key:
                command += ', '
            else:
                command += ';'
        my_cursor.execute(command)
        my_db.commit()

SellerManagement