import cv2
import numpy as np
import board
import neopixel
import time
import pickle

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 500

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

positions = []
GaussianRadius = 101

# define a video capture object
vid = cv2.VideoCapture(-1)


p = 0
pixels.fill((0, 0, 0))
pixels[0] = (30, 30, 30)
pixels.show()

def draw_circle(event,x,y,flags,param):
    global p
    if event == cv2.EVENT_LBUTTONDOWN:
        positions.append((x,y))
        p += 1
        print(p, x, y)
        pixels.fill((0, 0, 0))
        pixels[p] = (30, 30, 30)
        pixels.show()


cv2.namedWindow('image')
#make it fullscreen
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback('image',draw_circle)

while(1):

    ret, frame = vid.read()

    cv2.imshow('image',frame)
    
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break

    if p == 499:
        break

pickle.dump(positions, open("positionsGood.p", "wb"))
pixels.fill((100, 100, 100))
pixels.show()

ret2, frame2 = vid.read()

for x in range(0, len(positions)):
    cv2.circle(frame2, positions[x], 5, (0, 0, 255), 2)

# save the image
cv2.imwrite('positions6.png', frame2)

