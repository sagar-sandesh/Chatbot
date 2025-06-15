import random
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load trained model and data
with open('model.pkl', 'rb') as f:
    model, vectorizer, encoder, data = pickle.load(f)

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return " ".join(tokens)

def predict_class(text):
    processed = preprocess_text(text)
    x = vectorizer.transform([processed])
    pred = model.predict(x)[0]
    tag = encoder.inverse_transform([pred])[0]
    return tag

def get_response(tag):
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

def chatbot_response(text):
    tag = predict_class(text)
    response = get_response(tag)
    return response


if __name__ == "__main__":
    print("Chatbot is ready! Type something...")
    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        reply = chatbot_response(message)
        print("Bot:", reply)
