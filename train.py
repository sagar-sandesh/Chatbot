import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
nltk.download('punkt')
nltk.download('wordnet')

# Load data
with open('intents.json') as f:
    data = json.load(f)

lemmatizer = WordNetLemmatizer()

corpus = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        tokens = word_tokenize(pattern)
        words = [lemmatizer.lemmatize(w.lower()) for w in tokens]
        corpus.append(" ".join(words))
        labels.append(intent['tag'])

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(labels)

# Vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and preprocessors
with open('model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer, encoder, data),f)

print("Model trained and saved as model.pkl")
