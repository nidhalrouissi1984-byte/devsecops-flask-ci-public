
from app import app

def test_home_returns_hello_devsecops():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello DevSecOps!"
