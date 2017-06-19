# -*- coding: utf-8 -*-
import json

def send(socket, channelKey, values):
    # Example - GET /update?api_key=XFIAM10CT78X2NRF&field1=15&field2=2 HTTP/1.1
    request = [ 'field' + str(index+1) +'='+ str(item) for index,item in enumerate(values)]
    fieldValues = '&'.join(request)
    
    HttpSentence = 'GET /update?api_key='+ channelKey +'&'+ fieldValues + \
    ' HTTP/1.1\r\nHost: api.thingspeak.com\r\n\r\n'
    
    socket.send(HttpSentence.encode())
    response = socket.recv(4096)
    
    return response.decode()
    
def recv(socket, idChannel, apiKey, numField, numResults):
    '''
    Examples    
    GET /channels/289885/feeds.json?api_key=RUOPEE8SJH9FPL4W HTTP/1.1
    GET /channels/289885/feeds.json?api_key=RUOPEE8SJH9FPL4W&results=2 HTTP/1.1
    GET /channels/289885/fields/1.json?api_key=RUOPEE8SJH9FPL4W HTTP/1.1
    GET /channels/289885/fields/1.json?api_key=RUOPEE8SJH9FPL4W&results=2 HTTP/1.1
    '''
    if numField == 0:  
        if numResults == 0:
            HttpSentence = 'GET /channels/'+str(idChannel)+'/feeds.json?api_key='+str(apiKey)+' HTTP/1.1\r\nHost: api.thingspeak.com\r\n\r\n'
        else:
            HttpSentence = 'GET /channels/'+str(idChannel)+'/feeds.json?api_key='+str(apiKey)+'&results='+str(numResults)+' HTTP/1.1\r\nHost: api.thingspeak.com\r\n\r\n'
    else:
        if numResults == 0:
            HttpSentence = 'GET /channels/'+str(idChannel)+'/fields/'+str(numField)+'.json?api_key='+str(apiKey)+' HTTP/1.1\r\nHost: api.thingspeak.com\r\n\r\n'
        else:
            HttpSentence = 'GET /channels/'+str(idChannel)+'/fields/'+str(numField)+'.json?api_key='+str(apiKey)+'&results='+str(numResults)+' HTTP/1.1\r\nHost: api.thingspeak.com\r\n\r\n'
            
    socket.send(HttpSentence.encode())
    response = socket.recv(4096)
    decodedMessage = response.decode()
    splitted = decodedMessage.split('{',1)
    data = '{' + splitted[1]
    data = json.loads(data.split('\r')[0])
    
    return data
