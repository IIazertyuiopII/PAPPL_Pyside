# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bil.ui'
#
# Created: Fri Jan 16 08:36:52 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(374, 144)
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
"    color : black;\n"
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
"")
        GroupBox.setTitle("")
        self.label_4 = QtGui.QLabel(GroupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label_4.setObjectName("label_4")
        self.taille = QtGui.QLabel(GroupBox)
        self.taille.setGeometry(QtCore.QRect(60, 10, 67, 21))
        self.taille.setObjectName("taille")
        self.label_6 = QtGui.QLabel(GroupBox)
        self.label_6.setGeometry(QtCore.QRect(140, 10, 21, 21))
        self.label_6.setObjectName("label_6")
        self.number = QtGui.QLabel(GroupBox)
        self.number.setGeometry(QtCore.QRect(160, 10, 67, 21))
        self.number.setObjectName("number")
        self.eq = QtGui.QLabel(GroupBox)
        self.eq.setGeometry(QtCore.QRect(10, 40, 67, 21))
        self.eq.setObjectName("eq")
        self.conc = QtGui.QLabel(GroupBox)
        self.conc.setGeometry(QtCore.QRect(10, 70, 221, 21))
        self.conc.setObjectName("conc")
        self.suppr = QtGui.QPushButton(GroupBox)
        self.suppr.setGeometry(QtCore.QRect(10, 100, 61, 31))
        self.suppr.setObjectName("suppr")
        self.mod = QtGui.QPushButton(GroupBox)
        self.mod.setGeometry(QtCore.QRect(90, 100, 61, 31))
        self.mod.setObjectName("mod")
        self.der = QtGui.QPushButton(GroupBox)
        self.der.setGeometry(QtCore.QRect(160, 100, 61, 31))
        self.der.setObjectName("der")

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QtGui.QApplication.translate("GroupBox", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("GroupBox", "Taille", None, QtGui.QApplication.UnicodeUTF8))
        self.taille.setText(QtGui.QApplication.translate("GroupBox", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("GroupBox", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.number.setText(QtGui.QApplication.translate("GroupBox", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.eq.setText(QtGui.QApplication.translate("GroupBox", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.conc.setText(QtGui.QApplication.translate("GroupBox", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.suppr.setText(QtGui.QApplication.translate("GroupBox", "Suppr.", None, QtGui.QApplication.UnicodeUTF8))
        self.mod.setText(QtGui.QApplication.translate("GroupBox", "Modif", None, QtGui.QApplication.UnicodeUTF8))
        self.der.setText(QtGui.QApplication.translate("GroupBox", "Dériv", None, QtGui.QApplication.UnicodeUTF8))

