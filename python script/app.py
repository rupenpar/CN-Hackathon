"""Flask API surface for the Guardrail Engine."""

from flask import Flask, jsonify, request

from services import evaluate_action

app = Flask(__name__)


@app.post("/agent_action")
def agent_action() -> tuple:
    """Validate input and evaluate an incoming agent action."""
    if not request.is_json:
        return jsonify({"error": "Request must be application/json"}), 400

    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON payload"}), 400

    action = payload.get("action")
    if action is None:
        return jsonify({"error": "Missing required field: action"}), 400

    if not isinstance(action, str) or not action.strip():
        return jsonify({"error": "Field 'action' must be a non-empty string"}), 400

    result = evaluate_action(action)
    return jsonify(result), 200
