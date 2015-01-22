import pickle
import os
import copy

class Produit:
	nm = []
	def __init__(self,conc):
		self.diffusivity = conc[0]
		self.decay = conc[1]
		self.num = 0
		while self.num in Produit.nm:
			self.num += 1
		Produit.nm.append(self.num)
	def getDescription(self):
		return [str(self.num),str(self.diffusivity),str(self.decay)]
	def __str__(self):
		return "Produit " + str(self.num) + " Df : " + str(self.diffusivity) + "Dc : " + str(self.decay)

	def __del__(self):
		Produit.nm.remove(self.num)

class Bille:
	#id = 0 
	nm = []
	def __init__(self,equation,size,count,conc):
		self.eq = equation
		self.size = size
		self.conc = conc
		self.count = count
		self.num = 0
		while self.num in Produit.nm:
			self.num += 1
		Produit.nm.append(self.num)	
	def parseur(self):
		pass
	def getEquation(self):
		pass
	def getSize(self):
		pass
	def __str__(self):
		return "Bille " + str(self.num) + " Size : " + str(self.size) + "\nEq : " + self.eq + "\nConc : " + str(self.conc)
	def getDescription(self):
		return [str(self.num),str(self.size),str(self.eq),str(self.count),str(self.conc)]


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




