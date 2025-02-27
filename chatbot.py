
from nltk.chat.util import Chat, reflections

# Define conversation pairs: each pair is a list where:
#   - the first element is a regular expression pattern (to match user input)
#   - the second element is a list of possible responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"what is your name\??", ["My name is ChatBot.", "I'm ChatBot, your friendly assistant."]],
    [r"how are you\??", ["I'm good, thank you!", "Doing well, thanks for asking!"]],
    [r"sorry (.*)", ["No problem.", "Apologies accepted."]],
    [r"i'm (.*) doing good", ["Nice to hear that!", "Great!"]],
    [r"(.*)(location|city)\??", ["I am in the digital world.", "I live in cyberspace!"]],
    [r"(.*) created you\??", ["I was created by a Python developer using NLTK.", "Some brilliant mind built me using NLP techniques."]],
    [r"(.*)(help|support)(.*)", ["I can help you with basic questions. How can I assist you?"]],
    [r"quit", ["Bye, take care! See you soon."]],
    [r"(.*)", ["I'm not sure I understand. Could you please rephrase?"]]
]

def run_chatbot():
    """
    Run the chatbot conversation.
    """
    print("Hi, I'm ChatBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    run_chatbot()
