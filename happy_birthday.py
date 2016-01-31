from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


img1 = Image.open('images/image1.jpg')
img2 = Image.open('images/image2.jpg')
randxList = list()
randyList = list()
img1xList = list()
img1yList = list()
img2xList = list()
img2yList = list()
width, height = img1.size

print width

for i in range(width):
	for j in range(height):
		currentPixel1 = img1.getpixel((i,j))
		currentPixel2 = img2.getpixel((i,j))
		randxList.append(random.uniform(0,200))
		#print randxList[len(randxList) - 1]
		randyList.append(height - random.uniform(0,200))
		if currentPixel1[0] != 255 :
			img1xList.append(i)
			img1yList.append(height - j)
		if currentPixel2[0] != 255 :
			img2xList.append(i)
			img2yList.append(height - j)

A = [img1xList, img1yList]

fig = plt.figure()
fig.suptitle('Dear Dad')
plt.xlabel('Happiness')
plt.ylabel('Birthdayness')
line, = plt.plot(A[0], A[1], "x", color = "blue")

def update():
	rate = 400.0
	for i in range(500):
		for j in range(len(A[0])):
			if j < len(img2xList):
				A[0][j] = (1 - i/rate)*img1xList[j] + (i/rate)*img2xList[j]
				A[1][j] = (1 - i/rate)*img1yList[j] + (i/rate)*img2yList[j]

		yield A

def draw(data):
    line.set_xdata(data[0])
    line.set_ydata(data[1])
    return line,

ani = animation.FuncAnimation(fig, draw, update, interval=10, blit=False)
plt.show()

