from flask import Flask, jsonify
from app.data_simulator import get_mock_transactions
from app.nudge_engine import generate_nudge
from app.classifier import classify_expense

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AI Financial Nudger!"

@app.route('/nudge', methods=['GET'])
def get_nudge():
    txns = get_mock_transactions()
    nudge = generate_nudge(txns)
    return jsonify({"nudge": nudge})
