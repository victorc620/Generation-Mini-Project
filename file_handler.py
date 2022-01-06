import csv
import pymysql
import os
from dotenv import load_dotenv

def load_csv_to_list_of_dict(file_name:str):
    # Unit test completed
    """Load from orders.csv to creat a list of order(dict)"""
    list = []
    with open(file_name, "r") as f:
        csv_file = csv.DictReader(f)
        for line in csv_file:
            list.append(line)
        return list
        
def export_list_of_dict_to_csv(filename: str, list_of_dict: list, fieldnames: list):
    """Export orders_list to a csv file"""
    try:
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for line in list_of_dict:
                writer.writerow(line)
    except:
        print("Failed to open file")
        
def load_from_db(statement):
    """
    Load data from database to create a list of dictionaries
    statement: MySQL code
    return: List of dictionaries
    """
    # Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(host,user,password,database, autocommit=True)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    # Execute SQL query
    cursor.execute(statement)
    
    # Gets all rows from the result
    rows = cursor.fetchall()
    list_of_dict = [row for row in rows]
    
    #Close connection with database
    cursor.close()
    connection.close()
        
    return list_of_dict

def insert_into_db(table_name, item_list):
    # Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    mydb = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    mycursor = mydb.cursor()
    
    #insert list_of_dict to db row
    i=0
    for element in item_list:
            sql = f"""
                INSERT IGNORE INTO {table_name} (id, name, price)
                VALUES (%s,%s,%s)"""
            val = ("NULL", f"{element['name']}", f"{element['price']}")
            print(i)
            i+=1
            mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    mydb.close()
    
