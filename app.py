
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_msg = request.json.get('msg').lower()

    # Simple intent matching
    for intent, keywords in intents.items():
        if any(keyword in user_msg for keyword in keywords):
            return jsonify({'response': responses[intent]})

    # Default fallback response
    return jsonify({'response': "Sorry, I didn't understand that."})


intents = {
    'greeting': ['hello', 'hi', 'hey', 'good morning', 'good evening'],
    'goodbye': ['bye', 'see you', 'goodbye', 'see ya'],
    'thanks': ['thanks', 'thank you', 'thx'],
    'age': ['how old are you', 'your age'],
}

responses = {
    'greeting': 'Hello! How can I help you today?',
    'goodbye': 'Goodbye! Have a nice day!',
    'thanks': "You're welcome!",
    'age': "I'm a bot, I don't have an age.",
}

if __name__ == "__main__":
    app.run(debug=True)
