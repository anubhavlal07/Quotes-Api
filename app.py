from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

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
    app.run(debug=True)
