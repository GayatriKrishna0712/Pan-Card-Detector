import cv2  # computer vision for all the image processing requirements
from PIL import Image
import requests # used for fetching data from the URLs as we are going to take images from various urls
from skimage.metrics import structural_similarity  # used to determine the structural similarity score of the original and tamppered image
import imutils  # helps to grab the contours
