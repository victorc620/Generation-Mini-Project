from file_handler import load_csv_to_list_of_dict, export_list_of_dict_to_csv

products_csv_header = ["name", "price"]
courier_csv_header = ["name", "phone"]
orders_csv_header = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]

def main_menu(prod_list, cour_list, orders_list):
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
        exit_program(prod_list, cour_list, orders_list)
    elif action == 1:
        item_menu(prod_list, "product")
    elif action == 2:
        item_menu(cour_list, "courier")
    elif action == 3:
        orders_menu(orders_list, prod_list, cour_list)

def item_menu(item_list: list, menu_name: str):
    """
    Product/Courier menu
    item_list: prod_list/cour_list
    menu_name: "product" or "courier"
    """
    
    prod_menu = """
------PRODUCT MENU------

0. Return to main menu
1. Print product list
2. Create new product
3. Update existing product
4. Delete product
"""

    cour_menu = """
------COURIER MENU------

0. Return to main menu
1. Print courier list
2. Create new courier
3. Update existing courier
4. Delete courier 
"""
    if menu_name == "product":
        menu_interface = prod_menu
    elif menu_name == "courier":
        menu_interface = cour_menu
    
    while True: #Product/Courier Menu Loop
        print(menu_interface)
        action = menu_input(4)
        
        if action == 0:
            return
        elif action == 1:
            print_item(item_list)
        elif action == 2:
            create_new_item(item_list, menu_name)
        elif action == 3:
            update_existing_item(item_list, menu_name)
        elif action == 4:
            delect_item(item_list, menu_name)

def orders_menu(orders_list, prod_list, cour_list):
    """
    Orders menu
    orders_list = orders_list
    status_list = status_list
    cour_list = cour_list
    """
    
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

    status_list = ["Preparing", "Awaiting Shipment", "Shipped", "Refunded"]

    while True:
        print(order_menu)
        action = menu_input(7)
        
        if action == 0:
            return
        elif action == 1: #elif
            print_item(orders_list)
        elif action == 2:
            create_new_order(orders_list,prod_list,cour_list)
        elif action == 3:
            update_order_status(orders_list, status_list)
        elif action == 4:
            update_existing_order(orders_list, status_list, prod_list, cour_list)
        elif action == 5:
            delect_item(orders_list, "order")
        elif action == 6:
            list_orders_by_key(orders_list, "status")
        elif action == 7:
            list_orders_by_key(orders_list, "courier")

def print_item(lists):
    for element in lists:
        print("")
        for key,values in element.items():
            print(f"{key}: {values}")

def exit_program(prod_list, cour_list, orders_list):
    """
    Export prod_list, cour_list, orders_list to csv file
    Exit the program
    """
    export_list_of_dict_to_csv("data/product.csv",prod_list, products_csv_header)
    export_list_of_dict_to_csv("data/courier.csv",cour_list, courier_csv_header)
    export_list_of_dict_to_csv("data/orders.csv", orders_list, orders_csv_header)
    print("Thanks for using me, Bye")
    exit()

def create_new_item(item_list, list_name):
    """
    Add a new product/couries to the product/courier list
    item_list: prod_list/ cour_list
    list_key_1: "product"/"courier"
    """
    item = {}
    item["name"] = input(f"Enter the {list_name} name: ")
    if list_name == "product":
        item["price"] = float(input(f"Enter the price: "))
    if list_name == "courier":
        item["phone"] = int(input(f"Enter the phone: "))
    
    item_list.append(item)
    print(item_list)
    return item_list

def update_existing_item(item_list, list_name):
    """
    Update an existing product/courier with new name
    item_list: prod_list/ cour_list
    list_name: "product"/"courier"
    """
    while True:
        print_index(item_list)
        try:
            new__index = int(input(f"Enter the index of the {list_name} to be updated: "))
            if new__index > (len(item_list)-1):
                raise Exception
        except Exception:
            print("\nERROR: Please enter an valid action!\n")
            continue
        
        new_item_name = input(f"Enter the name of the new {list_name}: ")
        item_list[new__index]["name"] = new_item_name
        if list_name == "product":
            item_list[new__index]["price"] = float(input(f"Enter the new price: "))
        if list_name == "courier":
            item_list[new__index]["phone"] = int(input(f"Enter the new phone: "))            
        print(item_list)
        return item_list
    
def delect_item(item_list, list_name):
    """
    Delete an existing item from the list
    item_list: prod_list/ cour_list
    list_name: "product"/"courier"
    """
    print_index(item_list)
    while True:
        try: 
            item_index = int(input(f"Enter the index of the {list_name} to be deleted: "))
        except Exception:
            print("\nERROR: Please enter an valid action!\n")
            continue
        item_list.pop(item_index)
        print(item_list)
        return item_list

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
"""
        )
    pass

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
    prod_list = load_csv_to_list_of_dict("data/product.csv")
    cour_list = load_csv_to_list_of_dict("data/courier.csv")
    orders_list = load_csv_to_list_of_dict("data/orders.csv")
    
    while True: #Main Menu Loop
        main_menu(prod_list, cour_list, orders_list)

if __name__ == "__main__":
    main()