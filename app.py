from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API key from environment variable
openai.api_key = os.getenv('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')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
