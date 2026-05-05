from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_bens():
    response = client.get("/api/v1/bem/")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")

if __name__ == "__main__":
    try:
        test_get_bens()
    except Exception as e:
        print(f"Error: {e}")
