import os
import pymysql
from dotenv import load_dotenv

class Common_Function():
    
    @staticmethod
    def print_item(table_name):
        """Print out content from Database"""
        sql = f"SELECT * FROM {table_name}"
        lists = Database().execute_query(sql)
        for element in lists:
            print("")
            for key,values in element.items():
                print(f"{key}: {values}")
        print("")
        
    @staticmethod
    def print_dict(name):
        for key, value in name.items(): 
            print(f"{key} {value}")
        print("")
        
class Product(Common_Function):
    
    def __init__(self):
        self.table_name = "product"
    
    def print_product(self):
        self.print_item(self.table_name)
    
    def create_new_product(self):
        name = input(f"Enter the product name: ")
        price = input(f"Enter the price: ")
        sql = "INSERT IGNORE INTO product (name, price) VALUES (%s,%s)"
        val = (name, price)
        Database().execute_query(sql, val)
        
    def update_existing_product(self):
        self.print_item(self.table_name)
        id_input = int(input("Enter the product's ID: "))
        name = str(input("Enter the new product name: "))
        if name:
            sql = "UPDATE product SET name = %s WHERE id = %s"
            val = (name, id_input)
            Database().execute_query(sql, val)
        try:
            price = float(input("Enter the new price: "))
            sql = "UPDATE product SET price = %s WHERE id = %s"
            val = (price, id_input)
            Database().execute_query(sql, val)
        except ValueError:
            pass
    
    def delete_product(self):
        self.print_item(self.table_name)
        id_input = int(input("Enter the ID of product to be deleted: "))
        sql = "DELETE FROM product WHERE id = %s"
        val = id_input
        Database().execute_query(sql, val)
    
class Courier(Common_Function):

    def __init__(self):
        self.table_name = "courier"
    
    def print_courier(self):
        self.print_item(self.table_name)
    
    def create_new_courier(self):
        name = input(f"Enter the courier name: ")
        phone = input(f"Enter the phone: ")
        sql = "INSERT IGNORE INTO courier (name, phone) VALUES (%s,%s)"
        val = (name, phone)
        Database().execute_query(sql, val)
        
    def update_existing_courier(self):
        self.print_item(self.table_name)
        id_input = int(input("Enter the courier's ID: "))
        name = str(input("Enter the new courier name: "))
        if name:
            sql = "UPDATE courier SET name = %s WHERE id = %s"
            val = (name, id_input)
            Database().execute_query(sql, val)
        
        phone = str(input("Enter the new phone number: "))
        if phone:
            sql = "UPDATE courier SET phone = %s WHERE id = %s"
            val = (phone, id_input)
            Database().execute_query(sql, val)
            
    def delete_courier(self):
        self.print_item(self.table_name)
        id_input = int(input("Enter the ID of courier to be deleted: "))
        sql = "DELETE FROM courier WHERE id = %s"
        val = id_input
        Database().execute_query(sql, val)


class Orders(Common_Function):
    
    def __init__(self):
        self.table_name = "orders"
        self.orders_status = {"0":"Preparing", "1":"Waiting for Pickup", "2":"Delivered"}
    
    def print_order(self):
        self.print_item(self.table_name)
    
    def create_new_order(self):
        customer_name = str(input("Input for customer name: "))
        customer_address = str(input("Input for customer address: "))
        customer_phone = str(input("Input for customer phone number: "))
        
        self.table_name = "courier"
        self.print_item("courier")
        courier_id = int(input("Input the courier index to select courier: "))
        status = "Preparing"
        
        self.table_name = "product"
        self.print_item("product")
        product_str = str(input("Enter list of product index values (seperated with comma): "))
        self.table_name = "orders"
        product_str_list = product_str.split(",")
        for product in product_str_list:
            sql = ("INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, delivery_status, items) VALUES (%s,%s,%s,%s,%s,%s)")
            val = (customer_name, customer_address, customer_phone, courier_id, status, product)
            Database().execute_query(sql, val)
            
    def update_order_status(self):
        
        self.print_item(self.table_name)
        input_id = int(input("Which order your want to update?: ")) 
        self.print_dict(self.orders_status)
        input_status = input("What is the new orders status?: ")
        new_status = self.orders_status[input_status]
        sql = ("UPDATE orders SET delivery_status = %s WHERE customer_id = %s")
        val = (new_status, input_id)
        Database().execute_query(sql, val)
        
    def update_existing_orders(self):
        self.print_item(self.table_name)
        input_id = int(input("Which order your want to update?: "))
        customer_name = str(input("Input for customer name: "))
        if customer_name:
            Database().execute_query("UPDATE orders SET customer_name=%s WHERE customer_id = %s", (customer_name, input_id))
            
        customer_address = str(input("Input for customer address: "))
        if customer_address:
            Database().execute_query("UPDATE orders SET customer_address=%s WHERE customer_id = %s", (customer_address, input_id))
            
        customer_phone = str(input("Input for customer phone number: "))
        if customer_phone:
            Database().execute_query("UPDATE orders SET customer_phone=%s WHERE customer_id = %s", (customer_phone, input_id))
        
        self.print_item("courier")
        courier_id = str(input("Input the courier index to select courier: "))
        if courier_id:
            Database().execute_query("UPDATE orders SET courier_id=%s WHERE customer_id = %s", (courier_id, input_id))
        
        self.print_dict(self.orders_status)
        input_status = str(input("Input the index to select status: "))
        if input_status:
            status = self.orders_status[input_status]
            Database().execute_query("UPDATE orders SET delivery_status=%s WHERE customer_id = %s", (status, input_id))           
            
        self.print_item("product")
        item_str = str(input("Enter list of product index values: "))
        while item_str:
            if "," in item_str:
                print("Please enter ONE product\n")
                item_str = str(input("Enter list of product index values: "))
            else:
                Database().execute_query("UPDATE orders SET items=%s WHERE customer_id = %s", (item_str, input_id))
                break

    def delete_orders(self):
        self.print_item(self.table_name)
        input_id = int(input("Enter the customer id to delete orders: "))
        sql = ("DELETE FROM orders WHERE customer_id = %s")
        val = (input_id)
        Database().execute_query(sql, val)
    
class Database():
    
    def __init__(self):
    # Load environment variables from .env file
        load_dotenv()
        self.host = os.environ.get("mysql_host")
        self.user = os.environ.get("mysql_user")
        self.password = os.environ.get("mysql_pass")
        self.database = os.environ.get("mysql_db")
    
    # Establish a database connection
    def execute_query(self, statement, val=None):
        try:
            connection = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database, autocommit=True)
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(statement, val)
            rows = cursor.fetchall()
            connection.commit()
            cursor.close()
            connection.close()
            return rows
        except Exception as e:
            print(e)