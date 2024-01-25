# test_delivery_fee_calculator.py
import pytest
from app.fee_calculator import FeeCalculator
from app.schemas import OrderRequest

# Test case for calculate_base_fee
@pytest.mark.parametrize("distance, expected_fee", [
    (500, 200),
    (1000, 200),
    (1001, 300),
    (1501, 400),
    (2001, 500), 
])
def test_calculate_base_fee(distance, expected_fee):
    calculator = FeeCalculator(1000, distance, 5, "2024-01-20T16:00:00Z")
    assert calculator._calculate_base_fee() == expected_fee

# Test case for calculate_item_surcharge
@pytest.mark.parametrize("number_of_items, expected_fee", [
    (3, 0),
    (4, 0),
    (5, 50),
    (7, 150),
])
def test_calculate_item_surcharge(number_of_items, expected_fee):
    calculator = FeeCalculator(1000, 1000, number_of_items, "2024-01-20T16:00:00Z")
    assert calculator._calculate_item_surcharge() == expected_fee

# Test case for bulk_fee
@pytest.mark.parametrize("number_of_items, expected_fee", [
    (11, 0),
    (12, 0),
    (13, 120),
    (15, 120),
])
def test_bulk_fee(number_of_items, expected_fee):
    calculator = FeeCalculator(1000, 1000, number_of_items, "2024-01-20T16:00:00Z")
    assert calculator._bulk_fee() == expected_fee

# Test case for calculate_small_order_surcharge
@pytest.mark.parametrize("cart_value, expected_fee", [
    (400, 600),
    (800, 200),
    (1000, 0),
    (1500, 0),
])
def test_calculate_small_order_surcharge(cart_value, expected_fee):
    calculator = FeeCalculator(cart_value, 1000, 4, "2024-01-20T16:00:00Z")
    assert calculator._calculate_small_order_surcharge() == expected_fee

# Test case for is_rush_hour
@pytest.mark.parametrize("order_time, is_rush", [
    ("2023-12-01T16:00:00Z", True),
    ("2023-12-08T12:00:00Z", False),
    ("2024-01-05T18:59:00Z", True),
    ("2023-12-02T18:00:00Z", False),
    ("2023-12-06T17:00:00Z", False),
    ("2024-01-04T13:00:00Z", False),
])
def test_is_rush_hour(order_time, is_rush):
    calculator = FeeCalculator(1000, 1000, 4, order_time)
    assert calculator._is_rush_hour() == is_rush

# Test case for apply_discounts_and_caps
@pytest.mark.parametrize("cart_value, fee, expected_fee", [
    (10000, 1300, 1300),
    (19000, 1800, 1500),
    (20000, 2000, 0),
    (19999, 1600, 1500),
    (27000, 2500, 0),
])
def test_apply_discounts_and_caps(cart_value, fee, expected_fee):
    calculator = FeeCalculator(cart_value, 1000, 4, "2024-01-20T16:00:00Z")
    assert calculator._apply_discounts_and_caps(fee) == expected_fee

# Test case for calculate_delivery_fee
@pytest.mark.parametrize("cart_value, delivery_distance, number_of_items, order_time, expected_fee", [
    (790, 2235, 4, "2024-01-15T13:00:00Z", 710),
    (600, 1501, 12, "2023-12-01T16:00:00Z", 1360),
])
def test_calculate_delivery_fee(cart_value, delivery_distance, number_of_items, order_time, expected_fee):
    calculator = FeeCalculator(cart_value, delivery_distance, number_of_items, order_time)
    assert calculator.calculate_delivery_fee() == expected_fee


# Test case for validators
def test_number_of_items_validator():
    with pytest.raises(ValueError, match='number_of_items must be greater than zero'):
        OrderRequest(number_of_items=0, cart_value=100, delivery_distance=100)

def test_cart_value_validator():
    with pytest.raises(ValueError, match='cart_value must be greater than zero'):
        OrderRequest(number_of_items=1, cart_value=0, delivery_distance=100)

def test_delivery_distance_validator():
    with pytest.raises(ValueError, match='delivery_distance must be greater than zero'):
        OrderRequest(number_of_items=1, cart_value=100, delivery_distance=0)
