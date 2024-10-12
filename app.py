from flask import Flask, request, jsonify
from openai import OpenAI


import os

app = Flask(__name__)

# Get the OpenAI API key from environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# Root route to display a welcome message
@app.route('/')
def index():
    return "Welcome to the Chatbot API. Use the /chat endpoint to interact with the chatbot."

# Route for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Generate a response using OpenAI's ChatCompletion with the latest model
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ])
        return jsonify({"response": response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
