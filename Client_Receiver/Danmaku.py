from time import time
from Widget import MainWidget as MW
from PyQt5.Qt import Qt
from PyQt5.QtCore import QPoint, QPropertyAnimation
from PyQt5.QtWidgets import QLabel, QWidget, QApplication

ScreenWidth = QApplication.desktop().screenGeometry().width()
ScreenHeight = QApplication.desktop().screenGeometry().height()
MaxLine : int = 15
PreDanmakuTime = [None] * (MaxLine + 1)
#AllowOverlap = False
DanmakuSize : int = 40
DanmakuSpeed : int = 100
DanmakuSpace : int = 50

DScreen = QWidget()
DScreen.setGeometry(0, 0, ScreenWidth, DanmakuSize * MaxLine)
DScreen.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
DScreen.setAttribute(Qt.WA_TranslucentBackground)
DScreen.show()

def SpawnDanmaku(Text : str = 'Ramune-D by MizukiCry', Color : str = 'white', Line : int = 1, Time : int = 0) -> None:
    Danmaku = QLabel(DScreen)
    Danmaku.setText(Text)
    Danmaku.setStyleSheet('font-size:%dpx;color:%s' % (DanmakuSize, Color))
    Danmaku.adjustSize()
    #Danmaku.setAttribute(Qt.WA_TransparentForMouseEvents)
    Danmaku.show()

    PreDanmakuTime[Line] = Time + (Danmaku.width() + DanmakuSpace) / DanmakuSpeed
    Danmaku.Anima = QPropertyAnimation(Danmaku, b'pos')
    Danmaku.Anima.setDuration((ScreenWidth + Danmaku.width()) * 1000 // DanmakuSpeed)
    Danmaku.Anima.setStartValue(QPoint(ScreenWidth, (Line - 1) * DanmakuSize))
    Danmaku.Anima.setEndValue(QPoint(-Danmaku.width(), (Line - 1) * DanmakuSize))
    Danmaku.Anima.finished.connect(Danmaku.close)
    Danmaku.Anima.start()

def TrySpawnDanmaku(Text : str = 'Ramune-D by MizukiCry', Color : str = 'white') -> None:
    CurTime = time()
    for i in range(1, MaxLine + 1):
        if PreDanmakuTime[i] == None or CurTime >= PreDanmakuTime[i]:
            print(i, CurTime, PreDanmakuTime[i])
            SpawnDanmaku(Text, Color, i, CurTime)
            return