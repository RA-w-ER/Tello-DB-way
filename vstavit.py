import mysql.connector
from mysql.connector import Error
import random
mysql_config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'proba',
        'port': '3306',
        'ssl_disabled': True
    }
x=random.randint(1, 1000)
y=random.randint(1, 1000)
z=random.randint(1, 1000)
try:
    cnx = mysql.connector.connect(**mysql_config)
    if cnx.is_connected():
        print('connected to database')
        ctrlv = f"""
        INSERT INTO coord (x, y, z)
        VALUES
        ({x}, {y}, {z})
        """

        with cnx.cursor() as cursor:
            cursor.execute(ctrlv)
            cnx.commit()

except Error as e:
    print("mysql DB connection error")
    print(e)
