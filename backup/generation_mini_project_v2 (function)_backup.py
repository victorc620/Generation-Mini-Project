#Global Variables
prod_list = ["Coke Zero", "Coffee", "Tea"]

main_menu = """
------MAIN MENU------

0. Exit the app
1. Access product menu option
"""

prod_menu = """
------PRODUCT MENU------

0. Return to main menu
1. Print product list
2. Create new product
3. Update existing product
4. Delete product
"""

def create_new_product():
    """
    Add a new product to the product list
    """
    prod_name = input("Enter the product name: ")
    prod_list.append(prod_name)
    print(prod_list)

def update_existing_product():
    """
    Update an existing product with new name
    """
    while True:
        for index, prod in enumerate(prod_list):
            print(index, prod)
        try:
            new_prod_index = int(input("Enter the index of the item to be updated: "))
            if new_prod_index > (len(prod_list)-1):
                raise IndexError
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

def delect_product():
    """
    Delete an existing product from the list
    """
    print(prod_list)
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


# Main Program
while True: #Main Menu Loop
    print(main_menu)
    try:
        mm_input = int(input("Enter your action: "))
        if mm_input > 1:
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
            try:
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

print("Thanks for using the program, See Ya!")
