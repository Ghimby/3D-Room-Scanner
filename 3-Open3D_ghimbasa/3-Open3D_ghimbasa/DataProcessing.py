# Alex Ghimbasan
# COMPENG 2DX4 - Final Project
# 400203560
# ghimbasa
# Python version 3.6.8
# Program Description: This program gets distance values from the ToF sensor
# and then converts them into coordinates and writes them into a text file

import serial
import math

# Setting COM3 as serial port at 115.2kbps 8N1 (port acquired from serialpy)
s = serial.Serial("COM3", 115200)
print("Using Port: " + s.name)
file = open("pointCoordinates.txt", "w")
# Initializing Variables
xcoord = 0.0
ycoord = 0.0
zcoord = 0.0
rotations = 2 # Change this variable for the number of slices being processed
steppingAngle = (math.pi/180)*(360/512) # Calculated angle based on number of points being taken
angle = 0;
points = (rotations * 512) + 10


# Variable holding the current point being measured
# Starts at -10 due to text being sent to python before the distance values
pointNum = -10

# Looping for a specified amount of point (currently 2 rotations worth)
for i in range(points):
    pointNum = pointNum + 1

    # Printing out the point number
    if (pointNum > 0):
        print("Current Point = " + str(pointNum))
    
    x = s.readline() # Reading one byte
    c = x.decode() # Converting byte type to str
    print(c)

    # Calculating the coordinates based on the distance measurement
    # Also writing these coordinates to a txt file
    if (pointNum > 0):
        distance = float(c)
        angle = angle + steppingAngle
        ycoord = distance * (math.cos(angle))
        zcoord = distance * (math.sin(angle))
        file.write(str(xcoord) + " " + str(ycoord) + " " + str(zcoord) + " \n")
    
    if(pointNum == 512): # Once a full rotation is complete
        xcoord = xcoord + 200 # Moving 20cm forward between slices
        pointNum = 0
        angle = 0

print("Closing: " + s.name)
file.close()
s.close();
