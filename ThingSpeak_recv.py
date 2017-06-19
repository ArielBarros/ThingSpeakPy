# -*- coding: utf-8 -*-
import ThingSpeakPy
from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", metavar='IDCHANNEL', help="Specify the id channel", required=True)
parser.add_argument("-k", metavar='READAPIKEY', help="Specify the read API key", required=True)
parser.add_argument("-f", metavar='NUMFIELD', type=int, help="Specify the field you want", required=True)
parser.add_argument("-r", metavar='NUMRESULTS', type=int, help="Specify the number of results you want", required=True)
args = parser.parse_args()

serverName = 'api.thingspeak.com'
serverPort = 80
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

apiKey = args.k # 'RUOPEE8SJH9FPL4W'
idChannel = args.i # '289885'
numField = args.f
numResults = args.r

data= ThingSpeakPy.recv(clientSocket, idChannel, apiKey, numField, numResults)

print("Number of registered: ", data['channel']['last_entry_id'])
#print(data)

clientSocket.close()

