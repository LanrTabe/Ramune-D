import json
from sys import argv
from socket import socket
from threading import Thread
from Danmaku import SpawnDanmaku
from Widget import MainWidget as MW

class RThread(Thread):
    def __init__(self, Host : str, Port : int) -> None:
        super().__init__()
        self.Host = Host
        self.Port = Port
        self.Stopped = False
        MW.SetNetState(True)

    def run(self) -> None:

        self.RClient = socket()
        try:
            print('Try to connect', self.Host, self.Port)
            self.RClient.connect((self.Host, self.Port))
            self.RClient.send(json.dumps(dict(Type = 'Receiver')).encode('utf-8'))
            print('Connected')
        except Exception as e:
            MW.SetNetState(False)
            print(e)
            return
        MW.SetNetState(True)
        while True:
            try:
                Content = self.RClient.recv(1024).decode('utf-8')
                print('Received', Content)
                MW.DanmakuSlot.emit(Content)
            except:
                print('P3')
                if not self.Stopped:
                    MW.SetNetState(False)
                return

    def Stop(self) -> None:
        self.Stopped = True
        self.RClient.close()
        MW.Connected = False
        MW.UpdateButton()
