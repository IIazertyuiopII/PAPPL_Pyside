# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ok.ui'
#
# Created: Thu Jan 22 19:55:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(250, 45)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GroupBox.sizePolicy().hasHeightForWidth())
        GroupBox.setSizePolicy(sizePolicy)
        GroupBox.setMinimumSize(QtCore.QSize(0, 45))
        GroupBox.setMaximumSize(QtCore.QSize(250, 45))
        GroupBox.setBaseSize(QtCore.QSize(231, 45))
        GroupBox.setStyleSheet("#GroupBox{\n"
"\n"
"    border-style : none;\n"
"    border-bottom : 2px solid blue;\n"
"\n"
"}\n"
"\n"
"#groupBox{\n"
"\n"
"    border-radius : 0px;\n"
"    background : #eee;\n"
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
"    color : black;\n"
"\n"
"}\n"
"\n"
"#label_2,#label_3{\n"
"\n"
"    color : #000035;\n"
"    background-color : #b1b3b4;\n"
"\n"
"}\n"
"")
        GroupBox.setTitle("")
        self.label = QtGui.QLabel(GroupBox)
        self.label.setGeometry(QtCore.QRect(11, 7, 31, 30))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(GroupBox)
        self.label_2.setGeometry(QtCore.QRect(105, 7, 41, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(GroupBox)
        self.label_3.setGeometry(QtCore.QRect(55, 7, 41, 30))
        self.label_3.setObjectName("label_3")
        self.groupBox = QtGui.QGroupBox(GroupBox)
        self.groupBox.setGeometry(QtCore.QRect(150, 4, 72, 36))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.toolButton = QtGui.QToolButton(self.groupBox)
        self.toolButton.setGeometry(QtCore.QRect(2, 3, 30, 30))
        self.toolButton.setStyleSheet("#toolButton {\n"
"\n"
"    border-image: url(res/del.png) 0 0 0 0 stretch stretch;\n"
"\n"
"}")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtGui.QToolButton(self.groupBox)
        self.toolButton_2.setGeometry(QtCore.QRect(40, 3, 30, 30))
        self.toolButton_2.setStyleSheet("#toolButton_2 {\n"
"\n"
"    border-image: url(res/edit.png) 0 0 0 0 stretch stretch;\n"
"\n"
"}")
        self.toolButton_2.setText("")
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QtGui.QApplication.translate("GroupBox", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GroupBox", "A : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("GroupBox", "Decay", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GroupBox", "0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("GroupBox", "Diffusivity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GroupBox", "0.000", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setToolTip(QtGui.QApplication.translate("GroupBox", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setToolTip(QtGui.QApplication.translate("GroupBox", "Edit", None, QtGui.QApplication.UnicodeUTF8))

