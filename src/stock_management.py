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
        # done

    def adding_new_stock(stock_name, type, quantity, price_when_bought, seller_id, price_for_customers):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )
        my_cursor = mydb.cursor()

        price_for_customers = float(price_for_customers)

        type_id_command = "select type_id from stock_type where stock_type=\'" + type + "\';"
        my_cursor.execute(type_id_command)

        type_id = my_cursor.fetchall()
        my_cursor.execute("INSERT INTO stock_details (stock_name, type_id, quantity, sale_price, seller_id,purchase_price) VALUES (\'{3}\', {4}, {0}, {1}, {5}, {2});".format(quantity, price_for_customers,price_when_bought, stock_name, type_id[0][0], seller_id[0]))
        mydb.commit()
        print("new stock has been added.")

    def replenishing_stock(name, quantity):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart",
        )

        mycursor = mydb.cursor()
        mycursor.execute("select quantity from stock_details where stock_name=\'{0}\';".format(name))
        current_qty = mycursor.fetchall()
        current_qty = current_qty[0][0]
        new_qty = current_qty + quantity
        mycursor.execute("update stock_details set quantity={1} where stock_name=\'{0}\';".format(name,new_qty))
        mydb.commit()

stock_management