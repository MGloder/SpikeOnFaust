import faust

app = faust.App('exampleapp', broker='kafka://localhost')


class Order(faust.Record):
    account_id: str
    amount: int


@app.agent(value_type=Order)
async def order(orders):
    async for order in orders:
        print(f'Order for {order.account_id}: {order.amount}')
