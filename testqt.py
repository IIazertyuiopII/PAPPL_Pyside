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

        self.conf = beads.Configuration("default")

        self.b_charger_2.clicked.connect(self.addProduct)
        self.b_charger_4.clicked.connect(self.addBille)
        self.spinBox.valueChanged.connect(self.majOptions)
        self.spinBox_2.valueChanged.connect(self.majOptions)
        self.spinBox_3.valueChanged.connect(self.majOptions)

        self.b_charger.clicked.connect(self.load)
        self.b_sauver.clicked.connect(self.save)


  def save(self):

    string, _  = QFileDialog().getOpenFileName(self, 'Sauvegarder fichier', '~')

    with open(string,rwb) as dump:
      if os.path.isfile(string):
        if pickle.load(string).name != self.conf.name:
          error = "fichier deja existant, ecraser ?"
          return
      pickle.dump(self.conf, dump)

  def load(self):

      string, _  = QFileDialog().getOpenFileName(self, 'Ouvrir fichier', '~')
      if not string:
        return
      c1 = copy.deepcopy(self.conf)
      try:
        self.conf=pickle.load(string)
      except (pickle.UnpicklingError,ValueError) as err :
        if 'c1' in locals():
          self.conf = c1
        error = err
      if type(self.conf) != Configuration:
        err = "Fichier incompatible"
      del self.conf
      #Si tout va bien on affiche

  def textchange(self):
  		print("textchanged")
  		print(self.lineEdit.text())

  def majOptions(self):
      self.conf.opt = beads.Option(self.spinBox.value(),self.spinBox_2.value(),self.spinBox_3.value())

  def addProduct(self):
      self.conf.produits.append(beads.Produit(self.lineEdit.text(),self.lineEdit_2.text()))
      np = len(self.conf.produits)-1
      self.label_3.setText(str(np+1) + " Produits")

      tmp = ok(self,params=self.conf.produits[np].getDescription())
      tmp.modif.connect(self.modifyProduct)
      self.verticalLayout_2.insertWidget(0,tmp,stretch=1)

      self.lineEdit.setText("")
      self.lineEdit_2.setText("")

  def modifyProduct(self,k):

      for i in self.conf.produits :
        if i.num == k:
         self.lineEdit.setText(i.diffusivity)
         self.lineEdit_2.setText(i.decay)
         self.verticalLayout_2.takeAt(k)
         del i
         break

  def addBille(self):
    conc = [self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text(),self.lineEdit_9.text()]
    self.conf.billes.append(beads.Bille(self.lineEdit_3.text(),self.lineEdit_4.text(),conc))
    nb = len(self.conf.billes)-1

    self.verticalLayout_5.insertWidget(0,ok(self,params=self.conf.billes[nb].getDescription()))
    self.label_7.setText(str(nb+1) + " billes")

def mapAlphabet(k):
  k = int(k)
  c = {0:'A :',1:'B :',2:'C :',3:'D :',4:'E :',5:'F :'}
  if k in c:
    return c[k]
  else:
    return 'erreur'


class ok(QGroupBox, Ui_GroupBox):

  modif = Signal(int)

  def __init__(self,parent,params):
    super(ok, self).__init__(parent)
    self.setupUi(self)
    self.label.setText(mapAlphabet(params[0]))
    self.label_3.setText(params[1])
    self.label_2.setText(params[2])
    self.toolButton.clicked.connect(self.c)

  def c(self):
    self.modif.emit(int(self.label.text()))

app = QApplication(sys.argv)
frame = MainWindow()
frame.show()
app.exec_()
    
