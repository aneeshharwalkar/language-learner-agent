"""
Flask server exposing POST /chat per the API contract in docs/api-contract.md.
Run: python server.py
"""

import json

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from agent import chat

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/chat", methods=["POST"])
def handle_chat():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    dialect = data.get("dialect")
    message = data.get("message", "")
    scenario = data.get("scenario")
    history = data.get("history") or []
    turn = data.get("turn", 0)

    if not dialect:
        return jsonify({"error": "Missing required field: dialect"}), 400
    if not isinstance(history, list):
        return jsonify({"error": "Field 'history' must be a list"}), 400
    try:
        turn = int(turn)
    except (TypeError, ValueError):
        return jsonify({"error": "Field 'turn' must be a number"}), 400

    # `message` may be empty only on the turn-0 opener (scenario set, no history).
    # Otherwise the learner must have said something.
    is_opener_request = turn == 0 and scenario and not history and not str(message).strip()
    if not is_opener_request and not str(message).strip():
        return jsonify({"error": "Missing required field: message"}), 400

    try:
        result = chat(
            dialect,
            str(message),
            scenario=scenario,
            history=history,
            turn=turn,
        )
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except json.JSONDecodeError:
        return jsonify({"error": "Agent returned malformed JSON — retry"}), 502
    except Exception:
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)
