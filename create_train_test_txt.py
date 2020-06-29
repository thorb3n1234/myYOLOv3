import os
import sys


a = open("config/train.txt", "w")
for file in os.listdir("../daten/ML_DATA/data/data/train/"):
	if file.endswith('.jpg'):
		a.write("../daten/ML_DATA/data/data/train/"+ str(file) + os.linesep)
		#a.write("../GIT_DATA/ML_DATA/data/data/train/"+ str(file) + os.linesep)

a.close()

b = open("config/test.txt", "w")
for file in os.listdir("../daten/ML_DATA/data/data/test/"):
	if file.endswith('.jpg'):
		b.write("../daten/ML_DATA/data/data/train/"+ str(file) + os.linesep)
		#b.write("../GIT_DATA/ML_DATA/data/data/test/"+ str(file) + os.linesep)
b.close()

