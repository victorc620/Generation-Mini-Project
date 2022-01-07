import csv
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
def execute_query(statement, val = None, host=host,user=user,password=password,database=database):
    connection = pymysql.connect(host,user,password,database, autocommit=True)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(statement, val)
    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return rows

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

