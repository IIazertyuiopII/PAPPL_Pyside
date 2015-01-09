import pickle
import os

class Produit:
	id = 0
	def __init__(self,diffu, deay):
		self.num = id
		self.diffusivity = diffu
		self.decay = deay
		id += 1

class Bille:
	def __init__(self,equation,size,conc):
		self.eq = equation
		self.size = size
		self.conc = conc
	def parseur(self):
		pass
	def getEquation(self):
		pass
	def getSize(self):
		pass


class Option:
	def __init__(self,npas,size):
		self.nombrePas = npas
		self.sizeArena = size


class Configuration:
	def __init__(self,name):
		self.name = name
		self.opt = Option(10000, 50)
		self.billes = []
		self.produits = []


def loadConf(string):
	if conf:
		c1 = #deepcopy conf
	try:
		conf=pickle.load(string)
		if type(conf) not Configuration:
			conf = c1
			error = "Fichier incompatible"
	except(#Aucune idée) :

def saveConf(string):
	with open(string,rwb) as dump:
		if os.path.isfile(string):
			if pickle.load(string).name != conf.name:
				error = "fichier déjà existant, écraser ?"
				return
		pickle.dump(conf, dump)




