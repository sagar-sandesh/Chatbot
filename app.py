from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key ="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"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_msg = request.json.get('msg').lower()

    if not user_msg:
        return jsonify({'response': 'please say something!'})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_msg}])

        answer = response['choices'][0]['message']['content']
        return jsonify({'response': answer.strip()})

    except Exception as e:
        print("Error:", e)
        return jsonify({'response': "Sorry, I couldn't connect to the smart brain right now."})




    # # Simple intent matching
    # for intent, keywords in intents.items():
    #     if any(keyword in user_msg for keyword in keywords):
    #         return jsonify({'response': responses[intent]})
    #
    # # Default fallback response
    # return jsonify({'response': "Sorry, I didn't understand that."})


# intents = {
#     'greeting': ['hello', 'hi', 'hey', 'good morning', 'good evening'],
#     'goodbye': ['bye', 'see you', 'goodbye', 'see ya'],
#     'thanks': ['thanks', 'thank you', 'thx'],
#     'age': ['how old are you', 'your age'],
# }
#
# responses = {
#     'greeting': 'Hello! How can I help you today?',
#     'goodbye': 'Goodbye! Have a nice day!',
#     'thanks': "You're welcome!",
#      'age': "I'm a bot, I don't have an age.",
# }

if __name__ == "__main__":
    app.run(debug=True)
