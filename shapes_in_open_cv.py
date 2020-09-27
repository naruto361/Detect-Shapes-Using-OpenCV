import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path='resources/shapes4.jpg'

def getContours(img):
    contours,_=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv.contourArea(cnt)
        #print(area)
        
        if area>500:
            cv.drawContours(imgcopy,cnt,-1,(255,0,0),1)
            peri=cv.arcLength(cnt,True)
            #print(peri)
            approx=cv.approxPolyDP(cnt,0.02*peri,True)
            #print(len(approx))
            k=len(approx)
            x,y,w,h=cv.boundingRect(approx)
            cv.rectangle(imgcopy,(x,y),(x+w,y+h),(0,0,0),1)
            if k==3:
                text='triangle'
            elif k==5:
                text='pentagon'
            elif k==6:
                text='hexagon'
            elif k==10:
                text='star'
            elif k==7:
                text='heptagon'
            elif k==8:
                text='octagon'
            elif k==4:
                if w/h>=0.95 and w/h<=1.05:
                    text='square'
                else:
                    text='rectangle'
            else:
                text='circle'
            cv.putText(imgcopy,text,(x+w//2 -25 , y+h//2 +5 ),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
        
            
                 
img=cv.imread(path)
gray=cv.imread(path,0)
imgcopy=np.copy(img)
blur=cv.GaussianBlur(gray,(7,7),1)
canny=cv.Canny(blur,50,50)
blank=np.zeros_like(img)

getContours(canny)

titles=['img','gray','blur','canny','blank','copy']
images=[img,gray,blur,canny,blank,imgcopy]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray'),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()