from fastapi import FastAPI
from schemas import OrderRequest#, OrderResponse
# from fee_calculator import calculate_delivery_fee
from fee_calculator import FeeCalculator

app = FastAPI()


@app.post("/orders/")#, response_model=OrderResponse)
def create_order(order_req: OrderRequest):
    delivery_fee = calculate_delivery_fee(order_req.cart_value, order_req.delivery_distance,
                                          order_req.number_of_items, order_req.order_time)
    return {"delivery_fee": delivery_fee}
