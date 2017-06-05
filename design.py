# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(685, 493)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.your_songs = QtGui.QLabel(self.centralwidget)
        self.your_songs.setObjectName(_fromUtf8("your_songs"))
        self.gridLayout_2.addWidget(self.your_songs, 0, 0, 1, 1)
        self.sidebar = QtGui.QScrollArea(self.centralwidget)
        self.sidebar.setMinimumSize(QtCore.QSize(163, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(216, 16777215))
        self.sidebar.setStyleSheet(_fromUtf8("border: 0px transparent solid;"))
        self.sidebar.setFrameShape(QtGui.QFrame.NoFrame)
        self.sidebar.setFrameShadow(QtGui.QFrame.Plain)
        self.sidebar.setWidgetResizable(True)
        self.sidebar.setObjectName(_fromUtf8("sidebar"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 216, 452))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.sidebar.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.sidebar, 1, 0, 1, 1)
        self.tab_area = QtGui.QTextEdit(self.centralwidget)
        self.tab_area.setObjectName(_fromUtf8("tab_area"))
        self.gridLayout_2.addWidget(self.tab_area, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.your_songs.setText(_translate("MainWindow", "Your Songs", None))
        self.label.setText(_translate("MainWindow", "Recently Played", None))
        self.label_2.setText(_translate("MainWindow", "Your PLaylists", None))
        self.label_3.setText(_translate("MainWindow", "+ New Playlist", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

