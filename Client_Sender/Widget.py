import sys
from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QDesktopWidget, QLineEdit, QLabel

class R_Widget(QWidget):

    def __init__(self) -> None:
        super().__init__()
        SizeX, SizeY = 700, 300
        self.setFixedSize(SizeX, SizeY)
        self.setWindowTitle('Ramune-D (Client_Sender)')
        ScreenSize = QDesktopWidget().screenGeometry()
        self.move((ScreenSize.width() - SizeX) // 2, (ScreenSize.height() - SizeY) // 2)

        def EditIP(text) -> None:
            CheckSendable()

        self.TextIP = QLineEdit(self)
        self.TextIP.setGeometry(100, 50, 500, self.TextIP.size().height())
        self.TextIP.setPlaceholderText('IP')
        self.TextIP.setMaxLength(50)
        self.TextIP.textChanged.connect(EditIP)

        def EditPort(text) -> None:
            CheckSendable()

        self.TextPort = QLineEdit(self)
        self.TextPort.setGeometry(100, 100, 500, self.TextPort.size().height())
        self.TextPort.setPlaceholderText('Port')
        self.TextPort.setMaxLength(5)
        self.TextPort.setValidator(QIntValidator())
        self.TextPort.textChanged.connect(EditPort)

        def EditDanmaku(text) -> None:
            CheckSendable()

        self.TextDanmaku = QLineEdit(self)
        self.TextDanmaku.setGeometry(100, 150, 500, self.TextDanmaku.size().height())
        self.TextDanmaku.setPlaceholderText('Ramune-D')
        self.TextDanmaku.setMaxLength(40)
        self.TextDanmaku.textChanged.connect(EditDanmaku)

        def CheckSendable() -> None:
            if self.TextIP.text() != '' and self.TextPort.text() != '' and self.TextDanmaku.text() != '':
                self.SendButton.setEnabled(True)
            else:
                self.SendButton.setEnabled(False)

        self.SendButton = QPushButton('Send', self)
        self.SendButton.setGeometry(300, 200, 100, 50)
        self.SendButton.setEnabled(False)

        self.NetError = QLabel(self)
        self.NetError.setText('Unknown error, please check and try again!')
        self.NetError.setAlignment(Qt.AlignVCenter)
        self.NetError.setAlignment(Qt.AlignHCenter)
        self.NetError.setGeometry(100, 250, 500, 50)
        self.NetError.setVisible(False)

        self.show()


    def SetNetState(self, Flag : bool) -> None:
        self.NetError.setVisible(not Flag)

App = QApplication(sys.argv)
MainWidget = R_Widget()

if __name__ == '__main__':
    sys.exit(App.exec_())