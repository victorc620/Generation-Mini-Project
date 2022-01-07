from typing import ItemsView
from file_handler import execute_query, load_csv_to_list_of_dict, export_list_of_dict_to_csv

def main_menu():
    main_menu = """
------MAIN MENU------

0. Exit the app
1. Enter product menu
2. Enter courier menu
3. Enter order menu
"""
    print(main_menu)        
    action = menu_input(3)
    
    if action == 0:
        exit()
    elif action == 1:
        product_menu()
    elif action == 2:
        courier_menu()
    elif action == 3:
        orders_menu()

def product_menu():
    
    prod_menu = """
------PRODUCT MENU------

0. Return to main menu
1. Print product list
2. Create new product
3. Update existing product
4. Delete product
"""

    while True: #Product/Courier Menu Loop
        print(prod_menu)
        action = menu_input(4)
        
        if action == 0:
            return
        elif action == 1:
            print_item("SELECT * FROM product")
        elif action == 2:
            create_new_product()
        elif action == 3:
            update_existing_product()
        elif action == 4:
            delete_product()
            
def courier_menu():

    cour_menu = """
------COURIER MENU------

0. Return to main menu
1. Print courier list
2. Create new courier
3. Update existing courier
4. Delete courier 
"""

    while True: #Product/Courier Menu Loop
        print(cour_menu)
        action = menu_input(4)
        
        if action == 0:
            return
        elif action == 1:
            print_item("SELECT * FROM courier")
        elif action == 2:
            create_new_courier()
        elif action == 3:
            update_existing_product()
        elif action == 4:
            delete_courier()

def orders_menu():
    
    order_menu = """
------ORDERS MENU------

0. Return to main menu
1. Print order list
2. Create new order
3. Update existing order status
4. Update existing order
5. Delete order
6. List orders by status
7. List orders by courier
"""

    while True:
        print(order_menu)
        action = menu_input(7)
        
        if action == 0:
            return
        elif action == 1: #elif
            print_item("SELECT * FROM orders")
        elif action == 2:
            create_new_order()
        elif action == 3:
            update_order_status()
        elif action == 4:
            update_existing_orders()
        elif action == 5:
            delete_orders()
        # elif action == 6:
        #     list_orders_by_key(orders_list, "status")
        # elif action == 7:
        #     list_orders_by_key(orders_list, "courier")

def print_item(statment):
    """Print out content from Database
    statment: MySQL statment"""
    lists = execute_query(statment)
    for element in lists:
        print("")
        for key,values in element.items():
            print(f"{key}: {values}")
    return lists

def create_new_product():
    name = input(f"Enter the product name: ")
    price = input(f"Enter the price: ")
    sql = "INSERT IGNORE INTO product (name, price) VALUES (%s,%s)"
    val = (name, price)
    execute_query(sql, val)
    
def update_existing_product():
    print_item("SELECT * FROM product")
    id_input = int(input("Enter the product's ID: "))
    name = str(input("Enter the new product name: "))
    price = float(input("Enter the new price: "))
    sql = "UPDATE product SET name = %s, price = %s WHERE id = %s"
    val = (name, price, id_input)
    execute_query(sql, val)

def delete_product():
    print_item("SELECT * FROM product")
    id_input = int(input("Enter the ID of product to be deleted: "))
    sql = "DELETE FROM product WHERE id = %s"
    val = id_input
    execute_query(sql, val)

#-------------------------------------------------------------
def create_new_courier():
    name = input(f"Enter the courier name: ")
    phone = input(f"Enter the phone: ")
    sql = "INSERT IGNORE INTO courier (name, phone) VALUES (%s,%s)"
    val = (name, phone)
    execute_query(sql, val)
    
def update_existing_courier():
    print_item("SELECT * FROM courier")
    id_input = int(input("Enter the courier's ID: "))
    name = str(input("Enter the new courier name: "))
    phone = int(input("Enter the new phone number: "))
    sql = "UPDATE product SET name = %s, phone = %s WHERE id = %s"
    val = (name, phone, id_input)
    #TO DO: IF an input is empty, do not update its respective table property Update properties for courier in courier table
    execute_query(sql, val)
    
