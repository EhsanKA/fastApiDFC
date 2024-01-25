# test_delivery_fee_calculator.py
import pytest
from app.fee_calculator import FeeCalculator

### Test cases for test_calculate_base_fee() ###
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

### Test cases for test_calculate_item_surcharge() ###
@pytest.fixture(params=[
    (3, 0),  # number_of_items: 3, Expected Fee: 0
    (4, 0),
    (5, 50),
    (7, 150),
])
def item_surcharge_fixture(request):
    number_of_items, expected_fee = request.param
    calculator = FeeCalculator(1000, 1000, number_of_items, "2024-01-20T16:00:00Z")
    return calculator, expected_fee
def test_calculate_item_surcharge(item_surcharge_fixture):
    calculator, expected_fee = item_surcharge_fixture
    assert calculator._calculate_item_surcharge() == expected_fee

### Test cases for test_bulk_fee() ###
@pytest.fixture(params=[
    (11, 0),  # number_of_items: 10, Expected Fee: 0
    (12, 0),
    (13, 120),
    (15, 120),
])
def bulk_fee_fixture(request):
    number_of_items, expected_fee = request.param
    calculator = FeeCalculator(1000, 1000, number_of_items, "2024-01-20T16:00:00Z")
    return calculator, expected_fee
def test_bulk_fee(bulk_fee_fixture):
    calculator, expected_fee = bulk_fee_fixture
    assert calculator._bulk_fee() == expected_fee

### Test cases for test_calculate_small_order_surcharge() ###
@pytest.fixture(params=[
    (400, 600),  # cart_value: 10, Expected Fee: 0
    (800, 200),
    (1000, 0),
    (1500, 0),
])
def small_order_surcharge_fixture(request):
    cart_value, expected_fee = request.param
    calculator = FeeCalculator(cart_value, 1000, 4, "2024-01-20T16:00:00Z")
    return calculator, expected_fee
def test_calculate_small_order_surcharge(small_order_surcharge_fixture):
    calculator, expected_fee = small_order_surcharge_fixture
    assert calculator._calculate_small_order_surcharge() == expected_fee

### Test cases for test_is_rush_hour() ###
@pytest.fixture(params=[
    ("2023-12-01T16:00:00Z", True),     # Friday, time, is_rush_hour: True
    ("2023-12-08T12:00:00Z", False),    # Friday
    ("2024-01-05T18:59:00Z", True),    # Friday
    ("2023-12-02T18:00:00Z", False),    # Saturday
    ("2023-12-06T17:00:00Z", False),    # Wednesday
    ("2024-01-04T13:00:00Z", False),    # Thursday
])
def is_rush_hour_fixture(request):
    time_, expected_fee = request.param
    calculator = FeeCalculator(1000, 1000, 4, time_)
    return calculator, expected_fee
def test_is_rush_hour(is_rush_hour_fixture):
    calculator, expected_fee = is_rush_hour_fixture
    assert calculator._is_rush_hour() == expected_fee


### Test cases for test_apply_discounts_and_caps() ###
@pytest.fixture(params=[
    (10000, 1300, 1300),  # cart_value: 10000, fee: 1300, Expected Fee: 1300
    (19000, 1800, 1500),
    (20000, 2000, 0),
    (19999, 1600, 1500),
    (27000, 2500, 0)
])
def apply_discounts_and_caps_fixture(request):
    cart_value, current_fee, expected_fee = request.param
    calculator = FeeCalculator(cart_value, 1000, 4, "2024-01-20T16:00:00Z")
    return calculator, current_fee, expected_fee
def test_apply_discounts_and_caps(apply_discounts_and_caps_fixture):
    calculator, current_fee, expected_fee = apply_discounts_and_caps_fixture
    assert calculator._apply_discounts_and_caps(current_fee) == expected_fee


### Test cases for test_apply_discounts_and_caps() ###
@pytest.fixture(params=[
    (790, 2235, 4, "2024-01-15T13:00:00Z", 710),  # cart_value, delivery_distance, number_of_items, order_time_str, Expected Fee
    (600, 1501, 12, "2023-12-01T16:00:00Z", 1361)
])
def calculate_delivery_fee_fixture(request):
    cart_value, delivery_distance, number_of_items, order_time_str, expected_fee = request.param
    calculator = FeeCalculator(cart_value, delivery_distance, number_of_items, order_time_str)
    return calculator, expected_fee
def test_calculate_delivery_fee(calculate_delivery_fee_fixture):
    calculator, expected_fee = calculate_delivery_fee_fixture
    assert calculator.calculate_delivery_fee() == expected_fee