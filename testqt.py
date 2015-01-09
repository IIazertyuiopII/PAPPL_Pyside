import sys
 
import PySide
from PySide.QtGui import *
from PySide.QtCore import *
from entrée_données import Ui_MainWindow
from ok import Ui_GroupBox

 
class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        	
        #self.grpbox = ok(self)
        #self.grpbox.move(1000,500)

        #self.lineEdit.textEdited.connect(self.textchange)
        #event bindings

  def save(self):
        print ("saved")

  def load(self):
        print ("loaded")
  def textchange(self):
  		print("textchanged")
  		print(self.lineEdit.text())       
     

#class ok(QGroupBox, Ui_GroupBox):
#	def __init__(self,parent):
#		super(ok, self).__init__(parent)
#		self.setupUi(self)

       
app = QApplication(sys.argv)
frame = MainWindow()
frame.show()
app.exec_()
    
