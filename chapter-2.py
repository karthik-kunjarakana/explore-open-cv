# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:38:09 2024

@author: bgr
"""

import cv2

image =cv2.imread('C:/Users/bgr/Downloads/OpEn Cv/explore-open-cv/images/house_finch.JPEG')

#extracting rgb values

(B,G,R)=image[100,100]

print(B)
print(G)
print(R)