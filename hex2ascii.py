__author__ = 'cornelia'

from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# img = Image.open('test.png')
img = Image.open('sample.png')
hex = []
ints = []
cubic = []

def cube(x):
    if 0<=x: return x**(1./3.)
    return -(-x)**(1./3.)

pixels = list(img.convert('RGBA').getdata())

for r, g, b, a in pixels: 
    hex.append(rgb2hex(r, g, b))

print hex
print hex[0]
n = len(hex)
print n

for i in range(0, n):
    ints.append(int(hex[i][1:], 16))
print ints

print len(hex) == len (ints)
print len(ints)

for i in range(0, n):
    cubic.append(int(cube(ints[i])))
print cubic
print len(cubic)

target = open("letters.txt", 'w')
target.truncate()
target.seek(0)
for i in range(0, n):
    target.write(chr(cubic[i]))
target.close()