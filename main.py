from classes import Common_Function, Product, Courier, Orders

class Menu:
        
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def display_menu(self):
        print(self.menu)
    
    def return_to_main(self):
        Main_Menu().run() #need .run() instead of .run
        
class Main_Menu(Menu):
    
    def __init__(self):
        self.menu = """
------MAIN MENU------
0. Exit the app
1. Enter product menu
2. Enter courier menu
3. Enter order menu
"""
    
        self.choices = {
        "0" : self.quit,
        "1" : Product_Menu().run,
        "2" : Courier_Menu().run,
        "3" : Orders_Menu().run
    }

    def quit(self):
        print("Thanks for using this program")
        exit()

class Product_Menu(Menu):
    
    def __init__(self):
        
        self.menu = """
------PRODUCT MENU------
0. Return to main menu
1. Print product list
2. Create new product
3. Update existing product
4. Delete product
"""
        product = Product()
        self.choices = {
        "0" : self.return_to_main,
        "1" : product.print_product,
        "2" : product.create_new_product,
        "3" : product.update_existing_product,
        "4" : product.delete_product
        }

class Courier_Menu(Menu):
    
    def __init__(self):
        self.menu = """
------COURIER MENU------
0. Return to main menu
1. Print courier list
2. Create new courier
3. Update existing courier
4. Delete courier 
"""
        courier = Courier()
        self.choices = {
        "0" : self.return_to_main,
        "1" : courier.print_courier,
        "2" : courier.create_new_courier,
        "3" : courier.update_existing_courier,
        "4" : courier.delete_courier
        }

class Orders_Menu(Menu):
    
    def __init__(self):
        self.menu = """
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
        order = Orders()
        self.choices = {
        "0" : self.return_to_main,
        "1" : order.print_order,
        "2" : order.create_new_order,
        "3" : order.update_order_status,
        "4" : order.update_existing_orders,
        "5" : order.delete_orders,
    }

def main():
    Main_Menu().run()

if __name__ == "__main__":
    main()