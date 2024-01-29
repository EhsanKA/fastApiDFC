from datetime import datetime
import pytz


class FeeCalculator:
    def __init__(self, cart_value, delivery_distance, number_of_items, order_time_str):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.order_time_str = order_time_str

    def calculate_delivery_fee(self):
        fee = 0

        # Calculate base fee and surcharges
        fee += self._calculate_base_fee() 
        fee += self._calculate_item_surcharge() 
        fee += self._bulk_fee() 

        # Apply small order surcharge and consider a linear increase in the fee
        # to make the price, worth to be delivered
        fee += self._calculate_small_order_surcharge() 

        # Apply rush hour multiplier
        fee = self._calculate_rush_hour_surcharge(fee)

        # Apply discounts or caps
        fee = self._apply_discounts_and_caps(fee)

        return fee

    def _calculate_base_fee(self):
        if self.delivery_distance > 1000:
            return 200 + ((self.delivery_distance - 501) // 500) * 100
        return 200

    def _calculate_item_surcharge(self):
        if self.number_of_items >= 5:
            return (self.number_of_items - 4) * 50
        return 0

    def _bulk_fee(self):
        if self.number_of_items > 12:
            return 120
        return 0

    def _calculate_small_order_surcharge(self):
        if self.cart_value < 1000:
            return 1000 - self.cart_value
        return 0

    def _calculate_rush_hour_surcharge(self, fee):
        if self._is_rush_hour():
            return fee * 1.2
        return fee

    # def _is_rush_hour(self):
    #     # here you get the time and must convert their time (using the timezone coming with the 
    #     # order_time_str) and make everything in the UTC timezone.
    #     # then you would check if the tiem falls in the rush hour or not.
    #     # Assuming the input string ends with 'Z' to denote UTC time
    #     order_time = datetime.fromisoformat(self.order_time_str.replace("Z", "+00:00"))
    #     if order_time.weekday() != 4:  # Monday is 0 and Sunday is 6, so Friday is 4
    #         return False

    #     # Rush hour start and end
    #     rush_hour_start = order_time.replace(hour=15, minute=0, second=0)
    #     rush_hour_end = order_time.replace(hour=19, minute=0, second=0)

    #     # Check if the time is within the rush hour period
    #     return rush_hour_start <= order_time < rush_hour_end


    def _is_rush_hour(self):
        # Replace 'Z' with '+00:00' to make the string compatible with fromisoformat
        order_time_str = self.order_time_str.replace("Z", "+00:00")

        # Parse the datetime string to a timezone-aware datetime object
        order_time = datetime.fromisoformat(order_time_str)

        # Convert the time to UTC if it's not already
        if order_time.tzinfo is not None:
            order_time_utc = order_time.astimezone(pytz.utc)
        else:
            order_time_utc = order_time.replace(tzinfo=pytz.utc)

        # Check if the day is Friday (Monday is 0 and Sunday is 6, so Friday is 4)
        if order_time_utc.weekday() != 4:
            return False

        # Define rush hour start and end times in UTC
        rush_hour_start_utc = order_time_utc.replace(hour=15, minute=0, second=0, microsecond=0)
        rush_hour_end_utc = order_time_utc.replace(hour=19, minute=0, second=0, microsecond=0)

        # Check if the time is within the rush hour period in UTC
        return rush_hour_start_utc <= order_time_utc < rush_hour_end_utc


    def _apply_discounts_and_caps(self, fee):
        # Cap the delivery fee and apply free delivery for large orders
        fee = min(fee, 1500) if self.cart_value < 20000 else 0
        return fee
