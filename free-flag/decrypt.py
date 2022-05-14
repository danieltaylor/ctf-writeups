import sys
from PIL import Image

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}'
key = dict()

with Image.open('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}.png') as flag:
    for y in range(1):
        for x in range(len(chars)):
            key[flag.getpixel((x, y))] = chars[x]

with Image.open('freeflag.png') as flag:
    for y in range(1):
        for x in range(flag.size[0]):
            if flag.getpixel((x, y)) == (0, 0, 0, 0):
                break
            print(key[flag.getpixel((x, y))], end='')

print()
