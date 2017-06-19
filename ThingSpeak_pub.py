# -*- coding: utf-8 -*-
import ThingSpeakPy
from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-k", metavar='WRITEAPIKEY', help="Specify the write API key", required=True)
parser.add_argument('data', metavar='Data', type=float, nargs='+', help='Data that needs to be sent')
args = parser.parse_args()

serverName = 'api.thingspeak.com'
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

channelKey = args.k # 'DW6DWOL5B2XN6666'
dados = args.data

result = ThingSpeakPy.send(clientSocket, channelKey, dados)

print("Retorno: ", result)

clientSocket.close()
