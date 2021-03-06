import mysql.connector


class stock_management:
    def adding_new_type(item_types):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )

        mycursor = mydb.cursor()
        command = "insert into stock_type(stock_type) values (\"{}\");".format(item_types)
        mycursor.execute(command)
        mydb.commit()
        print("{} has been added into the database.".format(item_types))
        # done

    def adding_new_stock(stock_name, type, quantity, price_when_bought, seller, price_for_customers):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )

        mycursor = mydb.cursor()
        type_id = mycursor.execute("select type_id from stock_type where stock_type={1};".format(type))
        seller_id = mycursor.execute("select seller_id from stock_details where name={0};".format(seller))
        mycursor.execute("insert into  stock_details values({3}, {4}, {0}, {1}, {5}, {2};".format(quantity, \
                                                    price_for_customers, price_when_bought, stock_name, type_id, seller_id))
        print("new stock has been added.")
    def replenishing_stock(name, quantity):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )

        mycursor = mydb.cursor()
        current_qty = int(mycursor.execute("select quantity from stock_details where stock_name={0};".format(name)))
        new_qty = current_qty + quantity
        mycursor.execute("update stock_details set quantity={1} where stock_name={0}".format(name,new_qty))
stock_management