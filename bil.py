# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bil.ui'
#
# Created: Sat Jan 17 21:21:43 2015
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(231, 148)
        GroupBox.setStyleSheet("#GroupBox{\n"
"\n"
"    border-style : none;    \n"
"\n"
"}\n"
"\n"
"#groupBox{\n"
"\n"
"    border : 1px solid black;\n"
"    border-radius : 0px;\n"
"\n"
"}\n"
"\n"
".QLabel{\n"
"\n"
"    color : black;\n"
"    font-size : 15px;\n"
"    border : 1px solid #a4c7c0;\n"
"    padding : 0px 3px;\n"
"    font-weight : 400;\n"
"    background-color : #0098cc;\n"
"\n"
"}\n"
"\n"
"#taille,#number,#eq,#conc{\n"
"\n"
"    color : #000035;\n"
"    background-color : #b1b3b4;\n"
"\n"
"}\n"
"")
        GroupBox.setTitle("")
        self.label_4 = QtGui.QLabel(GroupBox)
        self.label_4.setGeometry(QtCore.QRect(11, 10, 51, 30))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtGui.QLabel(GroupBox)
        self.label_6.setGeometry(QtCore.QRect(140, 10, 30, 30))
        self.label_6.setObjectName("label_6")
        self.eq = QtGui.QLabel(GroupBox)
        self.eq.setGeometry(QtCore.QRect(5, 50, 221, 20))
        self.eq.setObjectName("eq")
        self.conc = QtGui.QLabel(GroupBox)
        self.conc.setGeometry(QtCore.QRect(5, 75, 221, 20))
        self.conc.setObjectName("conc")
        self.taille = QtGui.QLabel(GroupBox)
        self.taille.setGeometry(QtCore.QRect(72, 10, 41, 30))
        self.taille.setObjectName("taille")
        self.number = QtGui.QLabel(GroupBox)
        self.number.setGeometry(QtCore.QRect(180, 10, 41, 30))
        self.number.setObjectName("number")
        self.groupBox = QtGui.QGroupBox(GroupBox)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 191, 36))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.der = QtGui.QToolButton(self.groupBox)
        self.der.setGeometry(QtCore.QRect(1, 3, 30, 30))
        self.der.setStyleSheet("#der {\n"
"\n"
"    border-image: url(res/del.png) 0 0 0 0 stretch stretch;\n"
"\n"
"}")
        self.der.setText("")
        self.der.setObjectName("der")
        self.edit = QtGui.QToolButton(self.groupBox)
        self.edit.setGeometry(QtCore.QRect(79, 3, 30, 30))
        self.edit.setStyleSheet("#edit {\n"
"\n"
"    border-image: url(res/edit.png) 0 0 0 0 stretch stretch;\n"
"\n"
"}")
        self.edit.setText("")
        self.edit.setObjectName("edit")
        self.copy = QtGui.QToolButton(self.groupBox)
        self.copy.setGeometry(QtCore.QRect(160, 3, 30, 30))
        self.copy.setStyleSheet("#copy {\n"
"\n"
"    border-image: url(res/copy.png) 0 0 0 0 stretch stretch;\n"
"\n"
"}")
        self.copy.setText("")
        self.copy.setObjectName("copy")

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QtGui.QApplication.translate("GroupBox", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("GroupBox", "Taille :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("GroupBox", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.eq.setText(QtGui.QApplication.translate("GroupBox", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.conc.setText(QtGui.QApplication.translate("GroupBox", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.taille.setText(QtGui.QApplication.translate("GroupBox", "0.000", None, QtGui.QApplication.UnicodeUTF8))
        self.number.setText(QtGui.QApplication.translate("GroupBox", "0.000", None, QtGui.QApplication.UnicodeUTF8))

