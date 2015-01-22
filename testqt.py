# -*- coding: utf-8 -*-
import time
import sys
sys.path.append(".")
import beads
import threading
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

        self.initScrollAreas()

  def save(self):

    string, _  = QFileDialog().getSaveFileName(self, 'Save file', '')

    if not string:
      return

    self.export("save")

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

  def export(self,name):
    exp = open(name+"_export",'w')
    exp.write("Diffusivity_Beads " + str(self.conf.produits[0].diffusivity)+"\n")
    exp.write("Diffusivity_Chemi " + str(self.conf.produits[0].diffusivity)+"\n")
    exp.write("Decay_k " + str(self.conf.produits[0].decay)+"\n")
    exp.write("BeadSize " + str(self.conf.billes[0].size)+"\n")
    exp.write("TotalSteps " + str(self.conf.opt.nombrePas)+"\n")
    exp.write("NumProd " + str(len(self.conf.produits) )+"\n")
    exp.write("sx " + str(self.conf.opt.sizeArena)+"\n")
    exp.write("sy " + str(self.conf.opt.sizeArena)+"\n")
    exp.write("world "+name+"_export_world"+"\n")
    exp.close
    world = open(name+"_export_world",'w')
    for j,i in enumerate(self.conf.billes):
      world.write("ball " + str(j)+"\n")
      world.write("rand "+"\n")
      world.write(str(i.count)+"\n")
      world.write(i.eq+"\n")
      world.write("10 0"+"\n")
      world.write(str(i.conc)+"\n")



  def load(self):

      string, _  = QFileDialog().getOpenFileName(self, 'Open file', '')


      if not string:
        return

      string = open(string,"rb")

      try:
        loaded=pickle.load(string)
        print(type(loaded))
        # if type(loaded) == beads.Configuration :
        self.conf = loaded
        self.displayConf()
         #else:
         #  raise ValueError

      except (pickle.UnpicklingError,ValueError):
        c=QMessageBox(self)
        c.setText("Fichier incompatible ou corrompu.")
        c.exec_()

  def displayConf(self):
    a,b,c = self.conf.opt.nombrePas, self.conf.opt.sizeArena, self.conf.opt.OneEveryN
    self.spinBox.setValue(a)
    self.spinBox_2.setValue(b)
    self.spinBox_3.setValue(c)
    #Comme setValue va emettre valueChange et écraser opt, on sauvegarde d'abords les values

    for i in range(int(self.verticalLayout_2.count())):
      self.verticalLayout_2.takeAt(0)

    for i in self.conf.produits:
      tmp = ok(self,params=i.getDescription())
      tmp.modif.connect(self.modifyProduct)
      self.verticalLayout_2.insertWidget(0,tmp,stretch=1)

    np = len(self.conf.produits)
    self.label_3.setText(str(np+1) + " Products")

    for i in range(int(self.verticalLayout_5.count())):
      self.verticalLayout_5.takeAt(0)

    for i in self.conf.billes:
      tmp = bil(self,params=i.getDescription())
      tmp.editP.connect(self.modifBille)
      self.verticalLayout_5.insertWidget(0,tmp,stretch=1)

    np = len(self.conf.billes)
    self.label_7.setText(str(np+1) + " Products")

  def initScrollAreas(self):
    self.scrollarea_1 = QScrollArea(self.groupBox_6)
    scrollarea_1_widget = QWidget(self)
    self.verticalLayout_2 = QVBoxLayout()
    self.verticalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
    scrollarea_1_widget.setLayout(self.verticalLayout_2)
    self.scrollarea_1.setWidgetResizable(True)
    self.scrollarea_1.setWidget(scrollarea_1_widget)
    self.scrollarea_1.setVisible(True)
    self.scrollarea_1.resize(280,350)
    self.scrollarea_1.setViewportMargins(10,10,10,20)

    self.scrollarea_2 = QScrollArea(self.groupBox_7)
    scrollarea_2_widget = QWidget(self)
    self.verticalLayout_5 = QVBoxLayout()
    self.verticalLayout_5.setSizeConstraint(QLayout.SetMinAndMaxSize)
    scrollarea_2_widget.setLayout(self.verticalLayout_5)
    self.scrollarea_2.setWidgetResizable(True)
    self.scrollarea_2.setWidget(scrollarea_2_widget)
    self.scrollarea_2.setVisible(True)
    self.scrollarea_2.resize(285,571)
    self.scrollarea_2.setViewportMargins(10,10,10,20)

  def majOptions(self):
    #hgv
      self.conf.opt = beads.Option(self.spinBox.value(),self.spinBox_2.value(),self.spinBox_3.value())

  def addProduct(self):
      np = len(self.conf.produits)-1

      if(np<=5) :
        conc = [self.lineEdit.text(),self.lineEdit_2.text()]
        if(checkOneParamMissing(conc)==False) :
          tmp = beads.Produit(conc)
          print(tmp)
          self.conf.produits.append(tmp)
          self.label_3.setText(str(np+2) + " Products")

          tmp = ok(self,params=tmp.getDescription())
          tmp.modif.connect(self.modifyProduct)
          tmp.delet.connect(self.deleteProduct)
          self.verticalLayout_2.insertWidget(0,tmp,stretch=1)

          self.lineEdit.setText("")
          self.lineEdit_2.setText("")
        else :
          wrongInputAnimation(self.groupBox_4)

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

    self.label_3.setText(str(len(self.conf.produits)) + " Products")

  def deleteProduct(self,num):
    for i in range(self.verticalLayout_2.count()):

      if(type(self.verticalLayout_2.itemAt(i))==QSpacerItem) :
        continue
      
      if str(self.verticalLayout_2.itemAt(i).widget().num) == str(num) :
        selectedItem = self.verticalLayout_2.takeAt(i).widget()
        selectedItem.deleteLater()
        for j in self.conf.produits:
          if j.num == num :
            self.conf.produits.pop(self.conf.produits.index(j))
            break
        break
    self.label_3.setText(str(len(self.conf.produits)) + " Products")

  def addBille(self):
    conc = [self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text(),self.lineEdit_9.text()]
    con = list(conc)
    con.extend([self.lineEdit_3.text(),self.lineEdit_4.text()])
    if(checkOneParamMissing(con)==False) :

      self.conf.billes.append(beads.Bille(self.lineEdit_4.text(),self.lineEdit_10.text(),self.lineEdit_3.text(),conc))
      nb = len(self.conf.billes)-1
      self.label_7.setText(str(nb+1) + " Beads")


      tmp = bil(self,params=self.conf.billes[nb].getDescription())
      tmp.deriv.connect(self.modifBille)
      tmp.copyP.connect(self.copyBille)
      tmp.editP.connect(self.editBille)

      self.verticalLayout_5.insertWidget(0,tmp,stretch=1)
      self.lineEdit_10.setText("")
      self.lineEdit_5.setText("")
      self.lineEdit_6.setText("")
      self.lineEdit_7.setText("")
      self.lineEdit_8.setText("")
      self.lineEdit_9.setText("")
      self.lineEdit_3.setText("")
      self.lineEdit_4.setText("")
    else :
      wrongInputAnimation(self.groupBox_5)

  def modifBille(self,num):
    for i in range(self.verticalLayout_5.count()):
      if(type(self.verticalLayout_2.itemAt(i))==QSpacerItem) :
        continue

      if str(self.verticalLayout_5.itemAt(i).widget().num) == str(num) :
        for j in self.conf.billes:
          if j.num == num :
            c = self.conf.billes.pop(self.conf.billes.index(j))
            break
        selectedItem = self.verticalLayout_5.takeAt(i).widget()
        selectedItem.deleteLater()
        break
    self.label_7.setText(str(len(self.conf.billes)) + " Beads")

  def copyBille(self,num):
    for i in range(self.verticalLayout_5.count()):
      if(type(self.verticalLayout_2.itemAt(i))==QSpacerItem) :
        continue

      if str(self.verticalLayout_5.itemAt(i).widget().num) == str(num) :
        for j in self.conf.billes:
          print(" j : %d ==> num : %d", j.num,num)
          if str(j.num) == str(num) :
            c = self.conf.billes[self.conf.billes.index(j)]
            break
        selectedItem = self.verticalLayout_5.itemAt(i).widget()
        self.lineEdit_10.setText(selectedItem.taille.text())
        self.lineEdit_3.setText(selectedItem.number.text())
        self.lineEdit_4.setText(selectedItem.eq.text())
        self.lineEdit_5.setText(c.conc[0])
        self.lineEdit_6.setText(c.conc[1])
        self.lineEdit_7.setText(c.conc[2])
        self.lineEdit_8.setText(c.conc[3])
        self.lineEdit_9.setText(c.conc[4])
        break

  def editBille(self,num):
    for i in range(self.verticalLayout_5.count()):
      if(type(self.verticalLayout_2.itemAt(i))==QSpacerItem) :
        continue

      if str(self.verticalLayout_5.itemAt(i).widget().num) == str(num) :
        for j in self.conf.billes:
          if str(j.num) == str(num) :
            c = self.conf.billes.pop(self.conf.billes.index(j))
            break
        selectedItem = self.verticalLayout_5.takeAt(i).widget()
        self.lineEdit_10.setText(selectedItem.taille.text())
        self.lineEdit_3.setText(selectedItem.number.text())
        self.lineEdit_4.setText(selectedItem.eq.text())
        self.lineEdit_5.setText(c.conc[0])
        self.lineEdit_6.setText(c.conc[1])
        self.lineEdit_7.setText(c.conc[2])
        self.lineEdit_8.setText(c.conc[3])
        self.lineEdit_9.setText(c.conc[4])
        selectedItem.deleteLater()
        break
    self.label_7.setText(str(len(self.conf.billes)) + " Beads")

  def modifyStylesheetGuiFromMainThread(self,widget,stylesheet) :
    self.findChild(QWidget,widget).setStyleSheet(stylesheet)
    #dkfjg