def delete_courier():
    print_item("SELECT * FROM courier")
    id_input = int(input("Enter the ID of courier to be deleted: "))
    sql = "DELETE FROM courier WHERE id = %s"
    val = id_input
    execute_query(sql, val)

#------------------------------------------------------------
def create_new_order():
    customer_name = str(input("Input for customer name: "))
    customer_address = str(input("Input for customer address: "))
    customer_phone = str(input("Input for customer phone number: "))
    print_item("SELECT * FROM courier")
    courier_id = int(input("Input the courier index to select courier: "))
    status = "Preparing"
    print_item("SELECT * FROM product")
    item_str = str(input("Enter list of product index values (seperated with comma): "))
    sql = ("INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, delivery_status, items) VALUES (%s,%s,%s,%s,%s,%s)")
    val = (customer_name, customer_address, customer_phone, courier_id, status, item_str)
    execute_query(sql, val)
    
def update_order_status():
    orders_status = {0:"Preparing", 1:"Waiting for Pickup", 2:"Delivered"}
    
    print_item("SELECT * FROM orders")
    input_id = int(input("Which order your want to update?: ")) 
    print_dict(orders_status)
    input_status = int(input("What is the new orders status?: "))
    new_status = orders_status[input_status]
    sql = ("UPDATE orders SET delivery_status = %s WHERE customer_id = %s")
    val = (new_status, input_id)
    execute_query(sql, val)

def update_existing_orders():
    orders_status = {0:"Preparing", 1:"Waiting for Pickup", 2:"Delivered"}
    print_item("SELECT * FROM orders")
    input_id = int(input("Which order your want to update?: "))
    customer_name = str(input("Input for customer name: "))
    customer_address = str(input("Input for customer address: "))
    customer_phone = str(input("Input for customer phone number: "))
    
    print_item("SELECT * FROM courier")
    courier_id = int(input("Input the courier index to select courier: "))
    
    print_dict(orders_status)
    input_status = int(input("Input the courier index to select courier: "))
    status = orders_status[input_status]
    
    print_item("SELECT * FROM product")
    item_str = str(input("Enter list of product index values (seperated with comma): "))
    
    sql = ("UPDATE orders SET customer_name=%s, customer_address=%s, customer_phone=%s, courier_id=%s, delivery_status=%s, items=%s WHERE customer_id = %s")
    val = (customer_name, customer_address, customer_phone, courier_id, status, item_str, input_id)
    execute_query(sql, val)

def delete_orders():
    print_item("SELECT * FROM orders")
    input_id = int(input("Enter the customer id to delete orders: "))
    sql = ("DELETE FROM orders WHERE customer_id = %s")
    val = (input_id)
    execute_query(sql, val)

# def list_orders_by_key(orders_list, sort_by: str):
#     """
#     sort orders by keys in orders dict
#     sort_by: key (status/courier)
#     """
#     def myFunc(e):
#         return e[sort_by]
#     temp_list = list(orders_list)
#     temp_list.sort(key=myFunc)
#     for item in temp_list:
#         print(f"""
# Name: {item["customer_name"]}
# Address: {item["customer_address"]}
# Phone: {item["customer_phone"]}
# Courier: {item["courier"]}
# Status: {item["status"]}
# Item: {item["items"]}
# """)


def print_index(name):
    """Print item in list with index"""
    for index, item in enumerate(name):
        print(index, item)
        
def print_dict(name):
    for key, value in name.items(): 
        print(f"{key} {value}")

def menu_input(max_menu_index):
    while True:
        try:
            action = int(input("Enter your action: "))
            if action>max_menu_index:
                raise Exception
        except Exception:
            print("\nERROR: Please enter an valid action")
            continue
        return action

def main():
    while True: #Main Menu Loop
        main_menu()

if __name__ == "__main__":
    main()