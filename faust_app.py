from contextlib import redirect_stdout
from datetime import datetime as dt

import faust

app = faust.App("myapp", broker="kafka://localhost:29092")
topic = app.topic("unique_users")


@app.agent(topic)
async def uniqueUsers(messages):
    data_per_minute = []
    async for event in messages:
        # 1.2. Isolate uid and timestamp and unixstamp translate
        minute_event = {}
        ts_minute = dt.utcfromtimestamp(event["ts"]).time().replace(second=0, microsecond=0)
        if ts_minute not in [i for s in [d.keys() for d in data_per_minute] for i in s]:
            minute_event[ts_minute] = []
            minute_event[ts_minute].append(event["uid"])
        else:
            data_per_minute[data_per_minute.index(ts_minute)].append(event["uid"])
        data_per_minute.append(minute_event)
        for minute in data_per_minute:
            minute_key = list(minute)[0]
            print(f"Unique visitors per minute at {minute_key}: {len(set(minute[minute_key]))}")


# 3. Write a method for unique values on a minute (optional: day, week, month and year)
# 4. Push events in new topic

if __name__ == "__main__":
    app.main()
