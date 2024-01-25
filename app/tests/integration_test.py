from app.fee_calculator import FeeCalculator
from fastapi.testclient import TestClient
from app.main import app  # Assuming your FastAPI app is in 'main.py'

client = TestClient(app)

def test_order_endpoint():
    response = client.post(
        "/orders/",
        json={
            "cart_value": 600,
            "delivery_distance": 1501,
            "number_of_items": 12,
            "order_time": "2023-12-01T16:00:00Z"  # Friday rush hour
        }
    )

    assert response.status_code == 200
    data = response.json()
    calculator = FeeCalculator(600, 1501, 12, "2023-12-01T16:00:00Z")
    expected_fee = calculator.calculate_delivery_fee()
    assert data["delivery_fee"] == expected_fee
