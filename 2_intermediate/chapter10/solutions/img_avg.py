"""
Image Average

Here is the challenge problem for nested loops:
Images are often represented as 3D lists.
The outer list is the entire image.
The 1st level inner list is a row of pixels.
The 2nd level inner list is the RGB values for that pixel.
RGB (red, green, blue) values determine the color of the pixel.

The interesting thing is that we can iterate over images.
The challenge is: given an image, create a program that
will return a different image where each pixel is the average
of the pixels surrounding it in the original image.

To find the average value of all of a pixels neighbors, you must
calculate the average of the red values, blue values, and green values.
For example, if the neighbors of a pixel with value [1, 2, 3]
were [20, 30, 40] and [10, 120, 30], the new pixel that would replace the
original one would be [15, 75, 35] (since the average of 20 and 10 is 15,
the average of 30 and 120 is 75, and the average of 40 and 30 is 35).

EXAMPLE: An image with 9 pixels may look like:
[
    [
        [31, 41, 42], [51, 1, 101], [24, 141, 33]
    ],

    [
        [50, 21, 28], [31, 49, 201], [90, 54, 33]
    ],

    [
        [12, 81, 3], [22, 8, 91], [101, 141, 132]
    ]
]

HINT: Don't forget that a pixel may have varying amount of neighboring
pixels. A pixel at the edge, for example, has 3 neighboring pixels while
a pixel at the center of the image has 8 neighboring pixels (one on each
of its 4 sides, and then one at each of its 4 corners).

GIVEN: The code to grab an image from the internet and make it
into an array is given to you. The code also displays the new image
you create in the end. These weren't taught in the main curriculum, so
it isn't expected for students to fully understand what the given code
does.
"""

# Import libraries needed to run the program
# Before importing the libraries, you must have them installed.
# Follow the following instructions to get all the libraries installed:
# -1. We first have to make sure pip is there. To check, run pip --version
#     in the terminal. If a version appeared, then pip is there. If no
#     version appears, update your Python to the latest version of 2 or 3.
# -2. In terminal, run pip install pillow. Wait for Successfully installed
#     (something) to pop on the terminal.
# -3. In terminal, run pip install requests. Wait for Successfully installed
#     (something) to pop on the terminal.
# -4. In terminal, run pip install numpy. Wait for Successfully installed
#     (something) to pop on the terminal.
# -5. In terminal, run pip install matplotlib. Wait for Successfully
#     installed (something) to pop on the terminal.
# -6. If all 2-5 all were successful, now you all the packages needed for
#     this problem.

from PIL import Image
import requests
import numpy
import matplotlib.pyplot as plt

# Code that grabs the image from the internet and makes it into an array
IMAGE_URL = (
    "https://images.dog.ceo/breeds/waterdog-spanish/20180723_185544.jpg"
)
img = numpy.array(
    Image.open(requests.get(IMAGE_URL, stream=True).raw)
).tolist()
newimg = img  # the newimg starts as a copy of the original image
transpose = numpy.transpose(img)

# Code that displays the original image
plt.imshow(img)
plt.show()

"""
The double for loop gets all combination of indexes necessary
  to access all the pixels inside the list.
i is the index determining which inner
  list to get. Using the Example as the visual, this
  index goes from top to bottom.
j is the index determining which list inside 
  inner list to get. Using the Example as the visual, this 
  index goes from left to right.
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

        r_avg = -img[i][j][0]
        g_avg = -img[i][j][1]
        b_avg = -img[i][j][2]
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


# Code that displays the new image at the end
plt.imshow(newimg)
plt.show()

plt.imshow(transpose)
plt.show()
