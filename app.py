from flask import Flask, jsonify, request


app = Flask(__name__)
tasks = {}
next_id = 1


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.post("/tasks")
def create_task():
    global next_id

    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify(error="title is required"), 400

    task = {"id": next_id, "title": title, "done": False}
    tasks[next_id] = task
    next_id += 1
    return jsonify(task), 201


@app.get("/tasks")
def list_tasks():
    return jsonify(list(tasks.values())), 200


@app.put("/tasks/<int:task_id>/complete")
def complete_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify(error="not found"), 404

    task["done"] = True
    return jsonify(task), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
