"""
Flask server exposing POST /chat per the API contract in docs/api-contract.md.
Run: python server.py
"""

import json

from flask import Flask, jsonify, request

from agent import chat

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def handle_chat():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    dialect = data.get("dialect")
    message = data.get("message")
    # `turn` is accepted per the API contract (used by the UI for history tracking)
    # but the agent is stateless — we don't need it here.

    if not dialect:
        return jsonify({"error": "Missing required field: dialect"}), 400
    if not message:
        return jsonify({"error": "Missing required field: message"}), 400

    try:
        result = chat(dialect, str(message))
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except json.JSONDecodeError:
        return jsonify({"error": "Agent returned malformed JSON — retry"}), 502
    except Exception:
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
