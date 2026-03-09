from PySide6.QtCore import QCoreApplication, QRect, QMetaObject, Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QStatusBar, QWidget, QMenuBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelCamera = QLabel(self.centralwidget)
        self.labelCamera.setObjectName("labelCamera")
        self.labelCamera.setGeometry(QRect(150, 30, 500, 300))

        self.labelCounter = QLabel(self.centralwidget)
        self.labelCounter.setObjectName("labelCounter")
        self.labelCounter.setGeometry(QRect(150, 350, 200, 40))

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName("btnStart")
        self.btnStart.setGeometry(QRect(150, 400, 150, 40))

        self.btnToggleCamera = QPushButton(self.centralwidget)
        self.btnToggleCamera.setObjectName("btnToggleCamera")
        self.btnToggleCamera.setGeometry(QRect(320, 400, 150, 40))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Camera Counter", None))
        self.labelCamera.setText(QCoreApplication.translate("MainWindow", "Camera Feed", None))
        self.labelCounter.setText(QCoreApplication.translate("MainWindow", "Counter: 0", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", "Start Counter", None))
        self.btnToggleCamera.setText(QCoreApplication.translate("MainWindow", "Toggle Camera", None))
