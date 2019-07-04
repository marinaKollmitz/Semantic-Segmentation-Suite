#code to generate rgb color labels for 11 class research benchmark version of camvid, available from here: https://github.com/alexgkendall/SegNet-Tutorial/tree/master/CamVid

import cv2
import os
import numpy as np

#these are bgr color codes for the classes 
class_colors = [[128,128,128], #Sky
                [128,0,0], #Building
                [192,192,128], #Pole
                [128,64,128], #Road
                [60,40,222], #Pavement
                [128,128,0], #Tree
                [192,128,128], #SignSymbol
                [64,64,128], #Fence
                [64,0,128], #Car
                [64,64,0], #Pedestrian
                [0,128,192], #Bicyclist
                [0,0,0]] #Unlabelled

for color in class_colors:
    print "%d,%d,%d" % (color[2], color[1], color[0])

#label_path = "/home/kollmitz/datasets/CamVid/SegNet-Tutorial/CamVid/trainannot/"
#conv_label_path = "/home/kollmitz/datasets/CamVid/SegNet-Tutorial/CamVid/train_labels/"
#im_paths = os.listdir(label_path)
#
#for im_path in im_paths:
#    print "im_path", os.path.join(label_path,im_path)
#    image = cv2.imread(os.path.join(label_path,im_path), -1)
#    w,h = image.shape
#    conv_image = np.zeros((w,h,3), np.uint8)
#    
#    for i in range(0,w):
#        for j in range(0,h):
#            conv_image[i,j,:] = class_colors[image[i,j]]
#    
#    cv2.imwrite(os.path.join(conv_label_path, im_path), conv_image)
##    cv2.imshow('image', conv_image)
##    cv2.waitKey(500)
##    cv2.destroyAllWindows()
