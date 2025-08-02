from flask import Flask, request, jsonify
from chatbot_modified import chatbot_response  # change to 'chatbot' if you rename the file

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    
    if not message:
        return jsonify({"error": "No message provided"}), 400
    
    response = chatbot_response(message)
    return jsonify({"response": response})

@app.route('/')
def home():
    return "🤖 NLP Chatbot API is running!"

if __name__ == '__main__':
    app.run(debug=True)
