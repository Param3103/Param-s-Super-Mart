import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="param_super_mart")

mycursor = mydb.cursor()


task = int(input("Hello Param, what will you like to do today?\nEnter 1 if you would like to add new type of items to your store.\
             \nEnter 2 if you would like to replenish existing stock.\nEnter 3 if you would like to add new vendors to your list.\n"))
if task == 1:
    print("Adding new type of item to store.")
    item_type = input("What type of item are you adding? ")
    existing_types = mycursor.execute("SELECT * FROM stock_type;")
    if item_type in existing_types:
        print("This item already exists.")
    else:
        mycursor.execute("INSERT INTO stock_type(type_id, stock_type) values ();")
    # if item_type in stock_type:
    #      print this item already exists
    # else
    #     insert into stock_type values (index, item_type
elif task == 2:
    print("Replenishing existing stock.")
elif task == 3:
    print("Adding new vendors.")
