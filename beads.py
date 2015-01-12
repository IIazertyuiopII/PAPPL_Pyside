import pickle
import os
import copy

class Produit:
	id = 0
	def __init__(self,diffu, deay):
		self.num = Produit.id
		self.diffusivity = diffu
		self.decay = deay
		Produit.id += 1
	def __str__(self):
		return "Produit " + str(self.num) + " Df : " + str(diffusivity) + "Dc : " + str(decay)

class Bille:
	id = 0 
	def __init__(self,equation,size,conc):
		self.eq = equation
		self.size = size
		self.conc = conc
		self.num = Bille.id
		id += 1
	def parseur(self):
		pass
	def getEquation(self):
		pass
	def getSize(self):
		pass
	def __str__(self):
		return "Bille " + str(self.num) + " Size : " + str(self.size) + "\nEq : " + self.eq + "\nConc : " + str(self.conc)


class Option:
	def __init__(self,npas,size,eons):
		self.nombrePas = npas
		self.sizeArena = size
		self.OneEveryN = eons


class Configuration:
	def __init__(self,name):
		self.name = name
		self.opt = Option(10000, 50,10)
		self.billes = []
		self.produits = []




