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
"""

# Import libraries needed to run the program
# Before importing the libraries, you must have them installed.
# This problem requires the following libraries:
# pillow, requests, numpy, and matplotlib
# If you don't already have them installed, open your command prompt or terminal
# and please do
# this: pip install -U (library) (any other libraries, each separated by a space)
# ex: pip install -U numpy matplotlib requests pillow
# Note: on some windows machines, you may need to
# do: py -m pip install -U (library) (any other libraries, each separated by a space)

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

# create newimg as an empty list so that we'll know if something went wrong
# ie. if we try to display it and the function didn't run, we'd get an
# invalid shape error
newimg = [[[] for column in row] for row in img]

# Code that displays the original image
print("now displaying the original image")
plt.imshow(img)
plt.show()

# Write code to create newimg here

# Code that displays the new image at the end
print("now displaying the new image")
plt.imshow(newimg)
plt.show()
