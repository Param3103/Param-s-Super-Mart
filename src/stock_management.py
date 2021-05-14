import mysql.connector


class StockManagement:
    def __init__(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="param_super_mart"
        )

        self.my_cursor = self.my_db.cursor()
    def adding_new_type(self,item_type):
        command = "insert into stock_type(stock_type) values (\"{}\");".format(item_type)
        self.my_cursor.execute(command)
        self.my_db.commit()
        # done

    def adding_new_stock(self, stock_name, stock_type, quantity, price_when_bought, seller_id, price_for_customers):

        price_for_customers = float(price_for_customers)
        price_when_bought = float(price_when_bought)

        type_id_command = "select type_id from stock_type where stock_type=\'" + stock_type + "\';"
        self.my_cursor.execute(type_id_command)

        type_id = self.my_cursor.fetchall()[0]
        self.my_cursor.execute("INSERT INTO stock_details (stock_name, type_id, quantity, sale_price, seller_id,purchase_price )VALUES (\'{3}\', {4}, {0}, {1}, {5}, {2});".format(quantity, price_for_customers, price_when_bought, stock_name, type_id[0], seller_id))
        self.my_db.commit()
        print("new stock has been added.")

    def replenishing_stock(self, name, quantity):
        self.my_cursor.execute("select quantity from stock_details where stock_name=\'{0}\';".format(name))
        current_qty = self.my_cursor.fetchall()
        current_qty = current_qty[0][0]
        new_qty = current_qty + quantity
        self.my_cursor.execute("update stock_details set quantity={1} where stock_name=\'{0}\';".format(name,new_qty))
        self.my_db.commit()

    def finding_stock(self, keys, values):

        command = 'select * from stock_details where '
        for key in keys:
            if type(values[keys.index(key)]) != int:
                command += key
                command += '='
                command +='\''
                command += values[keys.index(key)]
                command += '\''
            else:
                command += key
                command += '='
                command += str(values[keys.index(key)])
            if keys.index(key) != len(keys) - 1:
                command += ' and '
            else:
                command += ';'
        self.my_cursor.execute(command)
        stocks = self.my_cursor.fetchall()
        return(stocks)


StockManagement