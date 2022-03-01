from sys import argv, exit
from PyQt5.QtWidgets import QApplication
App = QApplication(argv)

from Network import RThread
from Widget import MainWidget as MW

NetThread = None

def Start() -> None:
    if MW.Connected:
        return
    global NetThread
    NetThread = RThread(MW.TextIP.text(), int(MW.TextPort.text()))
    NetThread.start()

def Stop() -> None:
    if not MW.Connected:
        return
    global NetThread
    NetThread.Stop()
    NetThread = None

def main():
    MW.StartButton.pressed.connect(Start)
    MW.StopButton.pressed.connect(Stop)
    App.exec_()
    if NetThread != None:
        NetThread.Stop()
    exit()

if __name__ == '__main__':
    main()