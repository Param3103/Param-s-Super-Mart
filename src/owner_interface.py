from stock_management import stock_management


task = int(input("Hello Param, what will you like to do today?\nEnter 1 if you would like to add new type of items to your store.\
             \nEnter 2 if you would like to replenish existing stock.\nEnter 3 if you would like to add new vendors to your list.\n\
             Enter 4 if you are adding new brand of item to the store. \n"))
if task == 1:
    print("Adding new type of item to store.")
    stock_type = input("What type of item are you adding to the store? ")
    stock_management.adding_new_type(str(stock_type))
elif task == 2:
    print("Replenishing existing stock. ")

elif task == 3:
    print("Adding new vendors.")
elif task == 4:
    print("Adding new brand.")
