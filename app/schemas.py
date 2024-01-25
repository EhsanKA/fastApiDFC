from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime, timedelta, date

class OrderRequest(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    order_time_str: Optional[str] = Field(
        default_factory=lambda: datetime.utcnow().isoformat(),
        example=datetime.utcnow().isoformat()
    )

    # Add a validator for number_of_items
    @validator('number_of_items')
    def number_of_items_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('number_of_items must be greater than zero')
        return v
    
    @validator('cart_value')
    def cart_value_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('cart_value must be greater than zero')
        return v
    
    @validator('delivery_distance')
    def delivery_distance_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('delivery_distance must be greater than zero')
        return v
    
    # @validator('order_time_str')
    # def time_must_be_present_or_future(cls, v):
    #     order_time = datetime.fromisoformat(v)
    #     current_time = datetime.utcnow()  # Using UTC time
    #     print(order_time)
    #     print(current_time)

    #     # Compare dates
    #     order_date = order_time.date()
    #     current_date = current_time.date()
    #     if order_date < current_date:
    #         raise ValueError('order_date must be today or in the future')

    #     # If the dates are the same, compare times
    #     elif order_date == current_date:
    #         order_time_only = order_time.time()
    #         current_time_only = current_time.time()

    #         # Allow a small time delay between the order time and the current time
    #         time_difference = datetime.combine(date.min, current_time_only) - datetime.combine(date.min, order_time_only)
    #         if time_difference > timedelta(seconds=5):  # Adjust this value as needed
    #             raise ValueError('order_time must be in the present or future or the time delay is too long')

    #     return v