from fastapi import FastAPI, HTTPException
from app.schemas import OrderRequest
from app.fee_calculator import FeeCalculator

app = FastAPI()


@app.post("/orders/")
def create_order(order_req: OrderRequest):
    fee_calculator = FeeCalculator(order_req.cart_value, order_req.delivery_distance,
                                   order_req.number_of_items, order_req.order_time_str)
    delivery_fee = fee_calculator.calculate_delivery_fee()
    return {"delivery_fee": delivery_fee}
