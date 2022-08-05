# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\view.ui'
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
        self.centralwidget.setSizeIncrement(QtCore.QSize(400, 300))
        self.centralwidget.setBaseSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_logo = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_logo.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_logo.setObjectName("widget_logo")
        self.verticalLayout.addWidget(self.widget_logo)
        self.gridLayout_input = QtWidgets.QGridLayout()
        self.gridLayout_input.setVerticalSpacing(4)
        self.gridLayout_input.setObjectName("gridLayout_input")
        self.label_h1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_h1.setObjectName("label_h1")
        self.gridLayout_input.addWidget(self.label_h1, 1, 0, 1, 1)
        self.lineEdit_h1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_h1.setObjectName("lineEdit_h1")
        self.gridLayout_input.addWidget(self.lineEdit_h1, 1, 1, 1, 1)
        self.pushButton_h1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_h1.setObjectName("pushButton_h1")
        self.gridLayout_input.addWidget(self.pushButton_h1, 1, 2, 1, 1)
        self.label_h2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_h2.setObjectName("label_h2")
        self.gridLayout_input.addWidget(self.label_h2, 2, 0, 1, 1)
        self.lineEdit_h2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_h2.setObjectName("lineEdit_h2")
        self.gridLayout_input.addWidget(self.lineEdit_h2, 2, 1, 1, 1)
        self.pushButton_h2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_h2.setObjectName("pushButton_h2")
        self.gridLayout_input.addWidget(self.pushButton_h2, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_input)
        self.horizontalLayout_output = QtWidgets.QHBoxLayout()
        self.horizontalLayout_output.setSpacing(4)
        self.horizontalLayout_output.setObjectName("horizontalLayout_output")
        self.plainTextEdit_output = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_output.setMinimumSize(QtCore.QSize(0, 90))
        self.plainTextEdit_output.setMaximumSize(QtCore.QSize(300, 119))
        self.plainTextEdit_output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plainTextEdit_output.setObjectName("plainTextEdit_output")
        self.horizontalLayout_output.addWidget(self.plainTextEdit_output)
        self.verticalLayout_go_about = QtWidgets.QVBoxLayout()
        self.verticalLayout_go_about.setObjectName("verticalLayout_go_about")
        self.pushButton_go = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_go.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_go.setFont(font)
        self.pushButton_go.setObjectName("pushButton_go")
        self.verticalLayout_go_about.addWidget(self.pushButton_go)
        self.pushButton_about = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_about.setMaximumSize(QtCore.QSize(71, 16777215))
        self.pushButton_about.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout_go_about.addWidget(self.pushButton_about)
        self.horizontalLayout_output.addLayout(self.verticalLayout_go_about)
        self.verticalLayout.addLayout(self.horizontalLayout_output)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hash - Checker"))
        self.label_h1.setText(_translate("MainWindow", "Hash 1"))
        self.pushButton_h1.setText(_translate("MainWindow", "Browse"))
        self.label_h2.setText(_translate("MainWindow", "Hash 2"))
        self.pushButton_h2.setText(_translate("MainWindow", "Browse"))
        self.pushButton_go.setText(_translate("MainWindow", "GO!"))
        self.pushButton_about.setText(_translate("MainWindow", "About"))
