from contextlib import redirect_stdout
from datetime import datetime as dt

import faust

app = faust.App("myapp", broker="kafka://localhost:29092")
topic = app.topic("unique_users")


@app.agent(topic)
async def uniqueUsers(messages):
    data_per_minute = [{"ts": "", "uids": []}]
    async for event in messages:
        minute_event = {}
        ts_minute = (
            dt.utcfromtimestamp(event["ts"])
            .replace(second=0, microsecond=0)
            .strftime("%Y/%m/%d %H:%M")
        )

        if ts_minute not in [d.get("ts") for d in data_per_minute]:
            minute_event["ts"] = ts_minute
            minute_event["uids"] = []
            minute_event["uids"].append(event["uid"])
        else:
            for value in data_per_minute:
                if ts_minute == value.get("ts"):
                    value["uids"].append(event["uid"])
        data_per_minute.append(minute_event)
        for minute in data_per_minute:
            if minute.get("ts") is not None and minute.get("ts") != "":
                print(f"Unique visitors per minute at {minute['ts']}: {len(set(minute['uids']))}")


# 4. Push events in new topic

if __name__ == "__main__":
    app.main()
