#get the positions list from the piclke file
import pickle
import cv2
import board
import neopixel

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 500

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

cam = cv2.VideoCapture(-1)
allPixels = []

p = 0
for q in range(0, 7):
    del allPixels[:]
    allPixels = pickle.load(open("allpixels/allPixels" + str(q) + ".p", "rb"))
    print(len(allPixels))

    for x in allPixels:
        print(p)
        p += 1
        pixels[0:-1] = x
        pixels.show()

        # take a picture of the screen
        _, frame = cam.read()

        # save the image
        cv2.imwrite(f'/home/nvirjee/code/badappletempvid/frame{p}.png', frame)