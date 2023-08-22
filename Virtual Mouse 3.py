import cv2
import mediapipe as mp
import pyautogui

# Set up the webcam or video file as the input
cap = cv2.VideoCapture(0)

# Set up the MediaPipe hand tracking pipeline
pipeline = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Initialize the PyAutoGUI mouse position
mouse_x, mouse_y = pyautogui.position()
index_x, index_y = 0, 0

while True:
    # Capture a frame from the webcam or video file
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    
    # Run the frame through the hand tracking pipeline
    output = pipeline.process(rgb_frame)
    hands = output.multi_hand_landmarks
             

    # Check if a hand is detected
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x*frame_width)
                    y = int(landmark.y*frame_height)
                
                    if id == 8: #index finger
                        cv2.circle(img=frame, center=(x,y), radius=15, color=(255,0,0))
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y
                        pyautogui.moveTo(index_x, index_y)

                    if id == 4: #thumb
                        cv2.circle(img=frame, center=(x,y), radius=15, color=(0,248,0))
                        thumb_x = screen_width/frame_width*x
                        thumb_y = screen_height/frame_height*y
                        if abs(index_y - thumb_y) <50:
                            pyautogui.click()
                            pyautogui.sleep(1)

                    '''if id == 12: #middle finger
                        cv2.circle(img=frame, center=(x,y), radius=15, color=(255,0,0))
                        middle_x = screen_width/frame_width*x
                        middle_y = screen_height/frame_height*y
                        pyautogui.dragTo(index_x, index_y)
                        ''' 

            

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
    '''
    # Break the loop if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam or video file
cap.release()

# Destroy the OpenCV window
cv2.destroyAllWindows()

for finger_positions, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
            
                # Extract the positions of the fingers
                finger_positions = landmarks
                index_finger_pos = finger_positions[8]
                thumb_finger_pos = finger_positions[4]
                ring_finger_pos = finger_positions[9]

                # Check if the index finger and thumb are touching
                if (index_finger_pos.x - thumb_finger_pos.x) ** 2 + (index_finger_pos.y - thumb_finger_pos.y) ** 2 < 25:
                    # Hold down the left mouse button and move the mouse cursor using the index finger position
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(index_finger_pos.x, index_finger_pos.y)
                else:
                    # Release the left mouse button and move the mouse cursor using the index finger position
                    pyautogui.mouseUp(button='left')
                    pyautogui.moveTo(index_finger_pos.x, index_finger_pos.y)

                # Check if the ring finger and index finger are touching
                if (ring_finger_pos.x - index_finger_pos.x) ** 2 + (ring_finger_pos.y - index_finger_pos.y) ** 2 < 25:
                    # Simulate a left mouse click
                    pyautogui.click(button='left')
'''
