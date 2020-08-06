"""
Image Average

Here is the challenge problem for 2D loops:
Images are often represented as 3D arrays,
where the rows and columns are the pixels in the image,
and each pixel has an RGB (red, green, blue) value
which determines the color of the pixel.

The interesting thing is that we can iterate over images.
The challenge is, given an image, create a program that
will return a different image where each pixel is the average
of the pixels surrounding it in the original image.

NOTE: The image is 3 dimensional because each pixel has RGB values.
To find the average value of all of a pixels neighbors, you must
change the average of the red value to the red value, blue to blue, etc.
For example, if the neighbors of a pixel with value [1, 2, 3]
were [20, 30, 40] and [10, 120, 30], the new pixel that would replace the
original one would be [15, 75, 35]

EXAMPLE: A image with,let's say 9 pixels may look like:
[[[31,41,42], [51,1,101], [24,141,33]],
 [[50,21,28], [31,49,201], [90,54,33]],
 [[12,81,3], [22,8,91], [101,141,132]]]

HINT: Don't forget that a pixel may have varying amount of neighboring
pixels. A pixel at the edge, for example, has 3 neighboring pixels while
a pixel at the center of the image has 8 neighboring pixels.

GIVEN: The code to grab an image from the internet and make it
into an array is given to you. The code also displays the new image
you create in the end. These weren't taught in the main curriculum, so 
it isn't expected for students to fully understand what the given code 
does. 
"""

#All the libraries imported 
from PIL import Image
import requests
import numpy
import matplotlib.pyplot as plt

#Code that grabs the image from the internet and makes it into an array
url = "https://images.dog.ceo/breeds/waterdog-spanish/20180723_185544.jpg"
img = numpy.array(Image.open(requests.get(url, stream=True).raw)).tolist()
newimg = img
transpose = numpy.transpose(img)

plt.imshow(img)
plt.show()


#Write code to create newimg here
"""
Iterating over the image here. i is a variable from
0 to the width of the image.
j is a variable that ranges from 0 to the height of the image.
i is associated with values
"""
for i in range(len(img)):
    for j in range(len(img[0])):
        x_n = [0]
        y_n = [0]

        if i == 0:
            x_n.append(1)
        elif i == len(img) - 1:
            x_n.append(-1)
        else:
            x_n.append(1)
            x_n.append(-1)

        if j == 0:
            y_n.append(1)
        elif j == len(img[0]) - 1:
            y_n.append(-1)
        else:
            y_n.append(1)
            y_n.append(-1)

        r_avg = -1 * img[i][j][0]
        g_avg = -1 * img[i][j][1]
        b_avg = -1 * img[i][j][2]
        c = -1

        for x in x_n:
            for y in y_n:
                r_avg += img[i + x][j + y][0]
                g_avg += img[i + x][j + y][1]
                b_avg += img[i + x][j + y][2]
                c += 1
        r_avg = r_avg / c
        g_avg = g_avg / c
        b_avg = b_avg / c

        newimg[i][j] = [r_avg, g_avg, b_avg]
        

#Code that displays the new image at the end.
plt.imshow(newimg)
plt.show()

plt.imshow(transpose)
plt.show()
