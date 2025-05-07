from flask import Flask, jsonify
from flask_cors import CORS
import random
import json

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Load quotes from the JSON file
try:
    with open('quotes.json') as f:
        quotes = json.load(f)
except Exception as e:
    quotes = []
    print(f"Error loading quotes.json: {e}")

@app.route('/quote', methods=['GET'])
def get_quote():
    if not quotes:
        return jsonify({"error": "No quotes available"}), 500
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)