# 🤖 Smart NLP Chatbot

An intelligent NLP-based chatbot with enhanced features, built using Machine Learning, Text Processing, and Streamlit for a user-friendly interface.

## 🚀 Features

- **Intent Recognition** using Logistic Regression and TF-IDF
- **Confidence Score** with fallback for unclear queries
- **Sentiment-Aware Responses** (happy, neutral, sad tone detection)
- **Multilingual Input Support** using Google Translate
- **Chat History Logging** with timestamps
- **Daily Chat Summary** with your last interactions

## 🧠 Tech Stack

- Python, Streamlit
- scikit-learn, joblib
- TextBlob for sentiment analysis
- Googletrans for translation

## 🗂 Files

- `chatbot.py` – Main code
- `intents.json` – Predefined patterns and responses
- `chat_log.csv` – Auto-created for storing conversation history

## ⚙️ Setup & Run

1. Clone the repo and install dependencies:
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    ```

2. Run the chatbot:
    ```bash
    streamlit run chatbot_modified.py
    ```

3. Interact with the bot via the web UI!

## 👩‍💻 Built By

Parava Varshita  
BTech Final Year, AIML Dept – IARE College
