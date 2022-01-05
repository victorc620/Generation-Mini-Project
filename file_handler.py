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
        
def load_from_db(table_name):
    """Load data from database to create a list of dictionaries """
    
    list_of_dict = []
    
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
    
    # Return dict
    mycursor = mydb.cursor(pymysql.cursors.DictCursor)
    
    # Execute SQL query
    mycursor.execute(f"SELECT * FROM {table_name}")
    
    # Gets all rows from the result
    rows = mycursor.fetchall()
    for row in rows:
        list_of_dict.append(row)
        
    return list_of_dict