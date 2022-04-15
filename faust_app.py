import faust

app = faust.App("myapp", broker="kafka://localhost:29092")
topic = app.topic("unique_users")


@app.agent(topic)
async def uniqueUsers(messages):
    async for event in messages:
        # 1. Isolate uid and timestamp
        print(event["uid"])
        print(event["ts"])


# 2. Translate Unix timestamp into normal date
# 3. Write a method for unique values on a minute (optional: day, week, month and year)
# 4. Push events in new topic

if __name__ == "__main__":
    app.main()
