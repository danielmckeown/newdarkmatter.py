import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # for unequal plot boxes
from scipy.optimize import curve_fit
import pandas as pd
import sqlite3
import csv
# Create Python Data Frame to store data for publication

df = pd.DataFrame(columns=('n', 'nerror', 'a','aerror','r0','r0error','id','dm halo mass','redshift','descendant','progenitor','parenthalo'))

exampleFile00 = open('listofhalos.txt')
exampleFile0 = open('listofradii.txt')
exampleFile2 = open('mass_at_radii.txt')

exampleReader00 = csv.reader(exampleFile00)
exampleReader0 = csv.reader(exampleFile0)
exampleReader2 = csv.reader(exampleFile2)


y111 = list(exampleReader00)

r111 = list(exampleReader0)
# parenthalos is the final list

listdm = list(exampleReader2)

##### PARENT HALO FILE

parenthalos = []
parenthalo = open('parenthalos.txt','r')
for y in parenthalo.read().split('\n'):
	if y.isdigit():
		parenthalos.append(int(y))




###### DM MASS FILE

dm_mass = open('darkmattermass.txt')

dm_masses =  [elem.strip().split(';') for elem in dm_mass]

dm_masser = list(dm_masses)
dm_masse = [val for sublist in dm_masser for val in sublist]
dm_mass = [float(i) for i in dm_masse]



###### DESCENDANT FILE

descendants = []
descendant = open('descendant.txt','r')
for y in descendant.read().split('\n'):
	if y.isdigit():
		descendants.append(int(y))



#### PROGENITOR FILE


progenitor = []
progs = open('progenitor.txt','r')
for y in progs.read().split('\n'):
	if y.isdigit():
		progenitor.append(int(y))



#### Redshift File



red = open( "redshift.txt")

reds =  [elem.strip().split(';') for elem in red]

redder = list(reds)
redd = [val for sublist in redder for val in sublist]
redshift = [float(i) for i in redd]





##### Halo File



halo_id = []
halos = open('halo_id.txt','r')
for y in halos.read().split('\n'):
	if y.isdigit():
		halo_id.append(int(y))



g = len(r111)

#flattened = [val for sublist in list_of_lists for val in sublist]
# HEre  I use a list comprehension


y11 =[val for sublist in y111 for val in sublist]

r11 = [val for sublist in r111 for val in sublist]

list_dm = [val for sublist in listdm for val in sublist]

nm = 0

while nm < g:

	exampleFile = open(y11[nm])
	exampleReader = csv.reader(exampleFile)
	y1 = list(exampleReader)


	exampleFile1 = open(r11[nm])
	exampleReader1 = csv.reader(exampleFile1)
	r1 = list(exampleReader1)


	exampleFile2 = open(list_dm[nm])
	exampleReader2 = csv.reader(exampleFile2)
	total_dm_mass1 = list(exampleReader2)

	x = 0

	y2 = []



	while x < len(y1):
		mew = ''.join(y1[x])
	
		y2.insert(x,mew)
		x = x + 1

	y3 = map(float,y2)
	
	x1 = 0

	r2 = []

	while x1 < len(r1):
		mew1 = ''.join(r1[x1])
	
		r2.insert(x1,mew1)
		x1 = x1 + 1

	total_dm_mass2 = []

	x2 = 0
	
	while x2 < len(total_dm_mass1):
		mew2 = ''.join(total_dm_mass1[x2])
	
		total_dm_mass2.insert(x2,mew2)
		x2 = x2 + 1
	
	total_dm_mass = map(float,total_dm_mass2)
	y3 = map(float,y2)

	r3 = map(float,r2)		

	e1 = np.multiply(0.3, y3)

#### NON LINEAR REGRESSION PORTION OF THE PROGRAM



	def line(r, a, r0 , n):
		#r00 = (r/(r0*1000))**2
	    
	
		#return a * r**-n * (1.0 + r/r0)**(-3.0 + n)
		return a*np.exp(-(r/r0)**n)

	param_bounds=([-np.inf,-np.inf,0],[np.inf,np.inf,2])
		
	popt, pcov = curve_fit(line, r3, y3, sigma = e1, p0=[10.,10.,2.],bounds=param_bounds)

# Here the data is inserted into the data frame
	df.loc[nm] = [ popt[2] ,pcov[2,2]**0.5,popt[0],pcov[0,0]**0.5,popt[1],pcov[1,1]**0.5,halo_id[nm],dm_mass[nm],redshift[nm],descendants[nm],progenitor[nm],parenthalos[nm]]
		
	fig, ax1 = plt.subplots()
	
	axes = plt.gca()
	axes.set	
	rfine = np.linspace(1, 800, 150)  # define values to plot the function for
	plt.errorbar(r3, y3, yerr=e1, fmt= "none")
	ax1.loglog(rfine, line(rfine, popt[0], popt[1],popt[2]), 'r-')
	ax1.set_xlabel('Radius kpc')
# Make the y-axis label, ticks and tick labels match the line color.
	ax1.set_ylabel('density', color='b')
	ax1.tick_params('y', colors='b')
	plt.xlabel('Radius kpc')
	plt.ylabel('Dark Matter Density 10^10 Msolar /kpc^3')
		
	
	ax2 = ax1.twinx()

	ax2.plot(r3,total_dm_mass, 'r.')
	ax2.set_ylabel('Dark Matter Mass 10^10 Msolar', color='r')
	ax2.tick_params('y', colors='r')
	plt.title('Dark Matter Density of halo %s at Redshift %s'%(halo_id[nm],redshift[nm]))
	plt.show()
		
	nm = nm + 1

	



