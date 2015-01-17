# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entree_donnees.ui'
#
# Created: Sat Jan 17 21:03:59 2015
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("#groupBox_3,#groupBox_8,#groupBox_9 {\n"
"\n"
"    background : #2388DB;\n"
"\n"
"}\n"
"\n"
"#groupBox_6,#groupBox_7 {\n"
"\n"
"    border : 10px solid #2388DB;\n"
"    border-bottom-width : 20px;\n"
"    border-bottom-width : 20px;    \n"
"    border-radius : 0px;\n"
"\n"
"}\n"
"\n"
"#label_3,#label_7 {\n"
"\n"
"    padding : 0px 3px;\n"
"    font-size : 16pt;\n"
"    border : 1px solid #a4c7c0;\n"
"    border-bottom-style : none;\n"
"\n"
"}\n"
"\n"
"#label, #label_2 ,#label_8,#label_10,#label_9,#label_11,#label_12,#label_13,#label_14,#label_15,#label_16,#label_17,#label_18,#label_19{\n"
"\n"
"    font-size : 15px;\n"
"    padding : 0px 3px;\n"
"\n"
"}\n"
"\n"
"#label_4,#label_5,#label_6 {\n"
"\n"
"    font-style : italic;\n"
"    color : grey;\n"
"    background : none\n"
"\n"
"}\n"
"\n"
" QListWidget {\n"
"    border : none;\n"
"    background : #00264a;\n"
"    border-bottom-right-radius : 10px;\n"
" }\n"
"\n"
"#frame, #frame_2, #frame_3, #frame_4 {\n"
"\n"
"    background : #505050;\n"
"\n"
"}\n"
"\n"
"#centralwidget,QMainWindow {\n"
"\n"
"    background-color : #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QWidget {\n"
"\n"
"    font-size : 20px;\n"
"\n"
"}\n"
"\n"
".QLabel{\n"
"\n"
"    font-weight : 500;\n"
"    border : none;\n"
"    font-size : 16pt;\n"
"    color : #2388DB;\n"
"    background-color : #eee;\n"
"    \n"
"}\n"
"\n"
".QPushButton{\n"
"    \n"
"    font : 13pt \"Consolas\";\n"
"    border-radius : 0px;\n"
"    padding : 15px;\n"
"    color : #00003B;    \n"
"}\n"
"\n"
".QToolButton{\n"
"\n"
"    background-color : #fecc26;\n"
"    padding : 5px;    \n"
"\n"
"}\n"
"\n"
".QToolButton:pressed{\n"
"\n"
"     border-style :  outset;\n"
"    border-width : 2px;\n"
"    border-color : black;\n"
"    border-left-color:#ccc;\n"
"    border-top-color:#ccc;\n"
"\n"
"}\n"
"\n"
".QGroupBox{\n"
"\n"
"    border-bottom-right-radius : 20px;\n"
"    color : 0040f4;\n"
"    font-weight : 600;\n"
"    border : 0px;\n"
"    background-color : #fff;\n"
"\n"
"}\n"
"\n"
".QLineEdit, .QSpinBox{\n"
"\n"
"    color : #000035;\n"
"    padding : 2px;\n"
"    font-size : 14pt;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, 190, 1621, 16))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(400, 190, 20, 711))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1230, 190, 20, 711))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(820, 190, 20, 711))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 202, 160, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 191, 30))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(840, 202, 160, 30))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1353, 219, 150, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(543, 219, 150, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.b_charger_2 = QtGui.QToolButton(self.centralwidget)
        self.b_charger_2.setGeometry(QtCore.QRect(370, 440, 90, 50))
        self.b_charger_2.setObjectName("b_charger_2")
        self.b_charger_4 = QtGui.QToolButton(self.centralwidget)
        self.b_charger_4.setGeometry(QtCore.QRect(1195, 440, 90, 50))
        self.b_charger_4.setObjectName("b_charger_4")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(274, 30, 1051, 131))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 581, 91))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 30, 131, 20))
        self.label.setToolTip("")
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 131, 20))
        self.label_2.setToolTip("")
        self.label_2.setObjectName("label_2")
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(180, 30, 85, 24))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(500001)
        self.spinBox.setSingleStep(1000)
        self.spinBox.setProperty("value", 100000)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(180, 60, 85, 24))
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(290, 40, 171, 20))
        self.label_8.setToolTip("")
        self.label_8.setObjectName("label_8")
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(470, 40, 85, 24))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(10)
        self.spinBox_3.setSingleStep(1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(690, 20, 311, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 291, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b_charger = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.b_charger.setObjectName("b_charger")
        self.horizontalLayout.addWidget(self.b_charger)
        self.b_sauver = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.b_sauver.setObjectName("b_sauver")
        self.horizontalLayout.addWidget(self.b_sauver)
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(490, 250, 256, 441))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox_6)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 189, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(187, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.groupBox_7 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(1300, 250, 256, 441))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.groupBox_7)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 221, 391))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.groupBox_8 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(20, 260, 331, 401))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_8)
        self.groupBox_4.setGeometry(QtCore.QRect(35, 50, 260, 300))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 131, 20))
        self.label_10.setToolTip("")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 131, 20))
        self.label_9.setToolTip("")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 180, 113, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_9 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(853, 260, 331, 571))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_9)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 50, 250, 471))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_11 = QtGui.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(20, 40, 131, 20))
        self.label_11.setToolTip("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(20, 180, 131, 20))
        self.label_12.setToolTip("")
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 70, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 210, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 290, 113, 24))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_13 = QtGui.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(20, 260, 131, 20))
        self.label_13.setToolTip("")
        self.label_13.setObjectName("label_13")
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 320, 113, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 380, 113, 24))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 350, 113, 24))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(100, 410, 113, 24))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_14 = QtGui.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(40, 290, 51, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtGui.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(40, 320, 51, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(40, 350, 51, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(40, 380, 51, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(40, 410, 51, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtGui.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(20, 110, 131, 20))
        self.label_19.setToolTip("")
        self.label_19.setObjectName("label_19")
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 140, 113, 24))
        self.lineEdit_10.setObjectName("lineEdit_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCharger = QtGui.QAction(MainWindow)
        self.actionCharger.setObjectName("actionCharger")
        self.actionSauver = QtGui.QAction(MainWindow)
        self.actionSauver.setObjectName("actionSauver")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Products", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Global parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Beads", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "145 billes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "1655 Produits", None, QtGui.QApplication.UnicodeUTF8))
        self.b_charger_2.setText(QtGui.QApplication.translate("MainWindow", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.b_charger_4.setText(QtGui.QApplication.translate("MainWindow", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Simulation parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "step number :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Arena size :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "One picture every :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.b_charger.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.b_sauver.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Produit A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Diffusivity :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Decay :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Bille 1 :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Count :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Equation :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Concentrations :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "A ->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "B ->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "C ->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "D ->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "E ->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Size :", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCharger.setText(QtGui.QApplication.translate("MainWindow", "Charger", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSauver.setText(QtGui.QApplication.translate("MainWindow", "Sauver", None, QtGui.QApplication.UnicodeUTF8))

