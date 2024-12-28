from flask import Flask, render_template, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize Flask app
app = Flask(__name__)

# Load saved model and vectorizer (ensure these files exist in your directory)
model = joblib.load('random_forest_model.pkl')  # Your trained model file
vectorizer = joblib.load('tfidf_vectorizer.pkl')  # Your trained vectorizer file

@app.route('/')
def home():
    # Render the HTML page (index.html) when visiting the root URL
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input text from the request
    data = request.get_json()
    text = data['text']
    
    # Transform the text using the TF-IDF vectorizer
    text_vector = vectorizer.transform([text])
    
    # Predict emotion using the trained model
    prediction = model.predict(text_vector)
    
    # Convert prediction to human-readable emotion (adjust as per your model's labels)
    emotion = 'Happy' if prediction[0] == 1 else 'Bad'  # Example: 1=Happy, 0=Bad
    
    return jsonify({"emotion": emotion})

if __name__ == '__main__':
    app.run(debug=True)
