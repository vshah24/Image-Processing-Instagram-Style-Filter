import cv2
import numpy as np
img_original=cv2.imread('test.jpg')
img_modified=img_original.copy()


def dummy(val):
	pass



identity_kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
gaussian_kernel1 = cv2.getGaussianKernel(3, 0)
gaussian_kernel2 = cv2.getGaussianKernel(5, 0)
box_kernel = np.array([[1,1,1],[1,1,1],[1,1,1]], np.float32) / 9

kernels = [identity_kernel, sharpen_kernel, gaussian_kernel1, gaussian_kernel2, box_kernel]





cv2.namedWindow('app')                   		#Unique so that when we add a slider we can say we ant to add to window name app

		#Create a slider

cv2.createTrackbar('contrast','app',1,100,dummy)        #(Name to display,window name,min value,max value,call back->No need to have a function hence we have dummy function with just pass in it)

cv2.createTrackbar('brightness','app',50,100,dummy)	#50 :below that will be considered as negative value. 

cv2.createTrackbar('filter','app',0,len(kernels)-1,dummy)

cv2.createTrackbar('grayscale','app',1,1,dummy)



while True:
	cv2.imshow('app',img_modified)			#Window name and img 	
	k=cv2.waitKey(1) & 0xFF 			#Why do we need extra things when by just doing waitKey(0)?????
	if k==ord('q'):			 		#Gets numeric value of button q.
		break 

	contrast=cv2.getTrackbarPos('contrast','app')		#This function gives us the value of the contrast bar position currently.
			  #It takes(trackbarname,windowname)

	brightness=cv2.getTrackbarPos('brightness','app')


	kernel = cv2.getTrackbarPos('filter', 'app')


	img_modified = cv2.filter2D(img_original, -1, kernels[kernel])

	img_modified=cv2.addWeighted(img_modified,contrast,np.zeros(img_original.shape,dtype=img_original.dtype),0,brightness-50)  #Weighted as we observed earlier but here we want the current values which will be stored in the contrast and brightness.	
 		   
cv2.destroyAllWindows()
