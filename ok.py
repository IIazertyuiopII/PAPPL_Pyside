# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ok.ui'
#
# Created: Mon Jan 12 09:55:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(187, 35)
        GroupBox.setStyleSheet(".QGroupBox{\n"
"\n"
"    color : white;\n"
"    font-weight : 600;\n"
"    border : 0px;\n"
"    background-color : #00264a;\n"
"\n"
"}\n"
"\n"
".QLabel{\n"
"\n"
"    font-size : 15px;\n"
"    border : 1px solid #a4c7c0;\n"
"    padding : 0px 3px;\n"
"    font-weight : 400;\n"
"    background-color : #0098cc;\n"
"\n"
"}\n"
"\n"
"#label_2,#label_3{\n"
"\n"
"    color : #000035;\n"
"    background-color : #b1b3b4;\n"
"\n"
"}\n"
"\n"
"#toolButton{\n"
"    background-image : url(res/bite.png);\n"
"}")
        GroupBox.setTitle("")
        self.label = QtGui.QLabel(GroupBox)
        self.label.setGeometry(QtCore.QRect(11, 7, 31, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(GroupBox)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(GroupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 41, 16))
        self.label_3.setObjectName("label_3")
        self.toolButton = QtGui.QToolButton(GroupBox)
        self.toolButton.setGeometry(QtCore.QRect(160, 8, 20, 20))
        self.toolButton.setStyleSheet("#toolButton {\n"
"\n"
"    border-image: url(res/bite.png) 0 0 0 0 stretch stretch;\n"
"\n"
"}")
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QtGui.QApplication.translate("GroupBox", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GroupBox", "A : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GroupBox", "0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GroupBox", "0.000", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("GroupBox", "...", None, QtGui.QApplication.UnicodeUTF8))

