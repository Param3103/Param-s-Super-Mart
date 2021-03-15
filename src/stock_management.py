import mysql.connector


class stock_management:
    def adding_new_type(item_type):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )

        mycursor = mydb.cursor()
        command = "insert into stock_type(stock_type) values (\"{}\");".format(item_type)
        mycursor.execute(command)
        mydb.commit()
        print("{} has been added into the database.".format(item_type))
        # done

    def adding_new_stock(stock_name, type, quantity, price_when_bought, seller, price_for_customers):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )

        mycursor = mydb.cursor()
        type_id = mycursor.execute("select type_id from stock_type where stock_type=\'{0}\';".format(type))
        seller_id = mycursor.execute("select seller_id from seller_details where name=\'{0}\';".format(seller))

        mycursor.execute(("insert into stock_details(stock_name, type_id, quantity, sale_price, seller_id, purchase_price) values(\'{3}\', {4}, {0}, {1}, {5}, {2});".format(quantity, price_for_customers, price_when_bought, stock_name, type_id, seller_id)))
        mydb.commit()
        print("new stock has been added.")

    def replenishing_stock(name, quantity):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )

        mycursor = mydb.cursor()
        current_qty = int(mycursor.execute("select quantity from stock_details where stock_name=\'{0}\';".format(name)))
        new_qty = current_qty + quantity
        mycursor.execute("update stock_details set quantity={1} where stock_name=\'{0}\'".format(name,new_qty))
        mydb.commit()
stock_management