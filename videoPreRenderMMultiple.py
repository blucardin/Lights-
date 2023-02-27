#get the positions list from the piclke file
import pickle
import cv2

positions = pickle.load(open("positionsGood.p", "rb"))

# find the max value x and y coordinates
max_x = max(positions, key=lambda item:item[0])[0]
max_y = max(positions, key=lambda item:item[1])[1]

# find the min value x and y coordinates
min_x = min(positions, key=lambda item:item[0])[0]
min_y = min(positions, key=lambda item:item[1])[1]

# load the video file
vid = cv2.VideoCapture('Touhou - Bad Apple.mp4')


positions = [(x - min_x, y - min_y) for x, y in positions]
allPixels = []

#get the number of frames
num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

# split it up into chunks of 1000
q = 0
divisionFactor = 2  
for i in range(0, num_frames): 
    pixels = []
    print(i, num_frames)
    # read the frame
    _, img = vid.read()

    # resize the image to fit the screen
    img = cv2.resize(img, (max_x - min_x + 1, max_y - min_y + 1))

    # loop through the positions and turn the pixels on if they are white
    for idx, position in enumerate(positions):
        pixels.append([img[position[1], position[0]][1] // divisionFactor, img[position[1], position[0]][2]  // divisionFactor, img[position[1], position[0]][0]  // divisionFactor])

    allPixels.append(pixels)

    if i % 1000 == 0 and i != 0:
        pickle.dump(allPixels, open("allPixels" + str(q) + ".p", "wb"))
        q += 1
        allPixels = []

pickle.dump(allPixels, open("allPixels" + str(q) + ".p", "wb"))

print("done")
print(allPixels[10])

