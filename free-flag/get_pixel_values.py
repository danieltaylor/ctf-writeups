# prints the values of the first n pixels in the top row of the image

from PIL import Image

n = 5
with Image.open('BA.png') as image:
	for y in range(1):
		for x in range(n):
			print(image.getpixel((x, y)))
