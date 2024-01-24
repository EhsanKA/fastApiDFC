# test_delivery_fee_calculator.py
import pytest
from app.fee_calculator import FeeCalculator

@pytest.fixture(params=[
    (500, 200),  # Distance: 1500 meters, Expected Base Fee: 200
    (1000, 200),
    (1001, 300),
    (1501, 400),
    (2001, 500),
])
def base_fee_fixture(request):
    distance, expected_fee = request.param
    calculator = FeeCalculator(1000, distance, 5, "2024-01-20T16:00:00Z")
    return calculator, expected_fee

def test_calculate_base_fee(base_fee_fixture):
    calculator, expected_fee = base_fee_fixture
    assert calculator._calculate_base_fee() == expected_fee

def test_calculate_item_surcharge():
    assert calculate_item_surcharge(4) == 0
    assert calculate_item_surcharge(5) == 50
    assert calculate_item_surcharge(13) == 570

def test_calculate_small_order_surcharge():
    assert calculate_small_order_surcharge(890) == 110
    assert calculate_small_order_surcharge(999) == 1
    assert calculate_small_order_surcharge(1000) == 0
    assert calculate_small_order_surcharge(1200) == 0

def test_is_rush_hour():
    assert is_rush_hour("2024-01-19T16:00:00Z") == False  # Not a Friday
    assert is_rush_hour("2024-01-20T16:00:00Z") == True   # Friday, within rush hour

def test_calculate_rush_hour_surcharge():
    fee = 1000
    assert calculate_rush_hour_surcharge(fee, "2024-01-20T16:00:00Z") == 1200  # Rush hour
    assert calculate_rush_hour_surcharge(fee, "2024-01-19T16:00:00Z") == 1000  # Not rush hour

def test_apply_discounts_and_caps():
    assert apply_discounts_and_caps(1600, 15000) == 1500  # Cap at 1500
    assert apply_discounts_and_caps(500, 21000) == 0     # Free for large cart value

def test_calculate_delivery_fee():
    # Test various scenarios combining all functions
    assert calculate_delivery_fee(800, 2000, 10, "2024-01-20T16:00:00Z") == expected_value  # Replace expected_value with the correct amount
    # Add more scenarios
