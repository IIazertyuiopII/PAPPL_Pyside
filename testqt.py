# -*- coding: utf-8 -*-

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
        	
        self.grpbox = ok(self)
        self.grpbox2 = ok(self)
        self.grpbox3 = ok(self)
        self.verticalLayout_2.addWidget(self.grpbox)
        self.verticalLayout_2.addWidget(self.grpbox2)
        self.verticalLayout_2.addWidget(self.grpbox3)

        conf = beads.Configuration("default")

        #self.lineEdit.textEdited.connect(self.textchange)
        #event bindings

        self.b_charger_2.clicked.connect(self.addProduct)
        self.b_charger_4.clicked.connect(self.addBille)
        self.spinBox.valueChanged.connect(self.majOptions)
        self.spinBox_2.valueChanged.connect(self.majOptions)
        self.spinBox_3.valueChanged.connect(self.majOptions)

        self.b_charger.clicked.connect(self.load)
        self.b_sauver.clicked.connect(self.save)



  def save(self):

    #string = QFileDialog()

    with open(string,rwb) as dump:
      if os.path.isfile(string):
        if pickle.load(string).name != conf.name:
          error = "fichier deja existant, ecraser ?"
          return
      pickle.dump(conf, dump)

  def load(self):

    #string = QFileDialog()

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
    #Si tout va bien on affiche

  def textchange(self):
  		print("textchanged")
  		print(self.lineEdit.text())  

  # def modifyProductList(self,np):
  #       self.label_3.setText(str(np) + " Produits")
  #       if np < 2:
  #         self.lineEdit_6.
  #       if np > 3
  #       Desavtiver les partie useless

  def majOptions(self):
      conf.opt = beads.Option(self.spinBox.value(),self.spinBox_2.value(),self.spinBox_3.value())

  def addProduct(self):
      conf.produits.append(Product(self.lineEdit.text(),self.lineEdit_2.text()))
      np = len(conf.produits)-1
      self.label_3.setText(str(np) + " Produits")
      self.verticalLayout_2.add(conf.produits[np])
      

  def addBille(self):
    conc = [self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text(),self.lineEdit_9.text()]
    conf.billes.append(Bille(self.lineEdit_3.text(),self.lineEdit_4.text(),conc))
    nb = len(conf.billes)-1
    self.verticalLayout_5.add(conf.billes[nb])
    self.label_7.setText(str(nb) + " billes")
     

class ok(QGroupBox, Ui_GroupBox):
	def __init__(self,parent):
		super(ok, self).__init__(parent)
		self.setupUi(self)

       
app = QApplication(sys.argv)
frame = MainWindow()
frame.show()
app.exec_()
    
