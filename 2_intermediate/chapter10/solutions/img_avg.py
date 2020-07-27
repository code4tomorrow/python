""" Here is the challenge problem for 2d loops>
Images are often represented as 3d arrays,
where the rows and columns are the pixels in the image,
and each pixel has an r, g, and b value.

The interesting thing is that we can iterate over images.
The challenge is, given an image, create a program that
will return a different image where each pixel is the average
of the pixels surrounding it in the original image.

The neighbors of an image are all the pixels that surroun it,
1 on each side, and 4 on the diagonals, for 8 in total. 
Each pixel doesn't necessarily have 8 neighbors, though (think about why)

The code to grab an image from the internet and make it
into an array is given to you. The code also displays the new image
you create in the end.

NOTE: The image is 3 dimensional because each pixel has rgb values.
To find the average value of all of a pixels neighbors, you must
change the average of the red value to the red value, blue to blue, etc.
For example, if the neighbors of a pixel with value [1,2,3]
were [20,30,40] and [10,120,30], the new pixel that would replace the original one would be
[15,75,35]
"""

from PIL import Image
import requests
import numpy
import matplotlib.pyplot as plt

url = "https://images.dog.ceo/breeds/waterdog-spanish/20180723_185544.jpg"
img = numpy.array(Image.open(requests.get(url, stream=True).raw))
newimg = img
transpose = numpy.transpose(img)


#write code to create newimg here
def solution1():
	"""Iterating over the image here. i is a variable from 0 to the width of the image.
	j is a variable that ranges from 0 to the height of the image. i is associated with
	values"""
	for i in range(len(img)):
		for j in range(len(img[0])):
			x_n = [0]
			y_n = [0]

			if(i == 0):
				x_n.append(1)
			elif(i ==  len(img)-1):
				x_n.append(-1)
			else:
				x_n.append(1)
				x_n.append(-1)

			if(j == 0):
				y_n.append(1)
			elif(j ==  len(img[0])-1):
				y_n.append(-1)
			else:
				y_n.append(1)
				y_n.append(-1)

			r_avg = -1*img[i][j][0]
			g_avg = -1*img[i][j][1]
			b_avg = -1*img[i][j][2]
			c = -1

			for x in x_n:
				for y in y_n:
					r_avg += img[i+x][j+y][0]
					g_avg += img[i+x][j+y][1]
					b_avg += img[i+x][j+y][2]
					c+=1
			r_avg = r_avg/c
			g_avg = g_avg/c
			b_avg = b_avg/c

			newimg[i][j] = [r_avg, g_avg, b_avg]




solution1()

plt.imshow(newimg)
plt.show()

plt.imshow(transpose)
plt.show()