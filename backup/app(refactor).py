import csv

# Global Variables
prog_welcome = """
******CAFE APP*******
Welcome to the Program!
Your initial product list have been loaded into the programe
Your initial courier list have been loaded into the programe
Plese Enjoy~!
"""

main_menu = """
------MAIN MENU------

0. Exit the app
1. Enter product menu
2. Enter courier menu
3. Enter Orders Menu
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

order_menu = """
------ORDERS MENU------
0. Return to main menu
1. Print order dictionary
2. Create new order
3. Update existing order status
4. Update existing order
"""

#General Function:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_index(name):
    """
    Input: a list
    Output: print: index name 
    """
    for index, item in enumerate(name):
        print(index, item)
        
# Menu operation~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def create_new_item(list, list_name):
    """
    Add a new product/couries to the product/courier list
    """
    item = input(f"Enter the {list_name} name: ")
    list.append(item)
    print(list)
    return list

def create_new_order():
    """
    Create new orders in the list of dict(orders)
    """
    orders_dict = {}
    orders_dict["customer_name"] = str(input("Input for customer name: "))
    orders_dict["customer_address"] = str(input("Input for customer address: "))
    orders_dict["customer_phone_number"] = str(input("Input for customer phone number: "))
    print_index(cour_list)
    orders_dict["courier"] = cour_list[int(input("Input the courier index to select courier: "))]
    orders_dict["status"] = "Preparing"
    orders_list.append(orders_dict)
    
def update_existing_item(list, list_name):
    """
    Update an existing product/courier with new name  
    """
    while True:
        print_index(list)
        try:
            new__index = int(input(f"Enter the index of the {list_name} to be updated: "))
            if new__index > (len(list)-1):
                raise Exception
        except Exception:
            print("\nERROR: Please enter an valid action!\n")
            continue
        
        new_item_name = input(f"Enter the name of the new {list_name}: ")
        list[new__index] = new_item_name
        print(list)
        return list

def update_existing_order():
    """
    Update an existing order with new name  
    """
    while True:
        print_index(orders_list)
        try:
            new_order_index = int(input("Enter the index of the order to be updated: "))
            if new_order_index > (len(cour_list)-1):
                raise Exception
        except Exception:
            print("\nERROR: Please enter an valid action!\n")
            continue
        
        cus_name = str(input("Input for customer name: "))
        update_order_property(new_order_index, "customer_name", cus_name)
        
        cus_address = str(input("Input for customer address: "))            
        update_order_property(new_order_index, "customer_address", cus_address)
        
        cus_phone = str(input("Input for customer phone number: "))
        update_order_property(new_order_index, "customer_phone_number", cus_phone)
        
        print_index(cour_list)
        cour_index = input("Input the courier index to select courier: ")
        if cour_index:
            orders_list[new_order_index]["courier"] = cour_list[int(cour_index)]
        
        print_index(status_list)
        index_status = input("What is the new order status?: ")
        if index_status:
            orders_list[new_order_index]["status"] = status_list[int(index_status)] # Update status
        return

def update_order_property(index, key, value): #Check wether value is True
        if value:
            orders_list[index][key] = value
    
def update_order_status():
    """
    Update an existing order status
    """
    while True:
        print_index(orders_list)
        try:
            new_order_index = int(input("Enter the index of the order to be updated: "))
            if new_order_index > (len(cour_list)-1):
                raise Exception
        except Exception:
            print("\nERROR: Please enter an valid action!\n")
            continue
                
        print_index(status_list)
        index_status = int(input("What is the new order status?: "))
        orders_list[new_order_index]["status"] = status_list[index_status] # Update status
        return

def delect_item(list, list_name):
    """
    Delete an existing item from the list
    """
    print_index(list)
    while True:
        try: 
            item_index = int(input(f"Enter the index of the {list_name} to be deleted: "))
        except Exception:
            print("\nERROR: Please enter an valid action!\n")
            continue
        list.pop(item_index)
        print(list)
        return list

# I/O~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_prod_list():
    """
    Load from product.txt to creat a list of product from file
    """
    with open("product.txt", "r") as productfile:
        prod_list = []
        for name in productfile:
            prod_list.append(name.rstrip())
        
        return prod_list

def load_cour_list():
    """
    Load from courier.txt to creat a list of courier from file
    """
    with open("courier.txt", "r") as courfile:
        cour_list = []
        for name in courfile:
            cour_list.append(name.rstrip())
        
        return cour_list
    
def load_orders_list():
    """
    Load from orders.txt to creat a list of orders from file
    """
    with open("orders.txt", "r") as ordersfile:
        orders_list = []
        for name in ordersfile:
            orders_list.append(name.rstrip())
        
        return orders_list 

def export_prod_list():
    try:
        with open("product.txt", "w") as prod_list_update:
            for prod in prod_list:
                prod_list_update.write(prod + "\n")
    except:
        print("Failed to open file")
        
def export_cour_list():
    try:
        with open("courier.txt", "w") as cour_list_update:
            for cour in cour_list:
                cour_list_update.write(cour + "\n")
    except:
        print("Failed to open file")

def export_orders_list():
    try:
        with open("orders.txt", "w") as orders_list_update:
            for order in orders_list:
                orders_list_update.write(order + "\n")
    except:
        print("Failed to open file")

# Main Program-----------------------------------

print(prog_welcome)

prod_list = load_prod_list()
cour_list = load_cour_list()
orders_list = load_orders_list()
status_list = ["Preparing", "Awaiting Shipment", "Shipped", "Refunded"]

while True: #Main Menu Loop
    
    print(main_menu)
    
    try: # Handle invalid input
        mm_input = int(input("Enter your action: "))
        if mm_input > 4:
            raise Exception
    except Exception:
        print("\nERROR: Please enter an valid action")
        continue
    
    # Main menu input = 0 : Exit main menu 
    if mm_input == 0:
        export_prod_list()
        export_cour_list()
        break
    
    #Main menu input = 1 : Enter Product Menu
    if mm_input == 1:
        while True: #Product Menu Loop
            print(prod_menu)
            
            try: # Handle invalid input
                pm_input = int(input("Enter your action: "))
                if pm_input>4:
                    raise Exception
            except Exception:
                print("\nERROR: Please enter an valid action")
                continue
            
            if pm_input == 0:
                break
            if pm_input == 1:
                print(prod_list)
            if pm_input == 2:
                create_new_item(prod_list, "product")
            if pm_input == 3:
                update_existing_item(prod_list, "product")
            if pm_input == 4:
                delect_item(prod_list, "product")
    
    # Main menu input = 2 : Enter Courier Menu            
    if mm_input == 2:
        while True: #Courier Menu Loop
            print(cour_menu)
            
            try: # Handle invalid input
                cm_input = int(input("Enter your action: "))
                if cm_input>4:
                    raise Exception
            except Exception:
                print("\nERROR: Please enter an valid action")
                continue
            
            if cm_input == 0:
                break
            if cm_input == 1:
                print(cour_list)
            if cm_input == 2:
                create_new_item(cour_list, "courier")
            if cm_input == 3:
                update_existing_item(cour_list, "courier")
            if cm_input == 4:
                delect_item(cour_list, "courier")
                
    if mm_input == 3:
        while True:
            print(order_menu)
            
            try: # Handle invalid input
                om_input = int(input("Enter your action: "))
                if om_input>4:
                    raise Exception
            except Exception:
                print("\nERROR: Please enter an valid action")
                continue
            
            if om_input == 0:
                break
            if om_input == 1:
                print(orders_list)
            if om_input == 2:
                create_new_order()
            if om_input == 3:
                update_order_status()
            if om_input == 4:
                update_existing_order()
            if om_input == 5:
                delect_item(orders_list, "order")


# ELSE IF user input is 5:
# # STRETCH GOAL - DELETE courier
# PRINT orders list
# GET user input for order index value
# DELETE order at index in order list
# """

# Extra 
    if mm_input == 4:
        export_prod_list()
        print("Your file has been exported.")
        prod_list = load_prod_list()
        
    if mm_input == 5:
        export_cour_list()
        print("Your file has been exported.")
        cour_list = load_cour_list()

print("Thanks for using the program, See Ya!")