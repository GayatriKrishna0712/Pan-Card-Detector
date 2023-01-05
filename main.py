import cv2  # computer vision for all the image processing requirements
from PIL import Image
import requests # used for fetching data from the URLs as we are going to take images from various urls
from skimage.metrics import structural_similarity  # used to determine the structural similarity score of the original and tamppered image
import imutils  # helps to grab the contours



#opening the original and tampered file downloaded from kaagle---> Step 01
original = Image.open(requests.get("https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg",stream = True).raw)
fake = Image.open(requests.get("https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png",stream = True).raw)

#checking the format and size of the images---> Step 02
print('Orginal image format: ',original.format)
print('Fake image format: ',fake.format)
print('-----------------------------------\n')
print('Orginal image size: ',original.size)
print('Fake image size: ',fake.size)
print('-----------------------------------\n')

#Change the shape and size of the image---> Step 03
original = original.resize((250,150))
fake = fake.resize((250,150))
print('Orginal image size: ',original.size)
print('Fake image size: ',fake.size)
print('-----------------------------------\n')

# saving the images
original.save('pancardtem\images\original.png')
fake.save('pancardtem\images\duplicate.png')

#load the images using cv2 and apply certain cv2 function
original = cv2.imread('D:\Projects\pancard\pancardtem\images\original.png')
fake = cv2.imread('D:\Projects\pancard\pancardtem\images\duplicate.png')

#converting to grayscale--->Step 04
#We do gray scaling becoz in image processing many of the applications don't help to identify the edges of coloured images. Further coloured images are bit complex to understand as they have 3 channels RGB. 
ori_gray = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
fake_gray = cv2.cvtColor(fake,cv2.COLOR_BGR2GRAY)

#Find the similarity index of the images.--->Step 05
#Structural similarities means structure of image is compared to that image and the difference between the images in noted as a similarity index score
score,diff = structural_similarity(ori_gray,fake_gray,full=True)
diff = (diff*255).astype('uint8')
print('SSIM Score: ',round(score,4)*100,'%')
#As the pixel values range from 0 to 256, apart from 0 the range is 255. So dividing all the values by 255 will convert it to range from 0 to 1.
if score >=80:
    print('SSIM Score: ',round(score,4)*100,"%.The document given is original")
else:
    print('SSIM Score: ',round(score,4)*100,"%.The document given is fake")
print('-----------------------------------\n')

#calculating the threshold --->Step 06
thres = cv2.threshold(diff,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]

#Finding the contours --->Step 07
cntr = cv2.findContours(thres.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cntr = imutils.grab_contours(cntr)

#drawing boxes --->Step 08
for c in cntr:
  (x,y,w,h) = cv2.boundingRect(c)  # a rectangle has x lenght y breadth w width and h height
  cv2.rectangle(original,(x,y),(x+w,y+h),(0,0,255),2)
  cv2.rectangle(fake,(x,y),(x+w,y+h),(0,0,255),2)

#Visulizing
Image.fromarray(original)
Image.fromarray(fake)
#visualising the difference between the 2 images
Image.fromarray(diff)
#These black percent only display the difference between the body images, as we have already calculated
