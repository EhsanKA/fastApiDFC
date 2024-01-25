from fastapi import FastAPI
from app.schemas import OrderRequest
from app.fee_calculator import FeeCalculator

app = FastAPI()


@app.post("/orders/")
def create_order(order_req: OrderRequest):
    fee_calculator = FeeCalculator(order_req.cart_value, order_req.delivery_distance,
                                   order_req.number_of_items, order_req.order_time)
    delivery_fee = fee_calculator.calculate_delivery_fee()
    return {"delivery_fee": delivery_fee}
