# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fun.ui'
#
# Created: Sat Jan 17 21:04:57 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 698)
        MainWindow.setStyleSheet("QWidget {\n"
"\n"
"    font-size : 20px;\n"
"\n"
"}\n"
"\n"
".QLabel{\n"
"\n"
"    font-weight : 400;\n"
"    border : 1px solid #00008B;\n"
"    font-size : 16pt;\n"
"    background-color : #c7eef9;\n"
"    \n"
"}\n"
"\n"
"*[class=\"top\"]{\n"
"\n"
"    font : 13pt \"Consolas\";\n"
"    border-radius : 0px;\n"
"    background-color : #c7eef9;\n"
"    padding : 10px;\n"
"    border-bottom : 1px solid #ccc;\n"
"    color : #00003B;    \n"
"    border-right : 5px solid grey;\n"
"\n"
"}\n"
"\n"
".QPushButton{\n"
"    \n"
"    font : 13pt \"Consolas\";\n"
"    border-radius : 0px;\n"
"    background-color : #c7eef9;\n"
"    padding : 10px;\n"
"    border-bottom : 1px solid #ccc;\n"
"    color : #00003B;    \n"
"\n"
"}\n"
"\n"
".QToolButton{\n"
"\n"
"    background-color : #F6BA3F;\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    padding : 5px;    \n"
"\n"
"}\n"
"\n"
"\n"
".QGroupBox{\n"
"\n"
"    font: 75 16pt \"Buxton Sketch\";\n"
"    border : 2px dot-dot-dash black;\n"
"    border-radius : 20px;\n"
"    background-color : #fff;\n"
"\n"
"}\n"
"\n"
"#label_2{\n"
"\n"
"color : red;\n"
"\n"
"}")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(440, 20, 300, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_2 = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 430, 331, 141))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 50, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 101, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 190, 366, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.first = QtGui.QPushButton(self.verticalLayoutWidget)
        self.first.setMinimumSize(QtCore.QSize(300, 0))
        self.first.setObjectName("first")
        self.horizontalLayout_2.addWidget(self.first)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.first_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.first_2.setObjectName("first_2")
        self.verticalLayout.addWidget(self.first_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 34))
        self.menubar.setObjectName("menubar")
        self.menuHghghghgh = QtGui.QMenu(self.menubar)
        self.menuHghghghgh.setObjectName("menuHghghghgh")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuHghghghgh.addSeparator()
        self.menubar.addAction(self.menuHghghghgh.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("MainWindow", "Sauver", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("MainWindow", "Charger", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Membres", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Nombre de jambes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Nombre de bras", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "betete", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("MainWindow", "bhoufhghg", None, QtGui.QApplication.UnicodeUTF8))
        self.first.setText(QtGui.QApplication.translate("MainWindow", "je ne suis pas un bouton", None, QtGui.QApplication.UnicodeUTF8))
        self.first.setProperty("class", QtGui.QApplication.translate("MainWindow", "top", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setProperty("class", QtGui.QApplication.translate("MainWindow", "top", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setProperty("class", QtGui.QApplication.translate("MainWindow", "top", None, QtGui.QApplication.UnicodeUTF8))
        self.first_2.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHghghghgh.setTitle(QtGui.QApplication.translate("MainWindow", "hghghghgh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("MainWindow", "bite", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))

