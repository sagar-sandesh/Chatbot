import json
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open("intents.json", "r") as f:
    intents = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_msg = request.json.get('msg').lower()

    #rule-based matching
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_msg:
                response = random.choice(intent['responses'])
                return jsonify({'response': response})

    return jsonify({'response': "Sorry, I didn't understand that."})

if __name__ == "__main__":
    app.run(debug=True)
