import requests

BASE_URL = "http://localhost:5000"

def test_health():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    assert r.text == "OK"

def test_prediction():
    payload = {
        "features": [5.1, 3.5, 1.4, 0.2]
    }

    r = requests.post(f"{BASE_URL}/predict", json=payload)
    assert r.status_code == 200

    data = r.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], int)

