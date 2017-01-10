import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # for unequal plot boxes
from scipy.optimize import curve_fit
import pandas as pd


import csv

exampleFile00 = open('listofhalos.txt')
exampleFile0 = open('listofradii.txt')

exampleReader00 = csv.reader(exampleFile00)
exampleReader0 = csv.reader(exampleFile0)

y111 = list(exampleReader00)

r111 = list(exampleReader0)

g = len(r111)


#flattened = [val for sublist in list_of_lists for val in sublist]
# HEre  I use a list comprehension


y11 =[val for sublist in y111 for val in sublist]

r11 = [val for sublist in r111 for val in sublist]


print y11
print r11

nm = 0

while nm < g:
	print y11[0]
	print r11[0]



	print y11[nm]
	print r11[nm]
	exampleFile = open(y11[nm])
	exampleReader = csv.reader(exampleFile)
	y1 = list(exampleReader)
	print len(y1)

	exampleFile1 = open(r11[nm])
	exampleReader1 = csv.reader(exampleFile1)
	r1 = list(exampleReader1)


	print len(y1)

	print len(r1)

	x = 0

	y2 = []



