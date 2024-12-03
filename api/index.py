from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)
client = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    env_variable = os.getenv("OPENAI_API_KEY", "Not Found")
    return f"The value of YOUR_ENV_VARIABLE is: {env_variable}"


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Ensure you're getting JSON data
    print(data)  # Debug by printing the incoming data
    return jsonify(data)  # Return the same data for testing
