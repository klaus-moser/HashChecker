# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        MainWindow.setBaseSize(QtCore.QSize(400, 300))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 405, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.picture = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.picture.setMinimumSize(QtCore.QSize(400, 100))
        self.picture.setMaximumSize(QtCore.QSize(400, 100))
        self.picture.setBaseSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.picture.setFont(font)
        self.picture.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.picture.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.picture.setObjectName("picture")
        self.verticalLayout.addWidget(self.picture)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 7, 5)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.line_edit_h1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        self.line_edit_h1.setFont(font)
        self.line_edit_h1.setObjectName("line_edit_h1")
        self.gridLayout.addWidget(self.line_edit_h1, 0, 1, 1, 1)
        self.push_button_h1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.push_button_h1.setMinimumSize(QtCore.QSize(56, 17))
        self.push_button_h1.setMaximumSize(QtCore.QSize(56, 17))
        self.push_button_h1.setBaseSize(QtCore.QSize(56, 17))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_h1.setFont(font)
        self.push_button_h1.setAutoDefault(False)
        self.push_button_h1.setObjectName("push_button_h1")
        self.gridLayout.addWidget(self.push_button_h1, 0, 2, 1, 1)
        self.line_edit_h2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        self.line_edit_h2.setFont(font)
        self.line_edit_h2.setText("")
        self.line_edit_h2.setObjectName("line_edit_h2")
        self.gridLayout.addWidget(self.line_edit_h2, 1, 1, 1, 1)
        self.push_button_h2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.push_button_h2.setMinimumSize(QtCore.QSize(56, 17))
        self.push_button_h2.setMaximumSize(QtCore.QSize(56, 17))
        self.push_button_h2.setBaseSize(QtCore.QSize(56, 17))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_h2.setFont(font)
        self.push_button_h2.setObjectName("push_button_h2")
        self.gridLayout.addWidget(self.push_button_h2, 1, 2, 1, 1)
        self.label_h1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_h1.setFont(font)
        self.label_h1.setScaledContents(False)
        self.label_h1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_h1.setIndent(-1)
        self.label_h1.setObjectName("label_h1")
        self.gridLayout.addWidget(self.label_h1, 0, 0, 1, 1)
        self.label_h2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_h2.setFont(font)
        self.label_h2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_h2.setObjectName("label_h2")
        self.gridLayout.addWidget(self.label_h2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plain_text_edit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plain_text_edit.setMinimumSize(QtCore.QSize(332, 80))
        self.plain_text_edit.setMaximumSize(QtCore.QSize(300, 80))
        self.plain_text_edit.setBaseSize(QtCore.QSize(300, 80))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.plain_text_edit.setFont(font)
        self.plain_text_edit.setObjectName("plain_text_edit")
        self.horizontalLayout.addWidget(self.plain_text_edit)
        self.push_button_go = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.push_button_go.setMinimumSize(QtCore.QSize(56, 56))
        self.push_button_go.setMaximumSize(QtCore.QSize(56, 56))
        self.push_button_go.setBaseSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.push_button_go.setFont(font)
        self.push_button_go.setDefault(False)
        self.push_button_go.setFlat(False)
        self.push_button_go.setObjectName("push_button_go")
        self.horizontalLayout.addWidget(self.push_button_go)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hash - Checker"))
        self.push_button_h1.setText(_translate("MainWindow", "Browse"))
        self.push_button_h2.setText(_translate("MainWindow", "Browse"))
        self.label_h1.setText(_translate("MainWindow", "Hash 1"))
        self.label_h2.setText(_translate("MainWindow", "Hash 2"))
        self.push_button_go.setText(_translate("MainWindow", "GO!"))