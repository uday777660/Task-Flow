import pytest
from app import app, tasks
@pytest.fixture()
def client():
tasks.clear()
app.config["TESTING"] = True
with app.test_client() as c:
yield c
def test_health(client):
r = client.get("/health")
assert r.status_code == 200
assert r.get_json()["status"] == "ok"
def test_create_and_list(client):
r = client.post("/tasks", json={"title": "write lab 1"}) assert r.status_code == 201
r = client.get("/tasks")
assert len(r.get_json()) == 1
def test_create_requires_title(client):
r = client.post("/tasks", json={})
assert r.status_code == 400
def test_complete(client):
tid = client.post("/tasks", json={"title": "x"}).get_json()["id"] r = client.put(f"/tasks/{tid}/complete")
assert r.status_code == 200
assert r.get_json()["done"] is True
