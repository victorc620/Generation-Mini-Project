from main import main_menu


class Menu:
    
    def __init__(self):
        self.menu = ""
        self.choices ={"0":"temp"}
    
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

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
        self.choices = {
        "0": self.return_to_main,
        "1": self.test  
        }
    
    def test(self):
        print("product menu test")


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
        
        self.choices = {
        "0":self.return_to_main,
        "1":self.test
        }
        
    def test(self):
        print("courier menu test")

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

        self.choices = {
        "0" : self.return_to_main,
    }
        
    def test(self):
        print("orders menu test")
    pass

class Product:
    pass

class Courier:
    pass

class Order:
    pass

def main():
    Main_Menu().run()

if __name__ == "__main__":
    main()