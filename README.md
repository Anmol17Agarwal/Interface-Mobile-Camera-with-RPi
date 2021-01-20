# Interface-Mobile-Camera-with-RPi

Raspberry Pi has mostly used hardware to interface/working with the camera-based application. Mainly for Open CV (Open Computer Vision) based applications. As the Raspberry Pi beginner, without USB camera, we can also use our mobile camera to capture an image to process in Raspberry Pi using IP cam. So that USB camera is not needed, with also high resolution. But frame processing will be a little bit slow when compared to USB camera. The mobile which we gonna uses the camera should be connected with the same network at which the Raspberry Pi is connected so that it acts as Local IP to work on IP camera.

### Hardware Requirement
- Raspberry Pi
- SD card
- Power supply
- VGA to HDMI converter (Optional)
- Android Mobile

### Software Requirement
- Raspbian Stretch OS      
- SD card Formatter
- Win32DiskImager (or) Etcher
- IP webcam (Android application

### Python Library Used
- #### urllib
urllib is a Python module that can be used for opening URLs. It defines functions and classes to help in URL actions. With Python you can also access and retrieve data from the internet like XML, HTML, JSON, etc. You can also use Python to work with this data directly.
- #### cv2
OpenCV is a cross-platform library using which we can develop real-time computer vision applications. It mainly focuses on image processing, video capture and analysis including features like face detection and object detection.
To install the package of the opencv just open terminal window in RPi and run the below code
```
sudo pip3 install opencv-python
```
- #### numpy
NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
- #### imutils
Imutils are a series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV and both Python 2.7 and Python 3.
