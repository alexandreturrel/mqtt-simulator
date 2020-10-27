# README

## MQTT SIMULATOR

Tool created to simplify mqtt based protocols and architectures.

## HOW TO USE

```
> pip install -r requirements.txt
> start [with arguments] 
```

```
usage: MQTT SIMULATOR [-h] [-b BROKER] [-t TOPIC] [--topics TOPICS]
                      [--ftopics FTOPICS] [-m MESSAGE] [--messages MESSAGES]
                      [--fmessages FMESSAGES] [--randi [RANDI]]
                      [--rands [RANDS]] [--randjson [RANDJSON]]
                      [--timer [TIMER]] [-c CLIENTS] [--version] [-d]

Simulate one or more mqtt publisher(s).

optional arguments:
  -h, --help            show this help message and exit
  -b BROKER, --broker BROKER
                        define the broker to connect to. Default='localhost'
  -t TOPIC, --topic TOPIC
                        define a topic to send one or more message(s) to.
                        Default='/'
  --topics TOPICS       define a list of topics to send one or more messages
                        to.
  --ftopics FTOPICS     read a text file filled with a list of topics to send
                        messages to.
  -m MESSAGE, --message MESSAGE
                        define a message to send to the selected topic(s).
  --messages MESSAGES   define a list of messages to send to the selected
                        topic(s).
  --fmessages FMESSAGES
                        read a text file filled with a list of messages to
                        send to selected topic(s).
  --randi [RANDI]       send a random integer from 0 to the parameter entered
                        to the selected topic(s).
  --rands [RANDS]       send a random string to the selected topic(s).
  --randjson [RANDJSON]
                        send a random json object to the selected topic(s).
  --timer [TIMER]       define a time interval between sending two messages.
                        (seconds)
  -c CLIENTS, --clients CLIENTS
                        define the number the simulated clients.
  --version             show program's version number and exit
  -d, --debug
```
