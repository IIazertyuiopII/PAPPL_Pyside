import sys
sys.path.append(".")
import beads

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
    with open(string,rwb) as dump:
      if os.path.isfile(string):
        if pickle.load(string).name != conf.name:
          error = "fichier deja existant, ecraser ?"
          return
      pickle.dump(conf, dump)

  def load(self):
    if 'conf' in locals():
      c1 = copy.deepcopy(conf)
    try:
      conf=pickle.load(string)
    except (pickle.UnpicklingError,ValueError) as err :
      if 'c1' in locals():
        conf = c1
      error = err
    if type(conf) != Configuration:
      err = "Fichier incompatible"
    del conf

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
    
