from flask import Flask, request, jsonify
from chatbot_module import handle_query

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    question = data.get("question")
    engine = data.get("engine", "openai")
    answer = handle_query(question, engine)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
