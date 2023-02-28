# Lights!

![alt text](https://github.com/blucardin/Lights-/blob/a62bd654ee98b5f9166e320bfc36aaa7a4b4cc77/images/redCircle.png?raw=true)

#### Video Demo:  https://youtu.be/PH5mAJPhH-c
#### Description:

For the Lights! project, I displayed videos and images on an addressable set of Christmas lights. 

I used a raspberry pi running python to control the lights. It would accept a numpy array of frames from my computer over ssh. Each frame would be a 2d array of RGB values which the pi would then encode and send to the lights over serial. Finally, it would take an image using a camera and save it to a folder so that I could convert the frames back to a video. 

At first, I struggled with serial communication. I started with an arduino to control the lights, and it worked fine. However, when I switched to a raspberry pi, the lights would not work; they became unstable. Most times, they would not accept signals from the py, when they did, the wrong light would light up. 

I realized that the arduino was sending 5v signals which would be read fine by the 12v lights over the I2C connection, but the pi was sending 3.3v signals which wouldn't be picked up by the lights. I had to use a level shifter to convert the signals. After it arrived in the mail, I was good to go.

I also faced issues with determining the positions of the lights. The way I was able to display images was by determining the position of each light and then mapping the pixels of the image to the lights. I did this by taking a picture of the lights and then using an algorithm to determine the position of each light. 

This algorithm was not perfect. It would apply a gaussian blur to the image, then set the position of the light to the center of the brightest pixel. This would sometimes work, but sometimes the lights would be off by a few pixels. I tried to fix this by changing up the code, but it was not as accurate.

I quickly realized that there was not enough information needed to determine the position of each light. The only way I could fix this was to create a neural network to determine the position of each light. Not only did I not know how to do this, but learning machine learning would take too much time. So I opted to use a pre-trained neural network: my brain. For 15 minutes I clicked the position of every light in order, this gave me very accurate results.

In the end, I got a very good result. My program was able to play back video in near-original time (30fps). Since I only had 500 lights, the resolution was not very good, but it was still very impressive for just a raspberry pi and camera.

In the future, I would like to try putting the lights on an actual Christmas tree or bush to simulate real Christmas lights. 
