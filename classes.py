from file_handler import execute_query

class Item():
    
    @staticmethod
    def print_index(name):
        """Print item in list with index"""
        for index, item in enumerate(name):
            print(index, item)
    
    @staticmethod    
    def print_item(table_name):
        """Print out content from Database"""
        sql = f"SELECT * FROM {table_name}"
        lists = execute_query(sql)
        for element in lists:
            print("")
            for key,values in element.items():
                print(f"{key}: {values}")
        print("")
        return lists
    
    @staticmethod
    def print_with_sequence(table_name, column):
        sql = f"SELECT * FROM {table_name} ORDER BY {column} DESC"
        lists = execute_query(sql)
        for element in lists:
            print("")
            for key,values in element.items():
                print(f"{key}: {values}")

class Product(Item):
    
    table_name = "product"
    
    @staticmethod
    def create_new_product():
        name = input(f"Enter the product name: ")
        price = input(f"Enter the price: ")
        sql = "INSERT IGNORE INTO product (name, price) VALUES (%s,%s)"
        val = (name, price)
        execute_query(sql, val)
    
    def update_existing_product(self):
        super().print_item(self.table_name)
        id_input = int(input("Enter the product's ID: "))
        name = str(input("Enter the new product name: "))
        if name:
            sql = "UPDATE product SET name = %s WHERE id = %s"
            val = (name, id_input)
            execute_query(sql, val)
        try:
            price = float(input("Enter the new price: "))
            sql = "UPDATE product SET price = %s WHERE id = %s"
            val = (price, id_input)
            execute_query(sql, val)
        except ValueError:
            pass
            
    
    def delete_product(self):
        super().print_item(self.table_name)
        id_input = int(input("Enter the ID of product to be deleted: "))
        sql = "DELETE FROM product WHERE id = %s"
        val = id_input
        execute_query(sql, val)

class Courier(Item):
    
    table_name = "courier"
    
    @staticmethod
    def create_new_courier():
        name = input(f"Enter the courier name: ")
        phone = input(f"Enter the phone: ")
        sql = "INSERT IGNORE INTO courier (name, phone) VALUES (%s,%s)"
        val = (name, phone)
        execute_query(sql, val)
    
    def update_existing_courier(self):
        super().print_item(self.table_name)
        id_input = int(input("Enter the courier's ID: "))
        name = str(input("Enter the new courier name: "))
        if name:
            sql = "UPDATE courier SET name = %s WHERE id = %s"
            val = (name, id_input)
            execute_query(sql, val)
        
        phone = str(input("Enter the new phone number: "))
        if phone:
            sql = "UPDATE courier SET phone = %s WHERE id = %s"
            val = (phone, id_input)
            execute_query(sql, val)
    
    def delete_courier(self):
        super().print_item(self.table_name)
        id_input = int(input("Enter the ID of courier to be deleted: "))
        sql = "DELETE FROM courier WHERE id = %s"
        val = id_input
        execute_query(sql, val)

class Order(Item):
    
    table_name = "orders"
    orders_status = {"0":"Preparing", "1":"Waiting for Pickup", "2":"Delivered"}
    
    def create_new_order(self):
        customer_name = str(input("Input for customer name: "))
        customer_address = str(input("Input for customer address: "))
        customer_phone = str(input("Input for customer phone number: "))
        
        super().print_item(Courier.table_name)
        courier_id = int(input("Input the courier index to select courier: "))
        status = "Preparing"
        
        super().print_item(Product.table_name)
        product_str = str(input("Enter list of product index values (seperated with comma): "))
        product_str_list = product_str.split(",")
        for product in product_str_list:
            sql = ("INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, delivery_status, items) VALUES (%s,%s,%s,%s,%s,%s)")
            val = (customer_name, customer_address, customer_phone, courier_id, status, product)
            execute_query(sql, val)
    
    def update_order_status(self):
        
        super().print_item(self.table_name)
        input_id = int(input("Which order your want to update?: ")) 
        self.print_dict(self.orders_status)
        input_status = input("What is the new orders status?: ")
        new_status = self.orders_status[input_status]
        sql = ("UPDATE orders SET delivery_status = %s WHERE customer_id = %s")
        val = (new_status, input_id)
        execute_query(sql, val)
    
    def update_existing_orders(self):
        # orders_status = {0:"Preparing", 1:"Waiting for Pickup", 2:"Delivered"}
        super().print_item(self.table_name)
        input_id = int(input("Which order your want to update?: "))
        customer_name = str(input("Input for customer name: "))
        if customer_name:
            execute_query("UPDATE orders SET customer_name=%s WHERE customer_id = %s", (customer_name, input_id))
            
        customer_address = str(input("Input for customer address: "))
        if customer_address:
            execute_query("UPDATE orders SET customer_address=%s WHERE customer_id = %s", (customer_address, input_id))
            
        customer_phone = str(input("Input for customer phone number: "))
        if customer_phone:
            execute_query("UPDATE orders SET customer_phone=%s WHERE customer_id = %s", (customer_phone, input_id))
            
        super().print_item(Courier.table_name)
        courier_id = str(input("Input the courier index to select courier: "))
        if courier_id:
            execute_query("UPDATE orders SET courier_id=%s WHERE customer_id = %s", (courier_id, input_id))
        
        self.print_dict(self.orders_status)
        input_status = str(input("Input the courier index to select status: "))
        if input_status:
            status = self.orders_status[input_status]
            execute_query("UPDATE orders SET delivery_status=%s WHERE customer_id = %s", (status, input_id))           
        
        super().print_item(Product.table_name)
        item_str = str(input("Enter list of product index values: "))
        while item_str:
            if "," in item_str:
                print("Please enter ONE product\n")
                item_str = str(input("Enter list of product index values: "))
            else:
                execute_query("UPDATE orders SET items=%s WHERE customer_id = %s", (item_str, input_id))
                break
    
    def delete_orders(self):
        super().print_item(self.table_name)
        input_id = int(input("Enter the customer id to delete orders: "))
        sql = ("DELETE FROM orders WHERE customer_id = %s")
        val = (input_id)
        execute_query(sql, val)
    
    @staticmethod
    def print_dict(name):
        for key, value in name.items(): 
            print(f"{key} {value}")
        print("")

class Error_handling():
    
    @staticmethod
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