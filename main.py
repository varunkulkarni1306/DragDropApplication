from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout,QListWidgetItem
from PyQt5.QtWidgets import QLabel
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *





class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()
        self.myListWidget3 = QListWidget()
        self.myListWidget4 = QListWidget()
        self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget3.setViewMode(QListWidget.IconMode)
        self.myListWidget4.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)
        self.myListWidget3.setAcceptDrops(True)
        self.myListWidget3.setDragEnabled(True)
        self.myListWidget4.setAcceptDrops(True)
        self.myListWidget4.setDragEnabled(True)
        self.setGeometry(500, 550, 600, 300)
        self.myLayout = QHBoxLayout()
        self.myLayout.addWidget(self.myListWidget1)
        self.myLayout.addWidget(self.myListWidget2)
        self.myLayout.addWidget(self.myListWidget3)
        self.myLayout.addWidget(self.myListWidget4)

        l1 = QListWidgetItem("P01")
        l2 = QListWidgetItem( "P02")
        l3 = QListWidgetItem("P03")
        l4 = QListWidgetItem("P04")
        l5 = QListWidgetItem("P05")
        l6 = QListWidgetItem("P06")
        l7 = QListWidgetItem("P07")
        l8 = QListWidgetItem("P08")
        l9 = QListWidgetItem("P09")
        l10 = QListWidgetItem("P10")


        self.myListWidget1.insertItem(1, l1)
        self.myListWidget1.insertItem(2, l2)
        self.myListWidget1.insertItem(3, l3)
        self.myListWidget1.insertItem(4, l4)
        self.myListWidget1.insertItem(5, l5)
        self.myListWidget1.insertItem(6, l6)
        self.myListWidget1.insertItem(7, l7)
        self.myListWidget1.insertItem(8, l8)
        self.myListWidget1.insertItem(9, l9)
        self.myListWidget1.insertItem(10, l10)


        widget = QLabel(" Container 1", self)
        dock = QDockWidget(self.myListWidget2)
        dock.setTitleBarWidget(widget)

        widget = QLabel("  Container 2", self)
        dock = QDockWidget(self.myListWidget3)
        dock.setTitleBarWidget(widget)

        widget = QLabel("  container 3", self)
        dock = QDockWidget(self.myListWidget4)
        dock.setTitleBarWidget(widget)


        self.setWindowTitle('Assignment ')
        self.setLayout(self.myLayout)

        self.show()




App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
