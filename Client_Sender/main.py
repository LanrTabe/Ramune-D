import sys
import Widget
import Network

MW = Widget.MainWidget

def PressedSend() -> None:
    print('PressedSend')
    Res = Network.Send(MW.TextIP.text(), int(MW.TextPort.text()), MW.TextDanmaku.text(), None)
    MW.SetNetState(Res)

def main() -> None:
    MW.SendButton.pressed.connect(PressedSend)
    sys.exit(Widget.App.exec_())

if __name__ == '__main__':
    main()