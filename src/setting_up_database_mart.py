import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="param_super_mart"
)

mycursor = mydb.cursor()
"""
# below query created database
mycursor.execute("CREATE DATABASE param_super_mart;")

"""
"""
# below query created stock type table
mycursor.execute("CREATE TABLE stock_type(type_id int auto_increment, stock_type varchar(100), primary key (type_id));")
"""
"""
# below query created seller details table
mycursor.execute("CREATE TABLE seller_details(seller_id int auto_increment default = 1, name varchar(50), phone varchar(20), email varchar(100), address varchar(200), primary key (seller_id));")

"""

"""
# below query created stock details table
mycursor.execute("CREATE TABLE stock_details(stock_id int auto_increment, stock_name varchar(1000), type_id int,  quantity int, sale_price float, seller_id int, purchase_price float, primary key (stock_id), foreign key (type_id) references stock_type(type_id), foreign key (seller_id) references seller_details(seller_id));")
"""

"""
# below query makes customer details table
mycursor.execute("CREATE TABLE customer_details(customer_id int auto_increment, name varchar(50), phone varchar(20), email varchar(100), address varchar(200), primary key (customer_id));")
"""
mycursor.execute("ALTER TABLE customer_purchase_details ALTER COLUMN )
"""
mycursor.execute("CREATE TABLE income_management(purchase_id int, customer_id int, total_cost float, foreign key (purchase_id) references customer_purchase_details(purchase_id), foreign key (customer_id) references customer_details(customer_id));")
"""