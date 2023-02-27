
from moviepy.editor import *
import moviepy
import os

# get the list of files in the tempVid folder
files = os.listdir("tempVid")

# sort the files by the number at the end of the file name
files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# ignore the first 14 files
files = files[6:]


files = ["tempVid/" + file for file in files]
print("converting " + str(len(files)) + " images to video")
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(files, fps=25)

# create a list of images
# images = []

# # loop through the files and add them to the list
# p = 0 
# for file in files:
#     p += 1
#     print(p)
#     images.append(ImageClip("/Users/sam/code/lights/home/nvirjee/code/tempVid/" + file).set_duration(1))

#     if p == 100:
#         break

# # create the video
# clip = concatenate_videoclips(images, method="compose")

# write the video to a file
clip.write_videofile("video.mp4", fps=25)

