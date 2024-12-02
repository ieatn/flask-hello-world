from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def home():
    my_variable = os.environ.get("OPENAI_API_KEY")
    return f"Hello, {my_variable}!"

@app.route('/about')
def about():
    return 'About'
