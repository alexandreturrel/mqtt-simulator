import argparse
import json
from random import randint
import string
import paho.mqtt.client as mqtt

parser = argparse.ArgumentParser(prog='MQTT SIMULATOR', description='Simulate one or more mqtt publisher(s).')

parser.add_argument('-b', '--broker', type=str, default='localhost', help='define the broker to connect to. Default=\'localhost\'')
parser.add_argument('-t', '--topic', type=str, help='define a topic to send one or more message(s) to. Default=\'/\'')
parser.add_argument('--topics', type=str, help='define a list of topics to send one or more messages to.')
parser.add_argument('--ftopics', type=str, help='read a text file filled with a list of topics to send messages to.')
parser.add_argument('-m', '--message', type=str, help='define a message to send to the selected topic(s).')
parser.add_argument('--messages', type=str, help='define a list of messages to send to the selected topic(s).')
parser.add_argument('--fmessages', type=str, help='read a text file filled with a list of messages to send to selected topic(s).')
parser.add_argument('--randi', type=int, nargs='?', const=100, help='send a random integer from 0 to the parameter entered to the selected topic(s).')
parser.add_argument('--rands', type=str, nargs='?', const='pokedex.json', help='send a random string to the selected topic(s).')
parser.add_argument('--randjson', type=str, nargs='?', const='pokedex.json', help='send a random json object to the selected topic(s).')
parser.add_argument('--timer', type=int, nargs='?', const=1, help='define a time interval between sending two messages. (seconds)')
parser.add_argument('-c', '--clients', type=int, default=1, help='define the number the simulated clients.')

parser.add_argument('--version', action='version', version='%(prog)s 0.1')
parser.add_argument('-d', '--debug', action='store_true')

args = parser.parse_args()


####    DEBUG   ####

debug = args.debug
debug_out = ''

####    INIT MQTT    ####
broker = ''
port = 1883
topics = []
payloads = []

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(str(client)+" connected with result code "+str(rc))

def new_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    return client

####    BROKER  ####
if args.broker:
    broker = args.broker
    if debug:
        debug_out += 'broker: ' + broker + '\n'

####    TOPICS  ####
if args.topic:
    topics.append(args.topic)
    if debug:
        debug_out += 'topic: ' + args.topic + '\t' + str(topics) + '\n'
elif args.topics:
    topics = args.topics
    if debug:
        debug_out += 'topics: ' + args.topics + '\n'
elif args.ftopics:
    with open('topics.txt','r') as file:
        out = file.readlines()
        topics = [s.rstrip() for s in out]
    if debug:
        debug_out += 'ftopics: ' + args.ftopics + '\t' + str(topics) + '\n'
else:
    topics.append('/')
    if debug:
        debug_out+= 'topic: ' + str(topics) + '\n'

####    MESSAGES    ####
if args.message:
    payloads.append(args.message)
    if debug:
        debug_out += 'message: ' + args.message + '\t' + str(payloads) + '\n'

elif args.messages:
    payloads = messages
    if debug:
        debug_out += 'messages: ' + args.messages + '\n'

elif args.fmessages:
    with open('messages.txt','r') as file:
        out = file.readlines()
        payloads = [s.rstrip() for s in out]
    if debug:
        debug_out += 'fmessages: ' + args.fmessages + '\t' + str(payloads) + '\n'


####    RANDOMS     ####
elif args.randi:
    out_randi = randint(0,args.randi)
    payloads.append(out_randi)
    if debug:
        debug_out += 'randi: ' + str(out_randi) + '\t' + str(payloads) + '\n'

elif args.rands:
    with open('pokedex.json') as pokedex:
        data = json.load(pokedex)
        random_index = randint(0, len(data) - 1)
        out_rands = data[random_index]['name']['english']
        payloads.append(out_rands)
        if debug:
            debug_out += 'rands: ' + out_rands + '\t' + str(payloads) + '\n'

elif args.randjson:
    with open('pokedex.json') as pokedex:
        data = json.load(pokedex)
        random_index = randint(0, len(data)-1)
        out_randjson = data[random_index]
        payloads.append(out_randjson)
        if debug:
            debug_out += 'randjson: ' + str(out_randjson) + '\t' + str(payloads) + '\n'

else:
    payloads.append('Hello World!')
    if debug:
        debug_out += 'payload: ' + str(payloads) + '\n'

####    CLIENTS     ####
if args.clients != 1:
    if debug:
        debug_out += 'clients: ' + str(args.clients)

if debug:
    print(debug_out)
