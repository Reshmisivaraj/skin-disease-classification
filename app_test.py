import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('my_model.h5')

class_names = ['Healthy', 'Early Blight', 'Late Blight']

img = tf.keras.preprocessing.image.load_img('path/to/image.jpg', target_size=(28, 28))
img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)
img_array = tf.reshape(img_array, (-1, 784))

predictions = model.predict(img_array)

predicted_class = class_names[np.argmax(predictions[0])]
confidence = round(100 * (np.max(predictions[0])), 2)

print(f'Predicted class: {predicted_class}')
print(f'Confidence: {confidence}')