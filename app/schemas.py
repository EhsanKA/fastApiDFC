from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderRequest(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    order_time: Optional[str] = datetime.now().isoformat()
    