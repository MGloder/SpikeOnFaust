import faust

app = faust.App('exampleapp',
                broker='kafka://localhost:9092',
                value_serializer='raw')

greeting_topic = app.topic('greetings')


@app.agent(greeting_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(f'Order for {greeting}')
