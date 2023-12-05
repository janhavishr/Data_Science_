# import tensorflow as tf
# from tensorflow.keras import layers, models
# import numpy as np

# # Build the model
# model = models.Sequential()
# model.add(layers.Dense(1, input_dim=1))
# model.compile(optimizer='sgd', loss='mean_squared_error')

# # Generate data
# X = np.array([1, 2, 3, 4, 5], dtype=float)
# y = np.array([2, 4, 6, 8, 10], dtype=float)

# # Train the model
# model.fit(X, y, epochs=1000, verbose=0)

# # Make a prediction
# new_data = np.array([6], dtype=float)
# prediction = model.predict(new_data)

# print("Prediction for input 6:", prediction[0, 0])

# Import necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate synthetic dataset
np.random.seed(42)
X = np.random.rand(1000, 5)  # 1000 data points with 5 features
y = (X.sum(axis=1) > 2.5).astype(int)  # Binary classification task

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple neural network model
model = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=(5,)),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate the model on the test set
y_pred = (model.predict(X_test) > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy on the test set:", accuracy)

