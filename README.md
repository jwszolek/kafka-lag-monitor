## Kafka LAG monitor tool

#### Install 

To install all dependencies run 


``` 
git clone https://github.com/jwszolek/kafka-lag-monitor.git .
cd ./kafka-monitor-tools
pip install -r requirements.txt
```

#### Options

``` 
Usage: runner.py [options]

Kafka monitor tool

Options:
  -h, --help            show this help message and exit
  -b BROKERS, --borkers=BROKERS
                        broker lists
  -o OUTPUT, --output=OUTPUT
                        output file
```                        

#### Crontab setup

``` * * * * * ( sleep 30 ; python /root/kafka-monitor/runner.py -b 10.0.0.1:9092,10.0.0.2:9092,10.0.0.3:9092 -o /tmp/kafka-monitor/kafka-lag.log ) ```


#### Usage

Run: `python runner.py -b 10.0.0.1:9092,10.0.0.2:9092,10.0.0.3:9092 -o /tmp/kafka-monitor/kafka-lag.log`

Sample output:
```
head kafka-lag.log
{"consumer_lag": 183, "lag": 183, "group": "pdw-console", "partition": 0, "offset_first": 935, "topic": "TEST-DATAMASS-EVENTS", "offset_consumed": 0, "state": "Empty", "offset_last": 1118}
{"consumer_lag": 0, "lag": 0, "group": "pdw-console", "partition": 0, "offset_first": 163, "topic": "TESTING", "offset_consumed": 0, "state": "Empty", "offset_last": 163}
{"consumer_lag": 0, "lag": 0, "group": "pdw-console", "partition": 1, "offset_first": 27, "topic": "TESTING", "offset_consumed": 0, "state": "Empty", "offset_last": 27}
{"consumer_lag": 0, "lag": 0, "group": "pdw-console", "partition": 2, "offset_first": 28, "topic": "TESTING", "offset_consumed": 0, "state": "Empty", "offset_last": 28}
{"consumer_lag": 0, "lag": 0, "group": "pdw-console", "partition": 0, "offset_first": 72, "topic": "DATAMASS-ML-EVENTS", "offset_consumed": 0, "state": "Empty", "offset_last": 72}
{"consumer_lag": 7401, "lag": 7401, "group": "pdw-console", "partition": 0, "offset_first": 11207, "topic": "DATAMASS-MONITOR", "offset_consumed": 0, "state": "Empty", "offset_last": 18608}
{"consumer_lag": 0, "lag": 0, "group": "pdw-console", "partition": 0, "offset_first": 24, "topic": "testing", "offset_consumed": 0, "state": "Empty", "offset_last": 24}
{"consumer_lag": 2, "lag": 2, "group": "pdw-console", "partition": 0, "offset_first": 0, "topic": "apps", "offset_consumed": 0, "state": "Empty", "offset_last": 2}
{"consumer_lag": 2, "lag": 0, "group": "pdw-console", "partition": 1, "offset_first": 0, "topic": "apps", "offset_consumed": 0, "state": "Empty", "offset_last": 0}
```



