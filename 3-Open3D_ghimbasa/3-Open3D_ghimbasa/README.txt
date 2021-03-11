Version of python used 3.6.8

Data Processing file -
 - This is used when wanting to acquire distance measurements. Keil project must be loaded onto microntroller
 - This program MUST be running when activating the button press in order for distance measurements to be 
   recorded and converted into coordinates 
 - Coordinates will be written into a .txt file

Plotting 3D file -
 - This is used when wanting to visualize the points measured ONLY after the pointCoordinates.txt file is available
 - Once the pointCoordinates.txt file is created with all of the coordinates, running this program will 
   create the xyzCoordinates.xyz file and use that to visualize the measured points.

Setting up the process into 2 python files allowed for measurement and visualization to be done independently and
not require a fresh set of measurements between visualization attempts. 

The included files are ones from a measurement of a small cardboard box in the shape of a parallelogram.