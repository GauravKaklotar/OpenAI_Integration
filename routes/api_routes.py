from flask import Blueprint, request, jsonify
from helpers.openai_helper import get_openai_response, test_streaming

api_bp = Blueprint("api_bp", __name__)

@api_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    response = get_openai_response(prompt)
    return jsonify({"response": response})

@api_bp.route("/test_streaming", methods=["GET"])
def streaming():
    response = test_streaming()
    return jsonify({"response": response})