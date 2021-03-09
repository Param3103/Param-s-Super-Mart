import mysql.connector



class seller_management:
    def add_new_seller(name, phone, email, address):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )

        mycursor = mydb.cursor()
        command = "insert into seller_details(name, phone, email, address) values (\'{0}\', \'{1}\', \'{2}\', \'{3}\');".format(name, phone, email, address)
        mycursor.execute(command)
        mydb.commit()

    def update_seller_contact(finder_keys, finder_values, tbc_keys, new_values):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )

        mycursor = mydb.cursor()
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
        mycursor.execute(command)
        mydb.commit()

seller_management