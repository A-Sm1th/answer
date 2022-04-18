from datetime import datetime as dt

import faust


class UniqueIDPerMinutes(faust.Record):
    date: str
    distincts_id: int


app = faust.App("myapp", broker="kafka://localhost:29092")
unique_users = app.topic("unique_users")
events_per_minute = app.topic("events_per_minute")


@app.agent(unique_users)
async def uniqueUsers(messages) -> None:
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
                uniqueIdperMin = UniqueIDPerMinutes(
                    date=minute["ts"], distincts_id=len(set(minute["uids"]))
                )
                events_per_minute.send(value=uniqueIdperMin)


if __name__ == "__main__":
    app.main()
