import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout

#Model architecture
model = Sequential([
    #Convolutional layers
    Conv2D(32, (3,3), activation='relu', input_shape=(height, width, channels)),
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Conv2D(128, (3,3), activation='relu'),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    #Flatten layer to transition from convolutional to fully connected layers
    Flatten(),
    #Dropout layer to reduce overfitting
    Dropout(0.5),
    #Fully connected layers
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    #Output layer with 3 nodes for clay, silt, and sand content
    Dense(3, activation='linear')
])

#Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

#Fit the model to the training data
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))


#Model perfomance and statistics
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error

# Evaluate the model using r squared and RMSE
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Calculate Residual Prediction Deviation (RPD) and RPIQ statistics
stdev_y = np.std(y_test, axis=0)
rpd = stdev_y / np.sqrt(mean_squared_error(y_test, y_pred))
rpiq = 1 / rpd

# Generate descriptive statistics
df_y = pd.DataFrame(y_test, columns=["Clay", "Silt", "Sand"])
df_y_pred = pd.DataFrame(y_pred, columns=["Clay", "Silt", "Sand"])
df_stats = pd.concat([df_y, df_y_pred], axis=1)
df_stats.describe()
