#Global Variables
# prod_list = []

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
1. Access product menu option
2. Access courier menu option
3. Export product list to .txt
4. Export courier list to .txt
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

def create_new_product():
    """
    Add a new product to the product/courier list
    """
    item = input(f"Enter the product name: ")
    prod_list.append(item)
    print(prod_list)
        
def create_new_courier():
    """
    Add a new product to the product/courier list
    """
    item = input(f"Enter the courier name: ")
    cour_list.append(item)
    print(cour_list)

def print_index(name):
    for index, item in enumerate(name):
        print(index, item)

def update_existing_product():
    """
    Update an existing product with new name  
    """
    while True:
        print_index(prod_list)
        try:
            new_prod_index = int(input("Enter the index of the item to be updated: "))
            if new_prod_index > (len(prod_list)-1):
                raise Exception
        except ValueError:
            print("\nERROR: Please enter an integer!\n")
            continue
        except IndexError:
            print("\nERROR: Please enter an valid index!\n")
            continue
        
        new_prod_name = input("Enter the name of the new product: ")
        prod_list[new_prod_index] = new_prod_name
        print(prod_list)
        return
    
def update_existing_courier():
    """
    Update an existing courier with new name  
    """
    while True:
        print_index(cour_list)
        try:
            new_cour_index = int(input("Enter the index of the item to be updated: "))
            if new_cour_index > (len(cour_list)-1):
                raise IndexError
        except ValueError:
            print("\nERROR: Please enter an integer!\n")
            continue
        except IndexError:
            print("\nERROR: Please enter an valid index!\n")
            continue
        
        new_cour_name = input("Enter the name of the new product: ")
        cour_list[new_cour_index] = new_cour_name
        print(cour_list)
        return

def delect_product():
    """
    Delete an existing product from the list
    """
    print_index(prod_list)
    while True:
        try: 
            prod_index = int(input("Enter the index of the item to be deleted: "))
        except ValueError:
            print("\nERROR: Please enter an integer!")
            continue
        except IndexError:
            print("\nERROR: Please enter an valid index!")
            continue
        prod_list.pop(prod_index)
        print(prod_list)
        return
    
def delect_courier():
    """
    Delete an existing courier from the list
    """
    print_index(cour_list)
    while True:
        try: 
            cour_index = int(input("Enter the index of the item to be deleted: "))
        except ValueError:
            print("\nERROR: Please enter an integer!")
            continue
        except IndexError:
            print("\nERROR: Please enter an valid index!")
            continue
        cour_list.pop(cour_index)
        print(cour_list)
        return

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


# Main Program

print(prog_welcome)
prod_list = load_prod_list()
cour_list = load_cour_list()

while True: #Main Menu Loop
    
    print(main_menu)
    
    try: # Handle invalid input
        mm_input = int(input("Enter your action: "))
        if mm_input > 4:
            raise Exception
    except ValueError:
        print("\nERROR: Please enter an integer!")
        continue
    except Exception:
        print("\nERROR: Please enter an valid action")
        continue
    
    if mm_input == 0:# Exit main menu 
        break
    
    if mm_input == 1:
        while True: #Product Menu Loop
            print(prod_menu)
            
            try: # Handle invalid input
                pm_input = int(input("Enter your action: "))
                if pm_input>4:
                    raise Exception
            except ValueError:
                print("\nERROR: Please enter an integer!")
                continue
            except Exception:
                print("\nERROR: Please enter an valid action")
                continue
            
            if pm_input == 0:
                break
            if pm_input == 1:
                print(prod_list)
            if pm_input == 2:
                create_new_product()
            if pm_input == 3:
                update_existing_product()
            if pm_input == 4:
                delect_product()
                
    if mm_input == 2:
        while True: #Courier Menu Loop
            print(cour_menu)
            
            try: # Handle invalid input
                cm_input = int(input("Enter your action: "))
                if cm_input>4:
                    raise Exception
            except ValueError:
                print("\nERROR: Please enter an integer!")
                continue
            except Exception:
                print("\nERROR: Please enter an valid action")
                continue
            
            if cm_input == 0:
                break
            if cm_input == 1:
                print(cour_list)
            if cm_input == 2:
                create_new_courier()
            if cm_input == 3:
                update_existing_courier()
            if cm_input == 4:
                delect_courier()

    if mm_input == 3:
        export_prod_list()
        print("Your file has been exported.")
        prod_list = load_prod_list()
        
    if mm_input == 4:
        export_cour_list()
        print("Your file has been exported.")
        cour_list = load_cour_list()

print("Thanks for using the program, See Ya!")