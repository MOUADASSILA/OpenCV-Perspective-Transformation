#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:28:38 2024

@author: mac
"""

import cv2 
import numpy as np 

# Turn on Laptop's webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is available
    if not ret:
        print("Failed to grab frame")
        break

    # Locate points of the documents or object which you want to transform
    pts1 = np.float32([[150, 260], [490, 260], [150, 400], [490, 400]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))

    # Display the resulting frame
    cv2.imshow('Original Frame', frame) # Initial Capture
    cv2.imshow('Transformed Frame', result) # Transformed Capture

    # Press 'ESC' for exiting video
    if cv2.waitKey(24) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

