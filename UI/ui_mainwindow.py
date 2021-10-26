# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.previousEntry = QTextEdit(self.centralwidget)
        self.previousEntry.setObjectName(u"previousEntry")
        self.previousEntry.setGeometry(QRect(0, 0, 900, 300))
        sizePolicy.setHeightForWidth(self.previousEntry.sizePolicy().hasHeightForWidth())
        self.previousEntry.setSizePolicy(sizePolicy)
        self.previousEntry.setMinimumSize(QSize(900, 300))
        self.previousEntry.setMaximumSize(QSize(900, 300))
        font = QFont()
        font.setPointSize(14)
        self.previousEntry.setFont(font)
        self.previousEntry.setReadOnly(True)
        self.currentEntry = QTextEdit(self.centralwidget)
        self.currentEntry.setObjectName(u"currentEntry")
        self.currentEntry.setGeometry(QRect(0, 300, 900, 300))
        sizePolicy.setHeightForWidth(self.currentEntry.sizePolicy().hasHeightForWidth())
        self.currentEntry.setSizePolicy(sizePolicy)
        self.currentEntry.setMinimumSize(QSize(900, 300))
        self.currentEntry.setMaximumSize(QSize(900, 300))
        self.currentEntry.setFont(font)
        self.currentEntry.setReadOnly(False)
        self.todo = QTextEdit(self.centralwidget)
        self.todo.setObjectName(u"todo")
        self.todo.setGeometry(QRect(900, 0, 600, 600))
        sizePolicy.setHeightForWidth(self.todo.sizePolicy().hasHeightForWidth())
        self.todo.setSizePolicy(sizePolicy)
        self.todo.setMinimumSize(QSize(600, 600))
        self.todo.setMaximumSize(QSize(600, 600))
        self.todo.setFont(font)
        self.todo.setReadOnly(True)
        self.console = QTextEdit(self.centralwidget)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(0, 600, 1500, 40))
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMinimumSize(QSize(1500, 40))
        self.console.setMaximumSize(QSize(1500, 40))
        self.console.setFont(font)
        self.reminderList = QTextEdit(self.centralwidget)
        self.reminderList.setObjectName(u"reminderList")
        self.reminderList.setGeometry(QRect(900, 640, 600, 360))
        sizePolicy.setHeightForWidth(self.reminderList.sizePolicy().hasHeightForWidth())
        self.reminderList.setSizePolicy(sizePolicy)
        self.reminderList.setMinimumSize(QSize(600, 360))
        self.reminderList.setMaximumSize(QSize(600, 360))
        self.reminderList.setFont(font)
        self.reminderList.setReadOnly(False)
        self.markdownPreview = QTextEdit(self.centralwidget)
        self.markdownPreview.setObjectName(u"markdownPreview")
        self.markdownPreview.setGeometry(QRect(0, 640, 900, 360))
        sizePolicy.setHeightForWidth(self.markdownPreview.sizePolicy().hasHeightForWidth())
        self.markdownPreview.setSizePolicy(sizePolicy)
        self.markdownPreview.setMinimumSize(QSize(900, 360))
        self.markdownPreview.setMaximumSize(QSize(900, 360))
        self.markdownPreview.setFont(font)
        self.markdownPreview.setReadOnly(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

