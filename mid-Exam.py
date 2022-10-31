import cv2
import numpy as np

img = cv2.imread('medicine_with_noise.jpg')

img_background = np.ones((932, 1240, 3), dtype=np.uint8)*255
img_blur = cv2.GaussianBlur(img, (41, 43), 0)
img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)
print(img_blur.shape)

#------------------range---------------------#
upper_range_yellow = np.array([45, 255, 255])
lower_range_yellow = np.array([15, 100, 100])

upper_range_Blue = np.array([125, 150, 255])
lower_range_Blue = np.array([100, 50, 100])

upper_range_pink = np.array([190, 100, 255])
lower_range_pink = np.array([150, 40, 80])

upper_range_black = np.array([125, 120, 120])
lower_range_black = np.array([0, 0, 0])

upper_range_cream = np.array([20, 255, 255])
lower_range_cream = np.array([0, 30, 30])

#-------------------mask--------------------#
mask_1 = cv2.inRange(img_hsv, lower_range_yellow, upper_range_yellow) 
mask_indices_1 = np.where(mask_1 == 255) 
output_yellow = cv2.bitwise_and(img_blur,img_blur,mask=mask_1) 

mask_2 = cv2.inRange(img_hsv, lower_range_Blue, upper_range_Blue) 
mask_indices_2 = np.where(mask_2 == 255)
output_Blue = cv2.bitwise_and(img_blur,img_blur,mask=mask_2)

mask_3 = cv2.inRange(img_hsv, lower_range_pink, upper_range_pink) 
mask_indices_3 = np.where(mask_3 == 255)
output_pink = cv2.bitwise_and(img_blur,img_blur,mask=mask_3)

mask_4 = cv2.inRange(img_hsv, lower_range_black, upper_range_black) 
mask_indices_4 = np.where(mask_4 == 255)
output_black = cv2.bitwise_and(img_blur,img_blur,mask=mask_4)

mask_5 = cv2.inRange(img_hsv, lower_range_cream, upper_range_cream) 
mask_indices_5 = np.where(mask_5 == 255)
output_cream = cv2.bitwise_and(img_blur,img_blur,mask=mask_5)

# --------------------zeros_yellow-----------------------#
zeros_yellow_1 = np.zeros((932, 1240), dtype = np.uint8)
zeros_yellow_2 = np.zeros((932, 1240), dtype = np.uint8)

zeros_Blue_1 = np.zeros((932, 1240), dtype = np.uint8)
zeros_Blue_2 = np.zeros((932, 1240), dtype = np.uint8)
zeros_Blue_3 = np.zeros((932, 1240), dtype = np.uint8)
zeros_Blue_4 = np.zeros((932, 1240), dtype = np.uint8)

zeros_pink_1 = np.zeros((932, 1240), dtype = np.uint8)
zeros_pink_2 = np.zeros((932, 1240), dtype = np.uint8)
zeros_pink_3 = np.zeros((932, 1240), dtype = np.uint8)
zeros_pink_4 = np.zeros((932, 1240), dtype = np.uint8)
zeros_pink_5 = np.zeros((932, 1240), dtype = np.uint8)

zeros_black_1 = np.zeros((932, 1240), dtype = np.uint8)
zeros_black_2 = np.zeros((932, 1240), dtype = np.uint8)
zeros_black_3 = np.zeros((932, 1240), dtype = np.uint8)

zeros_cream_1 = np.zeros((932, 1240), dtype = np.uint8)
zeros_cream_2 = np.zeros((932, 1240), dtype = np.uint8)
zeros_cream_3 = np.zeros((932, 1240), dtype = np.uint8)

