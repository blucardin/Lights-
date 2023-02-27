from moviepy.editor import *

# Load the two videos from disk
video1 = VideoFileClip("Rick Roll.mp4")
video2 = VideoFileClip("video.mp4")

# # Set the width of each video to half of the total width
# width = int(video1.size[0]/2)

# # Resize each video to the new width and keep the aspect ratio
# video1 = video1.resize(width=width)
# video2 = video2.resize(width=width)

# Combine the two videos side by side
final_video = clips_array([[video1, video2]])

# Add the audio from the first video to the final video
final_video = final_video.set_audio(video1.audio)

# save the final video
final_video.write_videofile("final_video.mp4")
