import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix

# Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape((-1, 28, 28, 1)) / 255.0
x_test = x_test.reshape((-1, 28, 28, 1)) / 255.0

# One-hot encode labels
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Khởi tạo mô hình CNN
model = Sequential([
    # Set n1 = 50 cho lớp Convolution đầu tiên
    Conv2D(50, (5, 5), activation='relu', input_shape=(28, 28, 1), padding='valid'),
    MaxPooling2D((2, 2)),
    # Set n2 = 30 cho lớp Convolution đầu tiên
    Conv2D(30, (5, 5), activation='relu', padding='valid'),
    MaxPooling2D((2, 2)),
    Flatten(),
    # Set n3 = 20 cho lớp Fully-Connected đầu tiên
    Dense(20, activation='relu'),
    Dropout(0.5), # Có thể không dùng 
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# Data Augmentation
data_gen = ImageDataGenerator(
    rotation_range=20, width_shift_range=0.10, height_shift_range=0.10,
    shear_range=0.1, zoom_range=0.1, horizontal_flip=True, fill_mode='nearest'
)

# Fit the model
history = model.fit(data_gen.flow(x_train, y_train, batch_size=32),
                    epochs=10, validation_data=(x_test, y_test))

# Plotting the training and validation loss and accuracy
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()

plt.show()

# Evaluating the model on test set
y_pred = np.argmax(model.predict(x_test), axis=-1)
y_true = np.argmax(y_test, axis=-1)

# Classification Report and Confusion Matrix
print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))
