from flask import Flask, request, jsonify, render_template
from chatbot import WebsiteChatbot  # Assuming the chatbot class is in chatbot.py
from pathlib import Path

app = Flask(__name__)

# Initialize the chatbot with the dataset
dataset_path = Path("data/chatbot_dataset.json")
chatbot = WebsiteChatbot(dataset_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
