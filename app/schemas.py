from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class OrderRequest(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    order_time_str: Optional[str] = datetime.now().isoformat()

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
