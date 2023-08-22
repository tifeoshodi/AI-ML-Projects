import numpy as np
import cv2

# Load the pre-trained face recognition model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load images of known individuals and their corresponding labels
known_faces = []
labels = []

# Load and label known faces
known_image1 = cv2.imread("C:/Users/JIDE- OSHODI/Pictures/Snaps/tifeoshodi.jpg", cv2.IMREAD_GRAYSCALE)
known_faces.append(known_image1)
labels.append(1)  # Label for Person 1

'''known_image2 = cv2.imread("C:/Users/JIDE- OSHODI/Pictures/Snaps/20221015_124526.jpg", cv2.IMREAD_GRAYSCALE)
known_faces.append(known_image2)
labels.append(2)  # Label for Person 2

known_image2 = cv2.imread("C:/Users/JIDE- OSHODI/Pictures/Snaps/IMG-20230526-WA0072.jpg", cv2.IMREAD_GRAYSCALE)
known_faces.append(known_image2)
labels.append(3)  # Label for Person 3'''

# Train the face recognition model
face_recognizer.train(known_faces, np.array(labels))

# Initialize the video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face recognition
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the captured frame
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate through the detected faces
    for (x, y, w, h) in faces:
        # Extract the face region of interest
        face_roi = gray_frame[y:y+h, x:x+w]

        # Recognize the face
        label, confidence = face_recognizer.predict(face_roi)

        # Define the label text and confidence level
        if confidence < 100:
            label_text = f"Person {label}"
        else:
            label_text = "Unknown"

        confidence_text = f"Confidence: {round(100 - confidence)}%"

        # Draw a rectangle around the face and display the label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, label_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
video_capture.release()
cv2.destroyAllWindows()
