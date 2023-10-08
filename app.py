from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import cv2
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('wordnet')
import random
import string
import warnings

warnings.filterwarnings('ignore')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#import sys
#from chattt import chatbot_response

# Add the directory to sys.path
#sys.path.append(r'C:\\Users\\Reshmi\\Desktop\\final_app')

# Now you can import modules from the specified directory
#from . import 'C:\\Users\\Reshmi\\Desktop\\final_app\\app\\chattt.py'
#import chattt
#from chattt import chatbot_response
#from . import chattt
#from chattt import chatbot_response
# Rest of your code

#from . import chattt 
#from chattt import chatbot_response  # Import the chatbot_response function from chattt.py
 # Import the chatbot_response function from chattt.py


app = Flask(__name__)
model = tf.keras.models.load_model('SkinDiseasev1.h5')
class_names = ['Acne and Rosacea',
               'Tinea Ringworm Candidiasis and other Fungal Infections',
               'Vasculitis',
    'Urticaria Hives',
    
 'Psoriasis pictures Lichen Planus and related diseases',
 'Warts Molluscum and other Viral Infections',
 'Vascular Tumors',
 'Scabies Lyme Disease and other Infestations and Bites',
 'Systemic Disease',
 'Poison Ivy and other Contact Dermatitis',
 'Seborrheic Keratoses and other Benign Tumors',
 'Light Diseases and Disorders of Pigmentation',
 'Exanthems and Drug Eruptions',
 'Hair Loss Photos Alopecia and other Hair Diseases',
 'Nail Fungus and other Nail Disease',
 'Bullous Disease ',
 'Lupus and other Connective Tissue diseases',
 'Herpes HPV and other STDs Photos',
 'Melanoma Skin Cancer Nevi and Moles',
 'Cellulitis Impetigo and other Bacterial Infections',
 'Eczema Photos',
 'Atopic Dermatitis Photos',
 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
 'Normal']
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def predict(model, img_path):
    try:
        # Open and resize the uploaded image.
        img = Image.open(img_path)
        img = img.resize((224, 224))
        img_array = np.array(img)
        img_array = tf.keras.applications.mobilenet.preprocess_input(img_array)
        img_array = tf.expand_dims(img_array, 0)

        # uses the model to make predictions.
        predictions = model.predict(img_array)
        if predictions.any():
            predicted_class = class_names[np.argmax(predictions[0])]
            confidence = round(100 * (np.max(predictions[0])), 2)
            return predicted_class, confidence
        else:
            return "No predictions", 0.0
    except Exception as e:
        return str(e), 0.0

    # Make prediction on preprocessed image
   
    

        # uses the model to make predictions.
        


@app.route('/predict', methods=['POST'])
def predict_image():
    try:
        file = request.files['image']
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        if '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            predicted_class, confidence = predict(model, file_path)
            os.remove(file_path)
            return jsonify({
                'predicted_class': predicted_class,
                #'confidence': confidence
            })
        else:
            return jsonify({
                'error': 'Invalid file. Please upload an image.'
            })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })



@app.route('/')
def medapp():
    return render_template('medapp.html')
    

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/base')
def Chat():
    return render_template('base.html')

@app.route('/profiles')
def profiles():
    return render_template('profiles.html')

#@app.route('/get_response', methods=['POST'])
#def get_response():
    #user_input = request.form['user_input']
    #response = chatbot_response(user_input)  # Call the chatbot_response function
    #return response
    

if __name__ == '__main__':
    app.run(debug=True)




