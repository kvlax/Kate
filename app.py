from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']

    # Here you can add your AI logic or call an AI service
    # For simplicity, let's just echo the user's input
    ai_response = f"AI says: {user_input}"

    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
