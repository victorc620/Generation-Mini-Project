from file_handler import execute_query, load_csv_to_list_of_dict, export_list_of_dict_to_csv

products_csv_header = ["name", "price"]
courier_csv_header = ["name", "phone"]
orders_csv_header = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]

def main_menu(orders_list):
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
        pass
        # exit_program(cour_list, orders_list)
    elif action == 1:
        product_menu()
    elif action == 2:
        courier_menu()
    # elif action == 3:
    #     orders_menu(orders_list, prod_list, cour_list)

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

# def orders_menu(orders_list, prod_list, cour_list):
#     """
#     Orders menu
#     orders_list = orders_list
#     status_list = status_list
#     cour_list = cour_list
#     """
    
#     order_menu = """
# ------ORDERS MENU------

# 0. Return to main menu
# 1. Print order list
# 2. Create new order
# 3. Update existing order status
# 4. Update existing order
# 5. Delete order
# 6. List orders by status
# 7. List orders by courier
# """

#     status_list = ["Preparing", "Awaiting Shipment", "Shipped", "Refunded"]

#     while True:
#         print(order_menu)
#         action = menu_input(7)
        
#         if action == 0:
#             return
#         elif action == 1: #elif
#             print_item(orders_list)
#         elif action == 2:
#             create_new_order(orders_list,prod_list,cour_list)
#         elif action == 3:
#             update_order_status(orders_list, status_list)
#         elif action == 4:
#             update_existing_order(orders_list, status_list, prod_list, cour_list)
#         elif action == 5:
#             delect_item(orders_list, "order")
#         elif action == 6:
#             list_orders_by_key(orders_list, "status")
#         elif action == 7:
#             list_orders_by_key(orders_list, "courier")

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
def create_new_order(orders_list,prod_list, cour_list):
    """
    Create new order in the list of orders
    orders_list = orders_list
    cour_list = cour_list
    """
    orders_dict = {}
    orders_dict["customer_name"] = str(input("Input for customer name: "))
    orders_dict["customer_address"] = str(input("Input for customer address: "))
    orders_dict["customer_phone"] = str(input("Input for customer phone number: "))
    print_index(prod_list)
    item_index_string = str(input("Enter list of product index values (seperated with comma): "))
    print_index(cour_list)
    orders_dict["courier"] = int(input("Input the courier index to select courier: "))
    orders_dict["status"] = "Preparing"
    orders_dict["items"] =  [index.strip() for index in item_index_string.split(",")]
    orders_list.append(orders_dict)
    return orders_list

def update_order_status(orders_list, status_list):
    """
    Update an order status
    orders_list = orders_list
    status_list = status_list
    """
    while True:
        print_index(orders_list)
        try:
            new_order_index = int(input("Enter the index of the order to be updated: "))
            if new_order_index > (len(orders_list)-1):
                raise Exception
        except Exception:
            print("\nERROR: Please enter an valid action!\n")
            continue
                
        print_index(status_list)
        index_status = int(input("What is the new order status?: "))
        orders_list[new_order_index]["status"] = status_list[index_status]
        return

def update_existing_order(orders_list, status_list, prod_list, cour_list):
    """
    Update an existing order with new name
    orders_list = orders_list
    status_list = status_list
    cour_list = cour_list 
    """
    while True:
        print_index(orders_list)
        try:
            new_order_index = int(input("Enter the index of the order to be updated: "))
            if new_order_index > (len(orders_list)-1):
                raise Exception
        except Exception:
            print("\nERROR: Please enter an valid action!\n")
            continue
        
        cus_name = str(input("Input for customer name: "))
        if cus_name:
            orders_list[new_order_index]["customer_name"] = cus_name
            
        cus_address = str(input("Input for customer address: "))
        if cus_address:
            orders_list[new_order_index]["customer_address"] = cus_address            
            
        cus_phone = str(input("Input for customer phone number: "))
        if cus_phone:
            orders_list[new_order_index][ "customer_phone"] = cus_phone
            
        print_index(prod_list)
        item_index_string = str(input("Enter list of product index values (seperated with comma): "))
        
        print_index(cour_list)
        cour_index = input("Input the courier index to select courier: ")
        if cour_index:
            orders_list[new_order_index]["courier"] = int(cour_index)
            
        print_index(status_list)
        index_status = input("What is the new order status?: ")
        if index_status:
            orders_list[new_order_index]["status"] = status_list[int(index_status)] # Update status
        
        if item_index_string:
            orders_list[new_order_index]["items"] = [index.strip() for index in item_index_string.split(",")]
            
        return orders_list

def list_orders_by_key(orders_list, sort_by: str):
    """
    sort orders by keys in orders dict
    sort_by: key (status/courier)
    """
    def myFunc(e):
        return e[sort_by]
    temp_list = list(orders_list)
    temp_list.sort(key=myFunc)
    for item in temp_list:
        print(f"""
Name: {item["customer_name"]}
Address: {item["customer_address"]}
Phone: {item["customer_phone"]}
Courier: {item["courier"]}
Status: {item["status"]}
Item: {item["items"]}
""")


def print_index(name):
    """Print item in list with index"""
    for index, item in enumerate(name):
        print(index, item)

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
    # cour_list = load_csv_to_list_of_dict("data/courier.csv")
    orders_list = load_csv_to_list_of_dict("data/orders.csv")
    
    while True: #Main Menu Loop
        main_menu(orders_list)

if __name__ == "__main__":
    main()