def printTable(tl):
  tmp = ""
  for i in tl:
    tmp += i
    tmp += " "

def mapAlphabet(k):

  k = int(k)
  c = {0:'A :',1:'B :',2:'C :',3:'D :',4:'E :',5:'F :'}
  if k in c:
    return c[k]
  else:
    return 'error'

def checkOneParamMissing(iterable):
  for i in iterable :
    if(i==""):
      return True
  return False

def wrongInputAnimation(widget):
  
  b = blink()
  b.info.connect(frame.modifyStylesheetGuiFromMainThread)
  threading.Thread(target=b.doblink, args=[widget,3], kwargs={}).start()

class blink(QWidget):

  info = Signal(str,str)

  def doblink(self,widget,n) :
    if n==0 :
      return
    else :
      self.info.emit(widget.objectName(),"#"+widget.objectName()+" {border : 10px solid red;} ")
      time.sleep(0.5)
      self.info.emit(widget.objectName(),"#"+widget.objectName()+" {border : none;} ")
      time.sleep(0.5)
      self.doblink(widget,n-1)    
    
class ok(QGroupBox, Ui_GroupBox):

  modif = Signal(int)
  delet = Signal(int)

  def __init__(self,parent,params):
    super(ok, self).__init__(parent)
    self.setupUi(self)
    self.num = params[0]
    print(self.num)
    self.label.setText(mapAlphabet(params[0]))
    self.label_3.setText(params[1])
    self.label_2.setText(params[2])
    self.toolButton_2.clicked.connect(self.c)
    self.toolButton.clicked.connect(self.d)

  def c(self):
    self.modif.emit(int(self.num))
  def d(self): 
    self.delet.emit(int(self.num))

class bil(QGroupBox, Ui_bil):

  deriv = Signal(int)
  copyP = Signal(int)
  editP = Signal(int)

  def __init__(self,parent,params):
    super(bil, self).__init__(parent)
    self.setupUi(self)
    self.num = params[0]
    self.number.setText(params[3])
    self.taille.setText(params[2])
    self.eq.setText(params[1])
  #  tmp = ""
  #  for i in range(len(params[4])):
  #    tmp += mapAlphabet(i)+" : "+ str(params[4][i])
  #    print(mapAlphabet(i)+" : "+ str(params[4][i]))
    self.conc.setText(params[4])
    self.der.clicked.connect(self.c)
    self.edit.clicked.connect(self.e)
    self.copy.clicked.connect(self.d)

  def c(self):
    self.deriv.emit(int(self.num))
  def d(self):
    self.copyP.emit(int(self.num))
  def e(self):
    self.editP.emit(int(self.num))

app = QApplication(sys.argv)
frame = MainWindow()
frame.show()
app.exec_()
