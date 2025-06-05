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
x=random.randint(20, 40)
y=random.randint(20, 40)
z=random.randint(20, 40)
way=int(input())
try:
    cnx = mysql.connector.connect(**mysql_config)
    if cnx.is_connected():
        print('connected to database')
        ctrlv = f"""
        INSERT INTO ways (id, x, y, z)
        VALUES
        ({way}, {x}, {y}, {z})
        """

        with cnx.cursor() as cursor:
            cursor.execute(ctrlv)
            cnx.commit()

except Error as e:
    print("mysql DB connection error")
    print(e)
