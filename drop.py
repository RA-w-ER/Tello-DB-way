import mysql.connector
from mysql.connector import Error
mysql_config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'proba',
        'port': '3306',
        'ssl_disabled': True
    }

try:
    cnx = mysql.connector.connect(**mysql_config)
    if cnx.is_connected():
        print('connected to database')
        drop = "DROP TABLE for_drop"

        with cnx.cursor() as cursor:
            cursor.execute(drop)
            cnx.commit()

except Error as e:
    print("mysql DB connection error")
    print(e)
