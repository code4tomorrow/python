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
img = numpy.array(Image.open(requests.get(url, stream=True).raw)).tolist()
newimg = img
transpose = numpy.transpose(img)

plt.imshow(img)
plt.show()

#write code to create newimg here

plt.imshow(newimg)
plt.show()

plt.imshow(transpose)
plt.show()