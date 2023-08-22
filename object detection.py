import tensorflow as tf
import cv2

import tensorflow_datasets as tfds

# Load the COCO dataset
dataset, info = tfds.load('coco/2017', with_info=True)

def preprocess_data(data):
  image = data['image']
  label = data['label']
  
  # Resize the image to a fixed size
  image = tf.image.resize(image, (224, 224))
  
  # Normalize the image
  image = (image - 128) / 128
  
  return image, label

# Split the data into a training set and a validation set
train_data = dataset['train']
val_data = dataset['validation']

# Use the `map` method to apply the preprocessing function to each element in the dataset
train_data = train_data.map(preprocess_data)
val_data = val_data.map(preprocess_data)

# Use the `batch` method to create batches of data
train_data = train_data.batch(32)
val_data = val_data.batch(32)

# Load a pre-trained model
model = tf.keras.applications.ssd_mobilenet_v1.SSDMobileNetV1()

# Alternatively, you can build your own model from scratch using CNNs
'''inputs = tf.keras.Input(shape=(224, 224, 3))
x = tf.keras.layers.Conv2D(32, 3, activation='relu')(inputs)
x = tf.keras.layers.MaxPooling2D(2)(x)
x = tf.keras.layers.Conv2D(64, 3, activation='relu')(x)
x = tf.keras.layers.MaxPooling2D(2)(x)
x = tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
outputs = tf.keras.layers.Dense(len(info.features['label'].names), activation='softmax')(x)'''

model = tf.keras.Model(inputs=inputs, outputs=outputs)

#Compile the model
model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])

#Train the model
model.fit(train_data, epochs=10, validation_data=val_data)

model.save('object_detection_model.h5')

#Load the model
model = tf.keras.models.load_model('object_detection_model.h5')

#Open the webcam
cap = cv2.VideoCapture(0)

while True:

    #Read a frame from the webcam
    _, frame = cap.read()

    #Preprocess the frame
    frame = cv2.resize(frame, (224, 224))
    frame = (frame - 128) / 128

    #Use the model to predict the labels for the frame
    labels = model.predict(frame[tf.newaxis, ...])[0]

    #Loop over the labels and draw bounding boxes on the frame
    for label in labels:
        if label['score'] > 0.5:
            xmin, ymin, xmax, ymax = label['bbox']
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        #Show the frame
        cv2.imshow('Webcam', frame)

        #Break the loop if the user presses the 'q' key
        if cv2.waitKey(1) == ord('q'):
            break

    #Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

