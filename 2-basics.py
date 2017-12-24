
		#Lecture 10:Open CV Basics
import numpy as np
import cv2
img=cv2.imread('test.jpg')       #Reads the image


#This shows if the image is loaded or not
"""
if img is None:                  
	print 'not loaded'
else:
	print 'loaded'  
"""	

#Earlier code was not displayed that can be done by:

cv2.imshow('test',img)		   #By this command we don't see anything
#cv2.waitKey(0)                     #Helps us to display the image        //no need for seperate waitkey
#cv2.destroyAllWindows()


print img.shape          #Prints the height and width


		#Lecture 11:Color Space Conversion

#Convert RGB to Gray Scale
"""
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                   #Converts from Color to Gray         (image,cv2_COLOR *From To) 
cv2.imshow('gray',gray)		   
cv2.waitKey(0)                     
cv2.destroyAllWindows()


"""
		#Lecture 12:Brighness and Contrast

"""
cb_img=cv2.addWeighted(img,4,img.copy(),0,100)                 #Weighted Value :( img,alpha,img-2,beta,gamma)  
cv2.imshow('cb_img',cb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
		#Lecture 13:Convolution

K=np.array([
	[0,-1,0],
	[-1,5,-1],                             #		//Identity Kernel    ->Exactly the same as the original 
	[0,-1,0],
])

convolved=cv2.filter2D(img,-1,K)                      #(img,depth //rgb has depth 3 and -1 if we are not sure,open cv will figure,Kernel)
cv2.imshow('convolved',convolved)
cv2.waitKey(0)
cv2.destroyAllWindows()

