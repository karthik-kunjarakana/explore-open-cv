# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:47:53 2024

"""
'''Extracting the Region of Interest (ROI) '''

import cv2
image =cv2.imread('C:/Users/bgr/Downloads/OpEn Cv/explore-open-cv/images/house_finch.JPEG')
region_of_interest = image[50:500,200:700]
print(region_of_interest)
cv2.imshow("ROI",region_of_interest)
cv2.waitKey(0)