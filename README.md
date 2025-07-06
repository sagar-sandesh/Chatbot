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
```    
 2. **Create a virtual environment & activate it**

**Window:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

----

 3. **Install dependencies**
```bash
pip install -r requirements.txt
```

----

 4.  **Run the app**
```bash
python app.py
```

----

 5. **Open your browser at http://127.0.0.1:5000**

---- 

 ## ⚙️ How to Use

- Click the 🎤 mic button to start speaking
- Or type your message in the input box and press Send or Enter
- Chatbot replies appear in green, your messages in blue
- Responses are spoken aloud automatically
- Scroll chat history to follow the conversation

----

## 🧩 Project Structure
- ├── app.py                # Flask server & API endpoints
- ├── chatbot_model.py      # ML model loading & inference
- ├── train.py              # Model training script
- ├── model.pkl             # Trained ML model file
- ├── data.pickle           # Data for model vocabulary & classes
- ├── intents.json          # Intents & responses config
- ├── templates/
- │   └── index.html        # Chat UI page
- ├── static/
- │   ├── style.css         # Chat UI styles
- │   └── script.js         # JS for voice and chat interactions
- └── requirements.txt      # Python dependencies

----

## 🎨 Customize Your Chatbot
Edit intents.json to add new questions & answers
Run the training script:
python train.py
Restart Flask app to apply changes

---- 

## 💡 Tips & Troubleshooting
1. Mic issues?
     
    Check browser permissions and microphone hardware

2. PyAudio installation problems?
     
    Use platform-specific instructions (Windows wheels or Linux packages)

3. Voice not supported?
     
    Use modern Chrome/Edge browsers

4. Model loading errors?
     
    Ensure model.pkl and data.pickle are in place

----

## 🔮 Future Plans
- Add GPT-4 integration for smarter replies
- Multi-language support for voice input/output
- User login & chat history saving
- Deploy to public cloud platforms
- Mobile app version

----
## 📄 License
MIT License © 2025 sagar sandesh oli

----
## 👤 Author
Mr. Sagar Sandesh Oli

📧 olisagarsandesh@gmail.com

📍 Based in Finland 🇫🇮 | Originally from Nepal 🇳🇵

----
