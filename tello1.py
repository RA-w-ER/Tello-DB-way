import mysql.connector
from mysql.connector import Error
import random
from djitellopy import Tello
import time
import datetime

tello = Tello()
tello.connect()
x=float(tello.get_acceleration_x())
y=float(tello.get_acceleration_y())
z=float(tello.get_acceleration_z())
t=float(tello.get_temperature())
bat=float(tello.get_battery())
datime=datetime.datetime.now()
year=str(datime.year)
month=str(datime.month)
day=str(datime.day)
hour=str(datime.hour)
minute=str(datime.minute)

print(x, y, z, t, bat)

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
        ctrlv = f"""
        INSERT INTO coord (x, y, z, temp, bat, year, month, day, hour, minute)
        VALUES
        ({x}, {y}, {z}, {t}, {bat}, {year}, {month}, {day}, {hour}, {minute})
        """

        with cnx.cursor() as cursor:
            cursor.execute(ctrlv)
            cnx.commit()

except Error as e:
    print("mysql DB connection error")
    print(e)
tello.takeoff()
tello.move_left(int(50))
tello.rotate_counter_clockwise(int(360))
tello.move_forward(int(50))
tello.land()
x=float(tello.get_acceleration_x())
y=float(tello.get_acceleration_y())
z=float(tello.get_acceleration_z())
t=float(tello.get_temperature())
bat=float(tello.get_battery())
datime=datetime.datetime.now()
year=str(datime.year)
month=str(datime.month)
day=str(datime.day)
hour=str(datime.hour)
minute=str(datime.minute)
print(x, y, z, t, bat)
try:
    cnx = mysql.connector.connect(**mysql_config)
    if cnx.is_connected():
        print('connected to database')
        ctrlv = f"""
        INSERT INTO coord (x, y, z, temp, bat, year, month, day, hour, minute)
        VALUES
        ({x}, {y}, {z}, {t}, {bat}, {year}, {month}, {day}, {hour}, {minute})
        """

        with cnx.cursor() as cursor:
            cursor.execute(ctrlv)
            cnx.commit()

except Error as e:
    print("mysql DB connection error")
    print(e)
