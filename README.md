


# 🤖 Chatbot using NLP

This is an intelligent chatbot built using **Natural Language Processing (NLP)** and **Machine Learning**. It includes both a **Streamlit-based user interface** and a **Flask REST API**, allowing interaction via browser or backend integration.

---

## 🚀 Features

- 🧠 **Intent Detection** using TF-IDF + Logistic Regression
- 🎯 **Confidence-based fallback** for unclear inputs
- 😊 **Sentiment-aware replies** using TextBlob
- 🌐 **Multilingual support** with Google Translate
- 💬 **Conversation logging** with timestamps
- 📅 **Daily chat summary** using session memory
- 🌐 **Flask API endpoint** for chatbot interaction

---

## 🗂️ Project Structure

```

chatbot-nlp/
│
├── chatbot.py         # Main chatbot logic (Streamlit + ML + NLP)
├── intents.json                # Intents and responses
├── app.py                      # Flask API for chatbot interaction
├── requirements.txt            # List of required Python libraries
├── README.md                   # This file
└── chat\_log.csv                # (Auto-generated chat history)

````

---

## 💻 How to Run

## 🖥️ Option 1: Streamlit UI

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m textblob.download_corpora
````

2. Launch the chatbot interface:

   ```bash
   streamlit run chatbot_modified.py
   ```

3. Interact with the chatbot via your browser.

---

### 🌐 Option 2: Flask REST API

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Send a POST request to:

   ```
   http://127.0.0.1:5000/chat
   ```

3. Sample request body:

   ```json
   {
     "message": "Hello"
   }
   ```

4. Sample response:

   ```json
   {
     "response": "Hi there! 😊"
   }
   ```

---

## 📦 Requirements

Make sure the following packages are installed:

```txt
streamlit
scikit-learn
joblib
textblob
googletrans==4.0.0-rc1
flask
```

Also run:

```bash
python -m textblob.download_corpora
```

---

## 👩‍💻 Developed By

**Parava Varshita**
BTech Final Year – Artificial Intelligence & Machine Learning
Institute of Aeronautical Engineering (IARE), Dundigal

---

## 🌱 Future Enhancements

* Context-aware multi-turn conversations
* Voice-based interaction
* Chatbot integration with messaging platforms (e.g., Telegram, WhatsApp)


