from djitellopy import Tello
import random
x=random.randint(1, 9999999)
print(x)
q=int(input())
w=int(input())
e=int(input())
r=int(100)
tello = Tello()
tello.connect()
tello.takeoff()
tello.go_xyz_speed(q,w,e,r)
tello.land()