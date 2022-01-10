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
    connection = pymysql.connect(host=host,user=user,password=password,database=database, autocommit=True)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(statement, val)
    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return rows

