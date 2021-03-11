# Alex Ghimbasan
# COMPENG 2DX4 - Final Project
# 400203560
# ghimbasa
# Python version 3.6.8
# Program Description: This program takes coordinates from a txt file and
# then write them into an xyz file. This file is then processed by open3d
# and is vizualized. Note, this current setup is for drawing up 2 slices
# more slices would be added by changing the limit on the two for loops.
# For loop 1 input would directly be the amount of slices
# For loop 2 input would be the amount of slices - 1

import numpy as np
import open3d as o3d

# Reading coordinates from txt file
f=open('pointCoordinates.txt','r')
coordinates = f.read()
f.close()

# Writing these coordinates to an xyz file
f=open('xyzCoordinates.xyz','w')
f.write(coordinates)
f.close()

# Creating point cloud from xyz file
pcd=o3d.io.read_point_cloud('xyzCoordinates.xyz',format='xyz')
print(pcd)
print(np.asarray(pcd.points))

# Uncomment the line below to see the points being plotted
#o3d.visualization.draw_geometries([pcd])

# Only drawing 32 lines (1 for every 16 points, 512 lines would be too many)

# Plane Creation
pt1 = 0
pt2 = 16
pt3 = 32
pt4 = 48
pt5 = 64
pt6 = 80
pt7 = 96
pt8 = 112
pt9 = 128
pt10 = 144
pt11 = 160
pt12 = 176
pt13 = 192
pt14 = 208
pt15 = 224
pt16 = 240
pt17 = 256
pt18 = 272
pt19 = 288
pt20 = 304
pt21 = 320
pt22 = 336
pt23 = 352
pt24 = 368
pt25 = 384
pt26 = 400
pt27 = 416
pt28 = 432
pt29 = 448
pt30 = 464
pt31 = 480
pt32 = 496
po = 0

lines = []
# create planes
for x in range(2):
    lines.append([pt1+po,pt2+po])
    lines.append([pt2+po,pt3+po])
    lines.append([pt3+po,pt4+po])
    lines.append([pt4+po,pt5+po])
    lines.append([pt5+po,pt6+po])
    lines.append([pt6+po,pt7+po])
    lines.append([pt7+po,pt8+po])
    lines.append([pt8+po,pt9+po])
    lines.append([pt9+po,pt10+po])
    lines.append([pt10+po,pt11+po])
    lines.append([pt11+po,pt12+po])
    lines.append([pt12+po,pt13+po])
    lines.append([pt13+po,pt14+po])
    lines.append([pt14+po,pt15+po])
    lines.append([pt15+po,pt16+po])
    lines.append([pt16+po,pt17+po])
    lines.append([pt17+po,pt18+po])
    lines.append([pt18+po,pt19+po])
    lines.append([pt19+po,pt20+po])
    lines.append([pt20+po,pt21+po])
    lines.append([pt21+po,pt22+po])
    lines.append([pt22+po,pt23+po])
    lines.append([pt23+po,pt24+po])
    lines.append([pt24+po,pt25+po])
    lines.append([pt25+po,pt26+po])
    lines.append([pt26+po,pt27+po])
    lines.append([pt27+po,pt28+po])
    lines.append([pt28+po,pt29+po])
    lines.append([pt29+po,pt30+po])
    lines.append([pt30+po,pt31+po])
    lines.append([pt31+po,pt32+po])
    lines.append([pt32+po,pt1+po])
    po += 512;

#reset var
# Line Connection
pt1 = 0
pt2 = 16
pt3 = 32
pt4 = 48
pt5 = 64
pt6 = 80
pt7 = 96
pt8 = 112
pt9 = 128
pt10 = 144
pt11 = 160
pt12 = 176
pt13 = 192
pt14 = 208
pt15 = 224
pt16 = 240
pt17 = 256
pt18 = 272
pt19 = 288
pt20 = 304
pt21 = 320
pt22 = 336
pt23 = 352
pt24 = 368
pt25 = 384
pt26 = 400
pt27 = 416
pt28 = 432
pt29 = 448
pt30 = 464
pt31 = 480
pt32 = 496
po = 0
do = 512
# connect lines

for x in range(1):
    lines.append([pt1+po,pt2+do+po])
    lines.append([pt2+po,pt3+do+po])
    lines.append([pt3+po,pt4+do+po])
    lines.append([pt4+po,pt5+do+po])
    lines.append([pt5+po,pt6+do+po])
    lines.append([pt6+po,pt7+do+po])
    lines.append([pt7+po,pt8+do+po])
    lines.append([pt8+po,pt9+do+po])
    lines.append([pt9+po,pt10+do+po])
    lines.append([pt10+po,pt11+do+po])
    lines.append([pt11+po,pt12+do+po])
    lines.append([pt12+po,pt13+do+po])
    lines.append([pt13+po,pt14+do+po])
    lines.append([pt14+po,pt15+do+po])
    lines.append([pt15+po,pt16+do+po])
    lines.append([pt16+po,pt17+do+po])
    lines.append([pt17+po,pt18+do+po])
    lines.append([pt18+po,pt19+do+po])
    lines.append([pt19+po,pt20+do+po])
    lines.append([pt20+po,pt21+do+po])
    lines.append([pt21+po,pt22+do+po])
    lines.append([pt22+po,pt23+do+po])
    lines.append([pt23+po,pt24+do+po])
    lines.append([pt24+po,pt25+do+po])
    lines.append([pt25+po,pt26+do+po])
    lines.append([pt26+po,pt27+do+po])
    lines.append([pt27+po,pt28+do+po])
    lines.append([pt28+po,pt29+do+po])
    lines.append([pt29+po,pt30+do+po])
    lines.append([pt30+po,pt31+do+po])
    lines.append([pt31+po,pt32+do+po])
    lines.append([pt32+po,pt1+do+po])
    po += 512;


line_set = o3d.geometry.LineSet(points = o3d.utility.Vector3dVector(np.asarray(pcd.points)), lines = o3d.utility.Vector2iVector(lines),)

#Show results
o3d.visualization.draw_geometries([line_set])
