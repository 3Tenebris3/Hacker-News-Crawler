from fastapi.testclient import TestClient
from hn_crawler.interfaces.web import app

client = TestClient(app)

def test_html_home():
    r = client.get("/")
    assert r.status_code == 200
    assert "<table" in r.text

def test_json_endpoint_default():
    r = client.get("/api/entries")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) <= 30

def test_json_endpoint_long_filter():
    r = client.get("/api/entries?filter=long")
    assert r.status_code == 200
    titles = [e["title"] for e in r.json()]
    assert all(len(title.split()) > 5 for title in titles)
