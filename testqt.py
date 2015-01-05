import sys
 
import PySide
from PySide.QtGui import *
from PySide.QtCore import *
from fun import Ui_MainWindow
import images

 
class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionSave.triggered.connect(self.save)
        self.actionLoad.triggered.connect(self.load)
        self.toolButton.setDefaultAction(self.actionSave)
        self.toolButton_2.setDefaultAction(self.actionLoad)
        self.actionLoad.setIcon(QIcon(":bite.png"))

        self.lineEdit.textEdited.connect(self.textchange)
        #event bindings

  def save(self):
        print ("saved")

  def load(self):
        print ("loaded")
  def textchange(self):
  		print("textchanged")
  		print(self.lineEdit.text())       
     
       
app = QApplication(sys.argv)
frame = MainWindow()
frame.show()
app.exec_()
    
