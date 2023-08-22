import cv2
import numpy as np

def detect_defects(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to segment the image
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop over the contours
    for cnt in contours:
        # Check if the contour is sufficiently large to be a defect
        if cv2.contourArea(cnt) > 1000:
            # Draw a bounding box around the defect
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    # Return the image with defects marked
    return image

# Load an example image
image = cv2.imread("example.jpg")

# Detect defects in the image
result = detect_defects(image)

# Display the result
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
