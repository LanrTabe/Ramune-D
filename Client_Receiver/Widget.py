import Danmaku
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QLineEdit, QLabel, QSlider

class RWidget(QWidget):

    DanmakuSlot = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(750, 600)
        self.setWindowTitle('Ramune-D (Client_Receiver)')
        ScreenSize = QDesktopWidget().screenGeometry()
        self.move((ScreenSize.width() - 750) // 2, (ScreenSize.height() - 600) // 2)

        self.TextIP = QLineEdit(self)
        self.TextIP.setGeometry(50, 50, 300, 25)
        self.TextIP.setPlaceholderText('IP')
        self.TextIP.setMaxLength(50)
        self.TextIP.textChanged.connect(self.UpdateButton)

        self.TextPort = QLineEdit(self)
        self.TextPort.setGeometry(50, 100, 300, 25)
        self.TextPort.setPlaceholderText('Port')
        self.TextPort.setMaxLength(5)
        self.TextPort.setValidator(QIntValidator())
        self.TextPort.textChanged.connect(self.UpdateButton)

        #region TextDSize

        def ShowDSize(Size : int) -> None:
            self.TextDSize.setText('Danmaku Size(px):%d' % (Size * 5))

        def UpdateDSize() -> None:
            Danmaku.DanmakuSize = self.DSizeSlider.value() * 5

        self.TextDSize = QLabel(self)
        self.TextDSize.setStyleSheet('font-size:20px')
        self.TextDSize.setText('Danmaku Size(px):40')
        self.TextDSize.setGeometry(50, 150, 300, 25)

        self.DSizeSlider = QSlider(Qt.Horizontal, self)
        self.DSizeSlider.setGeometry(50, 175, 300, 25)
        self.DSizeSlider.setMinimum(2)
        self.DSizeSlider.setMaximum(30)
        self.DSizeSlider.setValue(8)
        self.DSizeSlider.valueChanged.connect(ShowDSize)
        self.DSizeSlider.sliderReleased.connect(UpdateDSize)

        #endregion

        #region TextDSpeed
        def ShowDSpeed(Speed : int) -> None:
            self.TextDSpeed.setText('Danmaku Speed(px):%d' % (Speed * 10))

        def UpdateDSpeed() -> None:
            Danmaku.DanmakuSpeed = self.DSpeedSlider.value() * 10

        self.TextDSpeed = QLabel(self)
        self.TextDSpeed.setStyleSheet('font-size:20px')
        self.TextDSpeed.setText('Danmaku Speed(px):100')
        self.TextDSpeed.setGeometry(50, 200, 300, 25)

        self.DSpeedSlider = QSlider(Qt.Horizontal, self)
        self.DSpeedSlider.setGeometry(50, 225, 300, 25)
        self.DSpeedSlider.setMinimum(1)
        self.DSpeedSlider.setMaximum(100)
        self.DSpeedSlider.setValue(10)
        self.DSpeedSlider.valueChanged.connect(ShowDSpeed)
        self.DSpeedSlider.sliderReleased.connect(UpdateDSpeed)
        #endregion

        #region TextDLine
        def ShowDLine(Line : int) -> None:
            self.TextDLine.setText('Danmaku Line:%d' % (Line))

        def UpdateDLine() -> None:
            Danmaku.MaxLine = self.DLineSlider.value()
            Danmaku.PreDanmakuTime = [None] * (Danmaku.MaxLine + 1)
            Danmaku.DScreen.setGeometry(0, 0, Danmaku.ScreenWidth, Danmaku.DanmakuSize * Danmaku.MaxLine)

        self.TextDLine = QLabel(self)
        self.TextDLine.setStyleSheet('font-size:20px')
        self.TextDLine.setText('Danmaku Line:15')
        self.TextDLine.setGeometry(50, 250, 300, 25)

        self.DLineSlider = QSlider(Qt.Horizontal, self)
        self.DLineSlider.setGeometry(50, 275, 300, 25)
        self.DLineSlider.setMinimum(1)
        self.DLineSlider.setMaximum(100)
        self.DLineSlider.setValue(15)
        self.DLineSlider.valueChanged.connect(ShowDLine)
        self.DLineSlider.sliderReleased.connect(UpdateDLine)
        #endregion

        self.StartButton = QPushButton('Start', self)
        self.StartButton.setGeometry(50, 300, 100, 25)

        self.StopButton = QPushButton('Stop', self)
        self.StopButton.setGeometry(250, 300, 100, 25)

        self.Connected = False

        self.NetError = QLabel(self)
        self.NetError.setText('Unknown error')
        self.NetError.setAlignment(Qt.AlignVCenter)
        self.NetError.setAlignment(Qt.AlignHCenter)
        self.NetError.setGeometry(50, 350, 300, 50)
        self.NetError.setVisible(False)

        self.UpdateButton()

        self.DanmakuSlot.connect(self.CreateDanmaku)

        self.show()

    def SetNetState(self, Flag : bool) -> None:
        self.Connected = Flag
        self.NetError.setVisible(not Flag)
        self.UpdateButton()

    def UpdateButton(self) -> None:
        if self.TextIP.text() != '' and self.TextPort.text() != '' and not self.Connected:
            self.StartButton.setEnabled(True)
        else:
            self.StartButton.setEnabled(False)
        self.StopButton.setEnabled(self.Connected)

    def CreateDanmaku(self, Text) -> None:
        Danmaku.TrySpawnDanmaku(Text)
        pass

MainWidget = RWidget()