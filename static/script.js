const micBtn = document.getElementById("mic");
let recognizing = false;
let recognition;

if ('webkitSpeechRecognition' in window) {
  recognition = new webkitSpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.lang = 'en-US';

  recognition.onstart = () => {
    recognizing = true;
    micBtn.textContent = "🎙️ Listening...";
  };

  recognition.onend = () => {
    recognizing = false;
    micBtn.textContent = "🎤";
  };

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    input.value = transcript;
    send.click();
  };

  micBtn.onclick = () => {
    if (recognizing) {
      recognition.stop();
      return;
    }
    recognition.start();
  };
} else {
  micBtn.style.display = 'none'; // Hide mic button if not supported
}

// Text-to-speech function
function speak(text) {
  if ('speechSynthesis' in window) {
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
  }
}

// Update send.onclick to include speech output
send.onclick = () => {
  const msg = input.value.trim();
  if (!msg) return;
  appendMessage("user", msg);
  input.value = "";

  fetch("/get", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ msg })
  })
  .then(res => res.json())
  .then(data => {
    appendMessage("bot", data.response);
    speak(data.response);
  })
  .catch(() => {
    appendMessage("bot", "Oops! Something went wrong.");
  });
};
