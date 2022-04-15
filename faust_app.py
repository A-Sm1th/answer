import faust

app = faust.App("myapp", broker="kafka://localhost:29092")
topic = app.topic("unique_users")


@app.agent(topic)
async def uniqueUsers(messages):
    async for event in messages:
        print(event)


if __name__ == "__main__":
    app.main()
