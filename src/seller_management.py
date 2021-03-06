import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="param_super_mart"
)

mycursor = mydb.cursor()

class seller_management:
    def add_new_seller(name, phone, email, address):
        command = "insert into seller_details(name, phone, email, address) values (\'{0}\', \'{1}\', \'{2}\', \'{3}\');".format(name, phone, email, address)
        mycursor.execute(command)