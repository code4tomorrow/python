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


def distort(original_image, new_image):
    """
    Modifies new_image so that each pixel in new_image
    will be the average of the surrounding
    DISTORTION_RADIUS pixels.
    DISTORTION_RADIUS can be changed for more/less distortion.
    Arguments:
        original_image (list or tuple) - the reference image.
        new_image (list) - the image to modify.
    """
    DISTORTION_RADIUS = 1

    for row in range(len(original_image)):
        for column in range(len(original_image[0])):
            x_relative_indexes = []
            y_relative_indexes = [0]

            # handle y relative indexes
            # +1 to DISTORTION_RADIUS because stop is exclusive
            for relative_y in range(-DISTORTION_RADIUS, DISTORTION_RADIUS + 1):
                if (
                    row + relative_y < 0
                    or row + relative_y > len(original_image) - 1
                ):
                    # ignore relative indexes that are out of range of the original image
                    continue
                # if it isn't out of range, it's valid and should be appended
                y_relative_indexes.append(relative_y)

            # handle x relative indexes
            # +1 to DISTORTION_RADIUS because stop is exclusive
            for relative_x in range(-DISTORTION_RADIUS, DISTORTION_RADIUS + 1):
                if (
                    column + relative_x < 0
                    or column + relative_x > len(original_image[0]) - 1
                ):
                    # ignore relative indexes that are out of range of the original image
                    continue
                # if it isn't out of range, it's valid and should be appended
                x_relative_indexes.append(relative_x)

            # at this point, x_relative_indexes and y_relative_indexes are
            # complete, so now we use them.
            r_total = g_total = b_total = counter = 0  # initialize variables
            for x in x_relative_indexes:
                for y in y_relative_indexes:
                    # since images are 'rgb':
                    # red is the first val
                    r_total += original_image[row + y][column + x][0]

                    # green is the second val
                    g_total += original_image[row + y][column + x][1]

                    # blue is third val
                    b_total += original_image[row + y][column + x][2]

                    counter += 1

            # round because images don't deal w/ floats, only integers
            r_avg = round(r_total / counter)
            g_avg = round(g_total / counter)
            b_avg = round(b_total / counter)

            # update the pixel in newimg to match the average of its
            # surrounding pixels
            new_image[row][column] = [r_avg, g_avg, b_avg]


print("now modifying file. Depending on your pc, this may take a while.")
distort(img, newimg)

# Code that displays the new image at the end
print("now displaying the new image")
plt.imshow(newimg)
plt.show()
