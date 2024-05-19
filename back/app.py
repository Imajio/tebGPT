from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("sk-proj-yE5QgweOhYrZ2u7LLNhtT3BlbkFJoJxxlbCeclPvfUjbIAFP")


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({"response": "No message provided"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        return jsonify({"response": response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({"response": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
