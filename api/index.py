from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    env_variable = os.getenv("OPENAI_API_KEY", "Not Found")
    return f"The value of YOUR_ENV_VARIABLE is: {env_variable}"

