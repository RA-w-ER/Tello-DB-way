import mysql.connector
from mysql.connector import Error
import random
from djitellopy import Tello
import time
import cv2
import asyncio
import datetime
tello = Tello()
tello.connect()
wayid=int(input())
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
        ctrlf = f"SELECT `x`, `y`, `z` FROM `ways` WHERE id={wayid}"

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
tello.takeoff()
for n in result:
    dos_coord = n
    xp=int(dos_coord[0])
    yp=int(dos_coord[1])
    zp=int(dos_coord[2])
    print(xp, yp, zp)
    tello.go_xyz_speed(xp, yp, zp, 100)
    time.sleep(2)
tello.land()