'''
import cv2

def detect_damaged_packages(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use Otsu's thresholding method to segment the image
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Find contours in the image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate through the contours and draw a rectangle around any that are deemed damaged
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
    # Show the image with the detected damaged packages
    cv2.imshow("Damaged Packages", image)
    cv2.waitKey(0)

# Test the function with an example image
detect_damaged_packages("intact package.jpg")
'''

import cv2

def detect_damaged_packages(image_path):
    # Load the image
    cap = cv2.VideoCapture(0)
    
    # Convert the image to grayscale
    while True:
        # Capture a frame from the webcam or video file
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Use Otsu's thresholding method to segment the image
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Find contours in the image
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Iterate through the contours and draw a rectangle around any that are deemed damaged
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 50 and h > 50:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        
        # Show the image with the detected damaged packages
        cv2.imshow('Camera 1', frame)
        cv2.waitKey(1)

# Test the function with an example image
detect_damaged_packages("intact package.jpg")

