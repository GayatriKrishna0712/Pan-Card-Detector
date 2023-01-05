# <u>Pan Card Detector</u>

The purpose of this project is to detect tampering of PAN card using computer vision. With the adabce in technology, there are certain cases where the users provide fake IDs. This project will help various organizations where their employees provide them with IDs of verifications and the organization can know whethr the ID provided by their employees is orginal or not.


# Plan of Attack 
1. Get the image from the user.
2. Check the size and image format.
3. Change the shape and size of the image according to the original image
4. Convert the image to grayscale.
5. Find the similarity index of the images.
6. Find the threshod of the image.
7. Finding the contours.
8. Drawing bounding rectangles using contours. 
9. Plot the difference, threshold, original and tampered image.
10. Compare all the images and check the similarity.


# Libraries 
```python 
import cv2  # computer vision for all the image processing requirements
from PIL import Image
import requests # used for fetching data from the URLs as we are going to take images from various urls
from skimage.metrics import structural_similarity  # used to determine the structural similarity score of the original and tamppered image
import imutils  # helps to grab the contours
```


# Dataset
Kaagle Link: https://www.kaggle.com/code/hamedetezadi/card-tampering-detection/data

<u>Orginal Image : </u>

![image](https://user-images.githubusercontent.com/93417245/208227483-41a819c2-5b11-4805-8043-7dd8d13f39c6.png)

Tampered Image : 

![image](https://user-images.githubusercontent.com/93417245/208227511-88bbd041-073a-4ca7-9464-5a1c8ecc264c.png)



# What is meant by Structural Similarity Index?

Structural Similarities means structure of image is compared to that image and the difference between the images in noted as a similarity index score. The Structural Similarity score I got is 0.31451839 (ie) 31%, which is pretty low.So we say that the images are not much similar to each other.. Thus, structural similarity index helps us to determine exactly where in terms of X Y coordinates the location, the image differences are.




#Reference
1. https://www.stanleyulili.com/powershell/solution-to-running-scripts-is-disabled-on-this-system-error-on-powershell/
2. https://www.youtube.com/watch?v=YCzoBsE1KIU
3. https://code.visualstudio.com/docs/python/tutorial-flask

