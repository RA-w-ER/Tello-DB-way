import random
from time import daylight

import mysql.connector
from mysql.connector import Error
import random
from djitellopy import Tello
import time
import datetime
datime=datetime.datetime.now()
year=str(datime.year)
month=str(datime.month)
day=str(datime.day)
hour=str(datime.hour)
minute=str(datime.minute)
print(year, month, day, hour, minute)

