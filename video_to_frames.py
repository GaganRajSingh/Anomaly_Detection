# code to generate frames of a video
import cv2
import os
from os import path
video_name = 'Robbery032_x264.mp4'
vidcap = cv2.VideoCapture('input_video/' + video_name)
success,image = vidcap.read()
count = 0

input_frames_folder = 'input_frames'
if not path.exists(input_frames_folder):
    os.mkdir(input_frames_folder)

while success:
    cv2.imwrite(input_frames_folder + "/frame%d.jpg" % count, image)     
    success,image = vidcap.read()
    count += 1
    print(count)