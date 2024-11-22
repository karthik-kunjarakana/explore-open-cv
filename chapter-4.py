# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 07:47:35 2024

"""
''' Resizing the Image
resize() function takes 2 parameters, the image and the dimensions

 '''
import cv2
image =cv2.imread('C:/Users/bgr/Downloads/OpEn Cv/explore-open-cv/images/house_finch.JPEG')
resize = cv2.resize(image,(500,300))
cv2.imshow("Resize", resize)
cv2.waitKey(0)