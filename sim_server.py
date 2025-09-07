from flask import Flask, request, jsonify

app = Flask(__name__)

robot = {"x": 400, "y": 300}

@app.route("/move_rel", methods=["POST"])
def move_rel():
    data = request.get_json()
    dx = data.get("turn", 0)
    dy = data.get("distance", 0)
    robot["x"] += dx
    robot["y"] += dy
    return jsonify({"status": "ok", "robot": robot})

@app.route("/capture", methods=["GET"])
def capture():
    return jsonify({
        "robot": robot,
        "obstacles": [
            {"x": 200, "y": 150, "w": 50, "h": 50},
            {"x": 500, "y": 400, "w": 70, "h": 70}
        ]
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
