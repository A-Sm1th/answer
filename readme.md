# Data Challenge

## Tools used
- Docker
- Offset Explorer 2.2
- VScode

# Suggested steps

## 1. Setup of Kafka based on a Docker
Based on that [tutorial](https://www.baeldung.com/ops/kafka-docker-setup), I did the initial Kafka setup.
Then, I downloaded the sample file from the Docker container.

## 2. Create a topic
Created a topic on Offset Explorer named `dood_stream`

## 3. Use the kafka producer from kafka itself to send our test data to your topic
Executed in the Docker container :`zcat stream.gz | kafka-console-producer --broker-list localhost:29092 --topic dood_stream` based on the sample data section in the original ReadMe file.

## 4. Create a small app that reads this data from kafka and prints it to stdout
By executing `kafka-console-consumer --bootstrap-server kafka:9092 --topic dood_stream` the messages will keep being printed in stdout.

## 5. Find a suitable data structure for counting and implement a simple counting mechanism, output the results to stdout
I setup the pip package Faust on my machine to consume the raw events and manipulate the data.
As the code suggests, I isolated the timestamp values, converted them and rounded them to the minute.
Based on that rounding, I gathered all the events based on the minute. 
As soon as an event is discovered with a new "time", a new dictionary is created with that rounded time.

## 6. Results forwarding to another topic
I tried to forward the results to another topic following the Faust documentation and the GitHub issue [solution](https://github.com/robinhood/faust/issues/305#issuecomment-472176073) but I am not able to display that solution in a new topic `kafka-console-consumer --bootstrap-server localhost:9092 --topic events_per_minute` (executed in the same Docker container as the Kafka one).
# Bonus questions / challenges
The main challenges remained in finding a proper Python package able to consume the data then convert them in the demanded format.

## How can you scale it to improve throughput?
I guess that setting up Kafka on a Kubernetes Cluster would not only able a scaling in throughput but also an increase in reliability of the Kafka consumers and Kafka producers.

## Explain how you would cope with failure if the app crashes mid day / mid year.
- Check if the schema of the events have changed.
- Check the throughput dramatically increased/decreased at once.
- Check if unexpected characters appeared in a Kafka producer.

### Kafka Setup

- M1 Mac incompatibility with Docker solved thanks to that [StackOverflow post](https://stackoverflow.com/questions/65456814/docker-apple-silicon-m1-preview-mysql-no-matching-manifest-for-linux-arm64-v8)
