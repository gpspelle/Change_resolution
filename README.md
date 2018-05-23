# Change video resolution

This code was built to change a video resolution from 1920x1080 to 224x224.
It's using python3 and openCV 3. 

## Usage

To check parameters you'll need
$ python3 convert_channel.py

And an example of usage:

$ python3 change_resolution.py -path video.mp4 -res 224 224

## Todo

Because of some openCV bug, it couldn't be used detected fourcc directly from
the video and instead was used cv2.VideoWriter_fourcc('M','J','P','G') as 
standard.  

In future, it could be the same as the original video, but only this coded
format was able to be saved after resizing.

## References

* https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
* http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
