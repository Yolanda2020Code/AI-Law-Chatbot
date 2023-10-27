from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('chatbot.html')

@app.route('/ai_response', methods=['POST'])
def ai_response():
    user_message = request.json['message']
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=150
    )
    return jsonify(ai_message=response.choices[0].text.strip())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)


