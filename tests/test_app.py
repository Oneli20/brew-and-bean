from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_order():
    client = app.test_client()

    response = client.post(
        "/order",
        data={
            "name": "Test User",
            "coffee": "Cappuccino",
            "quantity": "2"
        }
    )

    assert response.status_code == 200
    assert b"Test User" in response.data