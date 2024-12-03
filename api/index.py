from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

