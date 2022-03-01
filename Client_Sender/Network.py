import json
from time import time
from socket import socket

RClient = socket()
RClient.settimeout(0.2)
LastTime = time()
FirstConnect = True

def Send(Host, Port, Text, Color) -> bool:
    print(Host, Port, Text, Color)
    R_SendContent = json.dumps(dict(Type = 'Sender', Text = Text, Color = Color))
    try:
        #print('try1')
        RClient.send(R_SendContent.encode('utf-8'))
    except:
        try:
            global FirstConnect
            if not FirstConnect:
                RClient.close()
            #print('try2')
            RClient.connect((Host, Port))
            FirstConnect = False
            #print('try3')
            RClient.send(R_SendContent.encode('utf-8'))
        except Exception as e:
            print(str(e))
            return False
    return True