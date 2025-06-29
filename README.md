# 🐾 MEOW MEOW Chatbot — Your Friendly Voice-Enabled AI Companion 🤖

---

### 🎉 Welcome to MEOW MEOW!  
A voice-enabled chatbot powered by Flask, machine learning, and Web Speech APIs. Talk or type — MEOW MEOW listens and responds with personality!

---

## 🚀 Features

- 🎤 **Voice Input:** Speak your message using the mic button  
- 🔊 **Voice Output:** Responses are read aloud using speech synthesis  
- 🤖 **AI-Powered:** Uses a trained ML model for natural conversations  
- 💾 **Persistent Data:** Loads `model.pkl` and `data.pickle` for quick response  
- 🎨 **Colorful, Responsive UI:** Smooth chat experience on desktop & mobile  
- ⚙️ **Easy to Train:** Customize intents & retrain the model anytime

---

## 🛠️ Tech Stack

| Frontend               | Backend          | Python Libraries                             |
|------------------------|------------------|---------------------------------------------|
| HTML5, CSS3, JavaScript| Flask            | flask, nltk, scikit-learn, numpy            |
| Web Speech API (Voice) | Python 3.7+      | pyttsx3, speechrecognition, pyaudio, openai |

---

## 📦 Installation Guide

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/meow-meow-chatbot.git
   cd meow-meow-chatbot

----
## 2. Create a virtual environment & activate it
##. Window: 
python -m venv venv
venv\Scripts\activate

##macOS/Linux:
python3 -m venv venv
source venv/bin/activate

## 3. Install dependencies
pip install -r requirements.txt

## 4. Run the app
pip install -r requirements.txt

## 5. Open your browser at http://127.0.0.1:5000

###⚙️ How to Use
.Click the 🎤 mic button to start speaking
.Or type your message in the input box and press Send or Enter
.Chatbot replies appear in green, your messages in blue
.Responses are spoken aloud automatically
.Scroll chat history to follow the conversation

## 🧩 Project Structure

meow-meow-chatbot/
│
├── app.py                # Flask server & API endpoints
├── chatbot_model.py      # ML model loading & inference
├── train.py              # Model training script
├── model.pkl             # Trained ML model file
├── data.pickle           # Data for model vocabulary & classes
├── intents.json          # Intents & responses config
│
├── templates/
│   └── index.html        # Chat UI page
│
├── static/
│   ├── style.css         # Chat UI styles
│   └── script.js         # JS for voice and chat interactions
│
└── requirements.txt      # Python dependencies
