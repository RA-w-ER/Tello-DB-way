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
        create_movies_table_query = """
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            collection_in_mil INT
        )
        """

        with cnx.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            cnx.commit()

except Error as e:
    print("mysql DB connection error")
    print(e)
