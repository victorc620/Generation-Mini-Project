from classes import Error_handling, Item, Product, Courier, Order

def main_menu():
    main_menu = """
------MAIN MENU------

0. Exit the app
1. Enter product menu
2. Enter courier menu
3. Enter order menu
"""
    print(main_menu)        
    action = Error_handling.menu_input(3)
    
    if action == 0:
        print("Thanks for using this program, see ya!\n")
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
        action = Error_handling.menu_input(5)
        product = Product()
        
        if action == 0:
            return
        elif action == 1:
            product.print_item(product.table_name)
        elif action == 2:
            product.create_new_product()
        elif action == 3:
            product.update_existing_product()
        elif action == 4:
            product.delete_product()
            
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
        action = Error_handling.menu_input(4)
        courier = Courier()
        
        if action == 0:
            return
        elif action == 1:
            courier.print_item(courier.table_name)
        elif action == 2:
            courier.create_new_courier()
        elif action == 3:
            courier.update_existing_courier()
        elif action == 4:
            courier.delete_courier()

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
        action = Error_handling.menu_input(7)
        order = Order()
        
        if action == 0:
            return
        elif action == 1:
            order.print_item(order.table_name)
        elif action == 2:
            order.create_new_order()
        elif action == 3:
            order.update_order_status()
        elif action == 4:
            order.update_existing_orders()
        elif action == 5:
            order.delete_orders()
        elif action == 6:
            order.print_with_sequence(order.table_name,"delivery_status")
        elif action == 7:
            order.print_with_sequence(order.table_name,"courier_id")

def main():
    while True: #Main Menu Loop
        main_menu()

if __name__ == "__main__":
    main()