import cv2
from mtcnn import MTCNN

# Load MTCNN model
detector = MTCNN()

# Load and preprocess an image for face detection
image_path = "C:/Users/JIDE- OSHODI/Desktop/-wrble6.jpg"
image = cv2.imread(image_path)
result = detector.detect_faces(image)

# Get the bounding box and facial landmarks for the detected face
bounding_box = result[0]['box']
landmarks = result[0]['keypoints']

# Draw the bounding box and facial landmarks on the image
cv2.rectangle(image, (bounding_box[0], bounding_box[1]), (bounding_box[0]+bounding_box[2], bounding_box[1]+bounding_box[3]), (0, 255, 0), 2)
cv2.circle(image, (landmarks['left_eye']), 2, (0, 0, 255), 2)
cv2.circle(image, (landmarks['right_eye']), 2, (0, 0, 255), 2)
cv2.circle(image, (landmarks['nose']), 2, (0, 0, 255), 2)
cv2.circle(image, (landmarks['mouth_left']), 2, (0, 0, 255), 2)
cv2.circle(image, (landmarks['mouth_right']), 2, (0, 0, 255), 2)

# Display the image with the bounding box and landmarks
cv2.imshow('MTCNN Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