# --------------------contours_yellow---------------------#
contours_1,hierachy_1 = cv2.findContours(mask_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt_1 in range(len(contours_1)):
    area_1 = cv2.contourArea(contours_1[cnt_1])
    print(area_1)
    if area_1 == 5821.0 :
        cv2.drawContours(zeros_yellow_1, contours_1, cnt_1, (255,255,255), -1)
    if area_1 == 6262.5 :
        cv2.drawContours(zeros_yellow_2, contours_1, cnt_1, (255,255,255), -1)
   
contours_2,hierachy_2 = cv2.findContours(mask_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt_2 in range(len(contours_2)):
    area_2 = cv2.contourArea(contours_2[cnt_2])
    print(area_2)
    if area_2 == 1506.5 :
        cv2.drawContours(zeros_Blue_1, contours_2, cnt_2, (255,255,255), -1)
    if area_2 == 1517.5 :
        cv2.drawContours(zeros_Blue_2, contours_2, cnt_2, (255,255,255), -1)  
    if area_2 == 1249.0 :
        cv2.drawContours(zeros_Blue_3, contours_2, cnt_2, (255,255,255), -1) 
    if area_2 == 1033.0 :
        cv2.drawContours(zeros_Blue_4, contours_2, cnt_2, (255,255,255), -1) 
        
contours_3,hierachy_3 = cv2.findContours(mask_3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt_3 in range(len(contours_3)):
    area_3 = cv2.contourArea(contours_3[cnt_3])
    # print(area_3)
    if area_3 == 2058.5 :
        cv2.drawContours(zeros_pink_1, contours_3, cnt_3, (255,255,255), -1)
    if area_3 == 1685.0 :
        cv2.drawContours(zeros_pink_2, contours_3, cnt_3, (255,255,255), -1)  
    if area_3 == 1374.5 :
        cv2.drawContours(zeros_pink_3, contours_3, cnt_3, (255,255,255), -1) 
    if area_3 == 1502.5:
        cv2.drawContours(zeros_pink_4, contours_3, cnt_3, (255,255,255), -1) 
    if area_3 == 1460.0 :
        cv2.drawContours(zeros_pink_5, contours_3, cnt_3, (255,255,255), -1)

contours_4,hierachy_4 = cv2.findContours(mask_4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt_4 in range(len(contours_4)):
    area_4 = cv2.contourArea(contours_4[cnt_4])
    # print(area_4)
    if area_4 == 4102.0 :
        cv2.drawContours(zeros_black_1, contours_4, cnt_4, (255,255,255), -1)
    if area_4 == 4423.5 :
        cv2.drawContours(zeros_black_2, contours_4, cnt_4, (255,255,255), -1)  
    if area_4 == 4119.0 :
        cv2.drawContours(zeros_black_3, contours_4, cnt_4, (255,255,255), -1) 
        
contours_5,hierachy_5 = cv2.findContours(mask_5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt_5 in range(len(contours_5)):
    area_5 = cv2.contourArea(contours_5[cnt_5])
    # print(area_5)
    if area_5 == 1641.0 :
        cv2.drawContours(zeros_cream_1, contours_5, cnt_5, (255,255,255), -1)
    if area_5 == 3484.0 :
        cv2.drawContours(zeros_cream_2, contours_5, cnt_5, (255,255,255), -1)  
    if area_5 == 3727.0 :
        cv2.drawContours(zeros_cream_3, contours_5, cnt_5, (255,255,255), -1) 
         
# --------------------where----------------------#  
zeros_yellow_1_out = np.where(zeros_yellow_1 == 255)
zeros_yellow_2_out = np.where(zeros_yellow_2 == 255)
 
zeros_Blue_1_out = np.where(zeros_Blue_1 == 255)
zeros_Blue_2_out = np.where(zeros_Blue_2 == 255)
zeros_Blue_3_out = np.where(zeros_Blue_3 == 255)
zeros_Blue_4_out = np.where(zeros_Blue_4 == 255)

zeros_pink_1_out = np.where(zeros_pink_1 == 255)
zeros_pink_2_out = np.where(zeros_pink_2 == 255)
zeros_pink_3_out = np.where(zeros_pink_3 == 255)
zeros_pink_4_out = np.where(zeros_pink_4 == 255)
zeros_pink_5_out = np.where(zeros_pink_5 == 255)

zeros_black_1_out = np.where(zeros_black_1 == 255)
zeros_black_2_out = np.where(zeros_black_2 == 255)
zeros_black_3_out = np.where(zeros_black_3 == 255)

zeros_cream_1_out = np.where(zeros_cream_1 == 255)
zeros_cream_2_out = np.where(zeros_cream_2 == 255)
zeros_cream_3_out = np.where(zeros_cream_3 == 255)

# --------------------move----------------------#  
img_background[zeros_yellow_1_out[0]-700, zeros_yellow_1_out[1]-440] = img_blur[zeros_yellow_1_out]
img_background[zeros_yellow_2_out[0]-730, zeros_yellow_2_out[1]-250] = img_blur[zeros_yellow_2_out]

img_background[zeros_Blue_1_out[0]-300, zeros_Blue_1_out[1]-1200] = img_blur[zeros_Blue_1_out]
img_background[zeros_Blue_2_out[0]-200, zeros_Blue_2_out[1]-1000] = img_blur[zeros_Blue_2_out]
img_background[zeros_Blue_3_out[0]-100, zeros_Blue_3_out[1]-990] = img_blur[zeros_Blue_3_out]
img_background[zeros_Blue_4_out[0]-10, zeros_Blue_4_out[1]-990] = img_blur[zeros_Blue_4_out]

img_background[zeros_pink_1_out[0]-700, zeros_pink_1_out[1]-100] = img_blur[zeros_pink_1_out]
img_background[zeros_pink_2_out[0]-530, zeros_pink_2_out[1]-600] = img_blur[zeros_pink_2_out]
img_background[zeros_pink_3_out[0]-430, zeros_pink_3_out[1]-500] = img_blur[zeros_pink_3_out]
img_background[zeros_pink_4_out[0]-300, zeros_pink_4_out[1]-180] = img_blur[zeros_pink_4_out]
img_background[zeros_pink_5_out[0]-170, zeros_pink_5_out[1]-1200] = img_blur[zeros_pink_5_out]

img_background[zeros_black_1_out[0]-700, zeros_black_1_out[1]-900] = img_blur[zeros_black_1_out]
img_background[zeros_black_2_out[0]-830, zeros_black_2_out[1]-600] = img_blur[zeros_black_2_out]
img_background[zeros_black_3_out[0]-880, zeros_black_3_out[1]-580] = img_blur[zeros_black_3_out]

img_background[zeros_cream_1_out[0]-1000, zeros_cream_1_out[1]-900] = img_blur[zeros_cream_1_out]
img_background[zeros_cream_2_out[0]-700, zeros_cream_2_out[1]-1350] = img_blur[zeros_cream_2_out]
img_background[zeros_cream_3_out[0]-10, zeros_cream_3_out[1]-580] = img_blur[zeros_cream_3_out]

#---------------------detector Blue---------------------------#
params_1=cv2.SimpleBlobDetector_Params()
params_1.filterByArea=True
params_1.minArea=100
params_1.filterByConvexity=True
params_1.maxConvexity=0.984
params_1.filterByCircularity=True
params_1.minCircularity=0.7
params_1.maxCircularity=0.9                  
params_1.filterByInertia=True
params_1.minInertiaRatio=0.2
params_1.maxInertiaRatio=0.4
detector_1=cv2.SimpleBlobDetector_create(params_1)
keypoints_1=detector_1.detect(img_background)
number_of_blobs=len(keypoints_1)
blank_1=np.zeros((1,1))
img_background=cv2.drawKeypoints(img_background,keypoints_1,blank_1,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
text_1="Med5: "+ str(len(keypoints_1))  + " tablet" 
cv2.putText(img_background,text_1,(480,380),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

#---------------------detector pink---------------------------#
params_2=cv2.SimpleBlobDetector_Params()
params_2.filterByArea=True
params_2.minArea=100
params_2.filterByConvexity=False
params_2.maxConvexity=0.986
params_2.filterByCircularity=True
params_2.minCircularity=0.7
params_2.maxCircularity=0.9                  
params_2.filterByInertia=True
params_2.minInertiaRatio=0.5
params_2.maxInertiaRatio=1
detector_2=cv2.SimpleBlobDetector_create(params_2)
keypoints_2=detector_2.detect(img_background)
blank_2=np.zeros((1,1))
img_background=cv2.drawKeypoints(img_background,keypoints_2,blank_2,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs=len(keypoints_2)
text_2="Med1: "+str(len(keypoints_2))  + " tablet"  
cv2.putText(img_background,text_2,(100,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

#---------------------detector cream---------------------------#
params_3=cv2.SimpleBlobDetector_Params()
params_3.filterByArea=True
params_3.minArea=3000
params_3.filterByConvexity=True
params_3.maxConvexity= 0.987
params_3.filterByCircularity=True
params_3.minCircularity=0.7
params_3.maxCircularity=1                 
params_3.filterByInertia=True
params_3.minInertiaRatio=0.19
params_3.maxInertiaRatio=0.8
detector_3=cv2.SimpleBlobDetector_create(params_3)
keypoints_3=detector_3.detect(img_background)
blank_3=np.zeros((1,1))
img_background=cv2.drawKeypoints(img_background,keypoints_3,blank_3,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs=len(keypoints_3)
text_3="Med2: "+str(len(keypoints_3))  + " tablet"  
cv2.putText(img_background,text_3,(100,580),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

#---------------------detector Black---------------------------#
params_4=cv2.SimpleBlobDetector_Params()
params_4.filterByArea=True
params_4.minArea=2000
params_4.filterByConvexity=False
params_4.maxConvexity=0.987
params_4.filterByCircularity=True
params_4.minCircularity=0.5
params_4.maxCircularity=0.8                 
params_4.filterByInertia=True
params_4.minInertiaRatio=0
params_4.maxInertiaRatio=0.2
detector_4=cv2.SimpleBlobDetector_create(params_4)
keypoints_4=detector_4.detect(img_background)
blank_4=np.zeros((1,1))
img_background=cv2.drawKeypoints(img_background,keypoints_4,blank_4,(255,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs=len(keypoints_4)
text_4="Med4: "+str(len(keypoints_4))  + " capsule"  
cv2.putText(img_background,text_4,(900,700),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

#---------------------detector yellow---------------------------#
params_5=cv2.SimpleBlobDetector_Params()
params_5.filterByArea=True
params_5.minArea=1000
params_5.filterByConvexity=True
params_5.maxConvexity=0.95
params_5.filterByCircularity=True
params_5.minCircularity=0
params_5.maxCircularity=0.5                
params_5.filterByInertia=True
params_5.minInertiaRatio=0
params_5.maxInertiaRatio=1
detector_5=cv2.SimpleBlobDetector_create(params_5)
keypoints_5=detector_5.detect(img_background)
blank_4=np.zeros((1,1))
img_background=cv2.drawKeypoints(img_background,keypoints_5,blank_4,(255,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs=len(keypoints_5)
text_5="Med3: "+str(len(keypoints_5))  + " capsule"  
cv2.putText(img_background,text_5,(450,700),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)

# --------------------imshow-----------------------------#  
cv2.imshow("img", img_background)
# cv2.imshow("img", img_background_yellow)
# cv2.imshow("img", img_background_Blue)
# cv2.imshow("img", img_background_yellow_hsv)
# cv2.imshow("blur", img_blur)
# cv2.imshow("hsv", img_hsv)
# cv2.imshow("converse_color", output_yellow)
# cv2.imshow("converse_color2", output_Blue)
# cv2.imshow("converse_color2", output_pink)
# cv2.imshow("converse_color2", output_black)
# cv2.imshow("converse_color2", output_cream)
# cv2.imshow("mask_6", mask_6)
# cv2.imshow("mask_6", mask_7)
# cv2.imshow('filtering circular blobs',blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()