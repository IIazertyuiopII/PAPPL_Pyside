import pickle
import os
import copy

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



def saveConf(string):
	with open(string,rwb) as dump:
		if os.path.isfile(string):
			if pickle.load(string).name != conf.name:
				error = "fichier deja existant, ecraser ?"
				return
		pickle.dump(conf, dump)




