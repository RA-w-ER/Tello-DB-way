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
        ctrlf = f"SELECT `x`, `y`, `z` FROM `coord` WHERE 1"

        with cnx.cursor(buffered=True) as cursor:
            cursor.execute(ctrlf)
            cnx.commit()
            result = cursor.fetchall()
            # for row in result:
            #     print(row)
            #     print(type(row))


except Error as e:
    print("mysql DB connection error")
    print(e)
print(result)
dlin_res=len(result)
print(dlin_res)
pos_coord=int(input())
dos_coord=result[pos_coord]

print(dos_coord)
xp=int(dos_coord[0])
yp=int(dos_coord[1])
zp=int(dos_coord[2])
print(xp, yp, zp)

