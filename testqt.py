# -*- coding: utf-8 -*-

import sys
sys.path.append(".")
import beads

import PySide
from PySide.QtGui import *
from PySide.QtCore import *
import os,pickle
from entree_donnees import Ui_MainWindow
from ok import Ui_GroupBox
from bil import Ui_GroupBox as Ui_bil 

 
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

    string, _  = QFileDialog().getSaveFileName(self, 'Sauvegarder fichier', '~')

    if not string:
      return

    # if os.path.isfile(string):
    #   with open(string,'rb') as dumpRead:
    #     temp = pickle.load(dumpRead)
    #     if temp.name != self.conf.name:
    #       msgBox = QMessageBox()
    #       msgBox.setText("Save")
    #       msgBox.setInformativeText("Fichier deja existant, ecraser ?")
    #       msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
    #       msgBox.setDefaultButton(QMessageBox.Save)
    #       ret = msgBox.exec_()
    #       dumpRead.close() #Automatiquement liberé après le with, mais bon

    #       if ret == QMessageBox.Cancel:
    #           return

    with open(string,'wb') as dump:
      self.conf.name = string
      pickle.dump(self.conf, dump)

  def load(self):

      string, _  = QFileDialog().getOpenFileName(self, 'Ouvrir fichier', '~')


      if not string:
        return

      string = open(string,"rb")

      try:
        loaded=pickle.load(string)
        if type(loaded) == beads.Configuration :
          self.conf = loaded
          self.displayConf()
        else:
          raise ValueError

      except (pickle.UnpicklingError,ValueError):
        QMessageBox.critical(self, "Fichier incompatible ou corrompu.", Dialog.MESSAGE, QMessageBox.ok)

  def displayConf(self):
    a,b,c = self.conf.opt.nombrePas, self.conf.opt.sizeArena, self.conf.opt.OneEveryN
    self.spinBox.setValue(a)
    self.spinBox_2.setValue(b)
    self.spinBox_3.setValue(c)
    #Comme setValue va emettre valueChange et écraser opt, on sauvegarde d'abords les values

    for i in range(int(self.verticalLayout_2.count())):
      self.verticalLayout_2.takeAt(0)

    for i in self.conf.produits:
      self.addProduct()

    for i in range(int(self.verticalLayout_5.count())):
      self.verticalLayout_5.takeAt(0)

    for i in self.conf.billes:
      self.addProduct(i)

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


    for i in range(self.verticalLayout_2.count()):

      if(type(self.verticalLayout_2.itemAt(i))==QSpacerItem) :
        continue
      
      if str(self.verticalLayout_2.itemAt(i).widget().num) == str(k) :
        selectedItem = self.verticalLayout_2.takeAt(i).widget()
        self.lineEdit.setText(selectedItem.label_3.text())
        self.lineEdit_2.setText(selectedItem.label_2.text())
        selectedItem.deleteLater()
        for j in self.conf.produits:
          if j.num == k :
            self.conf.produits.pop(self.conf.produits.index(j))
            break
        break

  def addBille(self):
    conc = [self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text(),self.lineEdit_9.text()]
    self.conf.billes.append(beads.Bille(self.lineEdit_3.text(),self.lineEdit_4.text(),conc))
    nb = len(self.conf.billes)-1
    self.label_7.setText(str(nb+1) + " billes")


    tmp = bil(self,params=self.conf.billes[nb].getDescription())
    tmp.deriv.connect(self.modifBille)
    self.verticalLayout_5.insertWidget(0,tmp,stretch=1)

    self.lineEdit_5.setText("")
    self.lineEdit_6.setText("")
    self.lineEdit_7.setText("")
    self.lineEdit_8.setText("")
    self.lineEdit_9.setText("")
    self.lineEdit_3.setText("")
    self.lineEdit_4.setText("")

  def modifBille(self,num):
    for i in range(self.verticalLayout_5.count()):
      if str(self.verticalLayout_5.itemAt(i).widget().num) == str(k) :
        for j in self.conf.produits:
          if j.num == k :
            c = self.conf.produits.pop(self.conf.produits.index(j))
            break
        selectedItem = self.verticalLayout_5.takeAt(i).widget()
        self.lineEdit_3.setText(selectedItem.taille.text())
        self.lineEdit_4.setText(selectedItem.eq.text())
        self.lineEdit_5.setText(c.conc[0])
        self.lineEdit_6.setText(c.conc[1])
        self.lineEdit_7.setText(c.conc[2])
        self.lineEdit_8.setText(c.conc[3])
        self.lineEdit_9.setText(c.conc[4])
        selectedItem.deleteLater()
        break

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
    self.num = params[0]
    self.label.setText(mapAlphabet(params[0]))
    self.label_3.setText(params[1])
    self.label_2.setText(params[2])
    self.toolButton.clicked.connect(self.c)

  def c(self):
    self.modif.emit(int(self.num))


class bil(QGroupBox, Ui_bil):

  deriv = Signal(int)

  def __init__(self,parent,params):
    super(bil, self).__init__(parent)
    self.setupUi(self)
    self.num = params[0]
    self.taille.setText(params[1])
    self.eq.setText(params[2])
    self.conc.setText(params[3])
    self.der.clicked.connect(self.c)

  def c(self):
    self.deriv.emit(int(self.num))

app = QApplication(sys.argv)
frame = MainWindow()
frame.show()
app.exec_()
    
