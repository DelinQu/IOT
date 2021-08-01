import sys
import time
# import cv2

from PyQt5.QtCore import QThread, pyqtSignal, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from sqlBlind import Ui_Dialog


TIME_LIMIT = 100
DECT_RES =[
[99,"3 人","2 人","1 人","无跌倒","无烟雾"],
[100,"3 人","2 人","1 人","无跌倒","无烟雾"],
[98,"3 人","1 人","1 人","无跌倒","无烟雾"],
[98,"3 人","1 人","2 人","无跌倒","无烟雾"],
[97,"3 人","2 人","2 人","无跌倒","无烟雾"],
[99,"3 人","2 人","2 人","无跌倒","无烟雾"],
[99,"3 人","2 人","1 人","出现1人跌倒","无烟雾"],
[99,"3 人","3 人","1 人","出现1人跌倒","无烟雾"],
[97,"3 人","3 人","1 人","无跌倒","烟雾发生火灾"],
[98,"3 人","3 人","1 人","无跌倒","烟雾发生火灾"]
]
BUFSIZE = 10

# 计时器
class Counter(QThread):
    # Runs a counter thread.
    countChanged = pyqtSignal(int)
    count = 0

    def run(self):
        while self.count < TIME_LIMIT:
            self.count +=1
            time.sleep(0.01)
            self.countChanged.emit(self.count)

    def initCount(self,num):
        self.countChanged.emit(num)
        self.count = num

class Dect(QThread):
    dect = pyqtSignal(int)
    cur = 0

    def run(self):
        while 1:
            res = self.cur
            time.sleep(0.5)
            self.dect.emit(res)
            self.cur = (self.cur+1) % len(DECT_RES)

class myWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectSlots()
        self.step = 0
        self.calc = Counter()
        self.dectThread = Dect()
        self.player = QMediaPlayer()
        self.playWidget =[self.player1,self.player2]
        self.fileURL = ['/home/qdl/Desktop/main/Resources/video.mp4',
                        '/home/qdl/Desktop/main/Resources/Dpj.mp4']
        # self.cap = cv2.VideoCapture(0)

    # 绑定组件
    def connectSlots(self):
        # ProcessBar
        self.startButtom.clicked.connect(self.startProcess)

    # 执行注入
    def playVideo(self):
        # 播放
        cur = self.tabMenu.currentIndex()
        self.player.stop()
        self.player.setVideoOutput(self.playWidget[cur])
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.fileURL[cur])))
        self.player.play()
        print("playing...")

    # 设置表格结果
    def setTableContent(self,cnt):
        [dig,c0,c1,c2,c3,c4] = cnt
        item0 = QTableWidgetItem(c0)
        item1 = QTableWidgetItem(c1)
        item2 = QTableWidgetItem(c2)

        item3 = QTableWidgetItem(c3)
        item4 = QTableWidgetItem(c4)

        self.table1.setItem(0,0,item0)
        self.table1.setItem(1,0,item1)
        self.table1.setItem(2,0,item2)

        self.table2.setItem(0,0,item3)
        self.table2.setItem(1,0,item4)

        self.Digit.setDecMode()
        self.Digit.display(dig)


    # 开始注入线程
    def startProcess(self):
        # 初始化
        self.calc.initCount(0)
        self.progressBar.setValue(0)
        self.processLabel.setText("连接设备...")
        self.calc.countChanged.connect(self.onCountChanged)
        self.processLabel.setText("连接中...")
        self.dectThread.dect.connect(self.dect)
        self.calc.start()
        self.dectThread.start()


    def onCountChanged(self, value):
        if value >= TIME_LIMIT:
            self.processLabel.setText("设备就绪")
            self.playVideo()
        self.progressBar.setValue(value)

    # 识别
    def dect(self,value):
        cnt = DECT_RES[value]
        self.setTableContent(cnt)
        print(cnt)
        self.player.stop()
        # 重新设置播放内容
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile( "./Resources"+ str((value+5)%BUFSIZE) +".png")))
        self.player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myWindow()
    w.show()
    sys.exit(app.exec_())

