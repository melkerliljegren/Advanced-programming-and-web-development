from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get("/")
def root():
    # Task 1 – minimal server
    return "Server is running!", 200


@app.get("/about")
def about():
    # Task 2 - custom route
    return "This is a demo API for learning Flask.", 200


@app.post("/greet")
def greet():
    if not request.is_json:
        return jsonify(error="Expected application/json"), 400

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="Malformed JSON (expected an object)"), 400

    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        return jsonify(
            error='Missing or invalid "name" (non-empty string required).',
            example={"name": "Alice"},
        ), 400

    return f"Hello {name.strip()}, nice to meet you!", 200


@app.post("/add")
def add():
    if not request.is_json:
        return jsonify(error="Expected application/json"), 400

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="Malformed JSON (expected an object)"), 400

    missing = [k for k in ("a", "b") if k not in data]
    if missing:
        return jsonify(
            error=f"Missing required key(s): {', '.join(missing)}",
            example={"a": 5, "b": 7},
        ), 400

    a, b = data["a"], data["b"]

    for k, v in {"a": a, "b": b}.items():
        if not isinstance(v, (int, float)):
            return jsonify(
                error=f'Field "{k}" must be a number (int or float).',
                got=type(v).__name__,
                example={"a": 5, "b": 7},
            ), 400

    return jsonify(sum=a + b), 200


if __name__ == "__main__":
    app.run(debug=True)
