# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:30:43 2024

@author: karthik-kunjarakana
"""

import cv2

#reading an Image
image = cv2.imread('C:/Users/bgr/Downloads/OpEn Cv/explore-open-cv/images/house_finch.JPEG')

#extracting height and width

h, w = image.shape[:2]
print(h)
print(w)

#o/p
#416
#500