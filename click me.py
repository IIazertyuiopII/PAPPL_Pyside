# -*- coding: utf-8 -*-
import os;
import subprocess;

listedir = os.listdir(".")
uilist = [i for i in listedir if ".ui" in i]
reslist = [j for j in listedir if ".qrc" in j]


for i in uilist :
	subprocess.call("pyside-uic "+str(i)+" > "+str(i[:-2])+"py",shell=True)

for j in reslist :
	subprocess.call("pyside-rcc -py3 "+str(j)+" -o "+str(j[:-3])+"py",shell=True)

subprocess.call("python testqt.py",shell=True)