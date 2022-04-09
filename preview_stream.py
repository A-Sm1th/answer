import gzip
import json

filename = "stream.jsonl.gz"  # Sample file.

json_content = []
with gzip.open(filename, "rb") as gzip_file:
    for line in gzip_file:  # Read one line.
        line = line.rstrip()
        if line:  # Any JSON data on it?
            obj = json.loads(line)
            json_content.append(obj)

print(json.dumps(json_content, indent=4))
