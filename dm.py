



###This program will extract data from the Illustris simulation
## and calculate the radial distribution of mass,etc
## using concentric radii 




###  Here I just do some basic initializations 

from scipy.stats import gaussian_kde
import pylab
import matplotlib.pyplot as plt
import h5py
import numpy as np
import requests
def get(path, params=None):
    # make HTTP GET request to path
    headers = {"api-key":"452a77edd4324ec835da440fc3fdc50b "}
    r9 = requests.get(path, params=params, headers=headers)

    # raise exception if response code is not HTTP SUCCESS (200)
    r9.raise_for_status()

    if r9.headers['content-type'] == 'application/json':
        return r9.json() # parse json responses automatically

    if 'content-disposition' in r9.headers:
        filename = r9.headers['content-disposition'].split("filename=")[1]
        with open(filename, 'wb') as f:
            f.write(r9.content)
        return filename # return the filename string

    



import requests
baseUrl = 'http://www.illustris-project.org/api/'
headers = {"api-key":"452a77edd4324ec835da440fc3fdc50b"}



##############################################
####MAIN PROGRAM STARTS HERE


############### This program will track the evolution of the contents of galaxies

########It contains loops which keep track of the url associated with each galaxy





##### it then takes this url and accesses all the data on it


###### in order to calculate the gas, dm,  and star radial density profiles

##### The program then finds power laws associated with these densities. 


#### input an initial id and redshift number. The id will become part of the url
###  This corresponding url contains all the information about each subhalo

### once an initial id is chosen, the loop will go to the next subhalo progenitor from 
## which the last halo evolved, so we can easily track the evolution. In this case
##   I have chosen an id and redshift that is at the very end of the halo evolution, very 
### near to present time, so only 2 halo profiles will be generated, but normally, I can go as far
### back as say snapshot 22  etc.   etc. and generate over 100 profiles for the dark
## matter, star, and gas densities of each galaxy and its corresponding progenitor

id = 2

url = "http://www.illustris-project.org/api/Illustris-2/snapshots/30/subhalos/" + str(id)
sub = get(url) # get json response of subhalo properties
print url
# prepare dict to hold result arrays

fields = ['snap','id','mass_gas','mass_stars','mass_dm','mass_bhs','len_stars','related']
r9 = {}
for field in fields:
	r9[field] = []



# Beginning of loop that runs over all the halos
nM = 0	

radiistring = ([])
densitystring = ([])
filename_list =([])
filename1_list = ([])
while sub['desc_sfid'] != -1:
	for field in fields:
		r9[field].append(sub[field])
		


		
	#print r['mass_stars']   # this is just an example of what I am actually doing here
# request the full subhalo details of the descendant by following the sublink URL
	s = r9['id'][nM]
	sub = get(sub['related']['sublink_descendant'])
	#print len(r['id'])

	t = r9['snap'][nM]
	url1 = "http://www.illustris-project.org/api/Illustris-2/snapshots/" + str(t) + "/subhalos/" + str(s)
	print url1
		
#### This next bit of code contains all the information about the specific redshift corresponding to each halo
###  given a value for t, the code picks out the proper redshift information so that the scale factor
### for each is correct	


	
	###### all the initialized code here
	id1 = s
	print id1
	if t == 19 :
		redshift = 18.789189562448097
		print redshift
	elif t == 20:
	
		redshift = 17.9630246045828
		print redshift
	elif t == 21:
		redshift = 17.0854527855627
		print redshift
	elif t ==  22:
		redshift = 16.248493279904903
	elif t ==  23 :
		redshift = 	15.450266628902101
	elif t ==  24 :
		redshift = 14.7634960164193
	elif t ==  25 :
		redshift = 14.0339921444525
	elif t ==  26 :
		redshift = 13.338248289848599
	elif t ==  27 :
		redshift = 12.6747021048037
	elif t ==  28 :
		redshift = 12.0418635439251
	elif t ==  29 :
		redshift = 11.49738795480349
	elif t ==  30 :
		redshift = 10.919033198155402
	elif t ==  31 :
		redshift = 10.367443572408702
	elif t ==  32 :
		redshift = 9.996590466186328
	elif t ==  33 :
		redshift = 9.84138043947183
	elif t ==  34 :
		redshift = 9.38877127194055
	elif t ==  35 :
		redshift = 9.00233985416247
	elif t ==  36 :
		redshift = 8.907999185598529
	elif t ==  37 :
		redshift = 8.44947629436874
	elif t ==  38 :
		redshift = 8.01217294886593
	elif t == 39 :
		redshift = 7.595107149871599
	elif t ==  40 :
		redshift = 7.23627606616736
	elif t ==  41 :
		redshift = 7.0054170455445295
	elif t == 42 :
		redshift = 6.855117262650801
	elif t ==  43 :
		redshift =  6.491597745667499
	elif t ==  44 :
		redshift = 6.14490120341637
	elif t ==  45 :
		redshift =  6.0107573988449
	elif t ==  46 :
		redshift = 5.846613747881871
	elif t ==  47 :
		redshift = 5.5297658079491
	
	elif t ==  48 :
		redshift = 5.227580973127339
	elif t == 49 :
		redshift =  4.99593346816462
	elif t ==  50 :
		redshift = 4.9393806634910105
	elif t ==  51 :
		redshift = 4.66451770247093
	elif t ==  52 :
		redshift = 4.42803373660555 
	elif t ==  53 :
		redshift =  4.17683491472647
	elif t ==  54 :
		redshift =  4.007945111465269
	elif t ==  55 :
		redshift =  3.93726108472758
	elif t == 56 :
		redshift =  3.70877426464224
	elif t ==  57 :
		redshift =  3.49086136926065
	elif t ==  58 :
		redshift =  3.28303305795652
	elif t ==  59 :
		redshift =  3.0848226358340103
	elif t ==  60 :
		redshift =  3.00813107163038
	elif t ==  61 :
		redshift =  2.89578500572743
	elif t ==  62 :
		redshift =  2.73314261731872
	elif t ==  63 :
		redshift =  2.57729027160189
	elif t ==  64 :
		redshift = 2.44422570455415
	elif t ==  65 :
		redshift = 2.31611074395689
	elif t ==  66 :
		redshift = 2.2079254723837
	elif t ==  67 :
		redshift = 2.10326965259577
	elif t ==  68 :
		redshift = 2.00202813925285
	elif t ==  69 :
		redshift = 	1.90408954353277	
	elif t ==  70 :
		redshift = 	1.82268925262035
	elif t ==  71:
		redshift = 	1.74357057433086
	elif t == 72:
		redshift = 	1.66666955611447
	elif t ==  73 :
		redshift = 	1.60423452207311
	elif t ==  74 :
		redshift = 	1.53123902915761
	elif t ==  75:
		redshift = 	 1.4719748452658
	elif t ==  76 :
		redshift = 	1.4140982203725199
	elif t == 77 :
		redshift = 	1.357576667403
	elif t ==  78 :
		redshift = 	1.30237845990597
	elif t ==  79 :
		redshift = 	1.2484726142451399
	elif t ==  80 :
		redshift = 	1.206258080781
	elif t ==  81 :
		redshift = 	1.1546027123602198
	elif t ==  82 :
		redshift = 	1.11415056376538
	elif t ==  83 :
		redshift = 	1.07445789454767
	elif t ==  84 :
		redshift = 	1.03551044566414
	elif t ==  85 :
		redshift = 	0.9972942257819399
	elif t ==  86 :
		redshift = 	0.987852810815766
	elif t ==  87 :
		redshift = 	0.950531351585033
	elif t ==  88 :
		redshift = 	0.923000816177909
	elif t ==  89 :
		redshift = 	0.886896937575248
	elif t ==  90 :
		redshift = 	0.8514709006246489
	elif t ==  91 :
		redshift = 	0.816709979011851
	elif t ==  92 :
		redshift = 	0.791068248946339
	elif t ==  93 :
		redshift = 	0.7574413726158531
	elif t ==  94 :
		redshift = 	0.732636182022312
	elif t ==  95 :
		redshift =  0.700106353718523	
	elif t ==  96 :
		redshift =  0.676110411213478
	elif t ==  97 :
		redshift = 	0.644641840684537
	elif t ==  98 :
		redshift = 	0.621428745242514
	elif t ==  99 :
		redshift = 	0.598543288187567
	elif t ==  100 :
		redshift = 	0.5759808451078869
	elif t ==  101 :
		redshift = 	0.546392183141022
	elif t ==  102 :
		redshift = 	 0.524565820433923
	elif t ==  103 :
		redshift = 	0.503047523244883
	elif t ==  104 :
		redshift = 	 0.48183294342095095	
	elif t == 105 :
		redshift = 	0.460917794180647	
	elif t ==  106 :
		redshift = 	 0.44029784924774296	
	elif t ==  107 :
		redshift = 	0.41996894199726703			
	elif t ==  108 :
		redshift = 	0.39992696461356303	
	elif t ==  109:
		redshift = 	0.380167867260239
	elif t ==  110:
		redshift = 	0.360687657261817
	elif t ==  111:
		redshift = 	0.34785384185817797	
	elif t ==  112:
		redshift = 	0.32882972420595397	
	elif t == 113:
		redshift = 	0.310074120127834	
	elif t ==  114:
		redshift = 	0.29158323972192396	
	elif t ==  115:
		redshift = 	 0.27335334657844	
	elif t ==  116:
		redshift = 	 0.261343256161012	
	elif t ==  117:
		redshift = 	0.24354018155467003	
	elif t ==  118:
		redshift = 	0.22598838626019802
	elif t == 119 :
		redshift = 	0.21442503551449502	
	elif t ==  120:
		redshift = 	0.19728418237600998	
	elif t ==  121:
		redshift = 	0.18038526170574898	
	elif t ==  122:
		redshift = 	0.16925203324361102	
	elif t ==  123:
		redshift = 	0.15274876890238098	
	elif t ==  124:
		redshift = 	0.141876203969562	
	elif t ==  125:
		redshift = 	0.125759332411261	
	elif t ==  126:
		redshift = 	0.10986994045882499	
	elif t ==  127:
		redshift = 	0.0994018026302219	
	elif t ==  128:
		redshift = 	0.0838844307974793	
	elif t ==  129:
		redshift = 	0.0736613846564387	
	elif t ==  130:
		redshift = 	0.058507322794513	
	elif t ==  131:
		redshift = 	0.048523629981805906	
	elif t ==  132:
		redshift = 	0.0337243718735154	
	elif t ==  133:
		redshift = 	0.0239744283827625
	elif t ==  134:
		redshift = 	0.00952166696794476	
	elif t ==  135:
		redshift = 	2.2204460492503099e-16	
	
	
	
	


	
########################### NORMAL method of SUMMING DM PARTICLES
	import pylab
	import matplotlib.pyplot as plt
	id1 = s
	
	params = {'dm':'Coordinates,SubfindDensity'}
	scale_factor = 1.0 / (1+redshift)          #IMPORTANT NEEDED FOR EACH REDSHIFT
	little_h = 0.704        #IMPORTANT NEEDED FOR EACH REDSHIFT
	sub1 = get(url1) # get json response of subhalo properties
	saved_filename = get(url1 + "/cutout.hdf5",params) # get and save HDF5 cutout file
	fields = ['snap','id','mass_gas','mass_stars','mass_dm','mass_bhs','len_stars']

	little_r = 0    
	big_r = 0.5   #units are kpc
	count = 0 
	radialdmmass_density =([])
	radialdmmass = ([])
	radialdm_distance = ([])
	# rr simply contains all the particle id's associated with the given shell
	
	while (count < 1):
		try:
		
			with h5py.File(saved_filename) as f:
			        dx1 = f['PartType1']['Coordinates'][:,0] - sub1['pos_x']
        			dy1 = f['PartType1']['Coordinates'][:,1] - sub1['pos_y']
        			dz1 = f['PartType1']['Coordinates'][:,2] - sub1['pos_z']
        			dens = np.log10(f['PartType1']['SubfindDensity'][:])
        #masses = f['PartType1']['SubfindDensity'][:]
    				#print "number of dm particles"
        			rr1 = np.sqrt(dx1**2 + dy1**2 + dz1**2)
        			rr1 *= ((scale_factor) / (little_h)) # ckpc/h -> physical kpc  IMPORTANT
        		
        			
        			rrr1 = sorted(rr1)
        			
        			
        			totaldm_masss = len(sorted(rr1)) * 0.0035271
        			
        			#print "now printing totaldm mass"
        			#print totaldm_masss
        			
        			##  Here iter variable is created
        			iter = len(rrr1) / (13) 
        			#print iter
        			
        			remainder = len(rrr1) % (13)
        			#print remainder
        			outer_radius1 = ([])
        			volume = ([])
        			error = ([])			
        			coun = 0
        			
        			
        			while coun < iter:
        				
        				#print "printing iter"
        				
        				#print iter
        				top13 = rrr1[:13]
        				
        				
        				error.insert(iter,np.sqrt(len(top13)))
        				
        				
        				# this inserts the last entry in the list top 50 to get the outer radius
        				outer_radius1.insert(coun,top13[12])
        				#### NOTE: This outer_radius.insert loop keeps looping through and finding the next outer radius corresponding to the location of the next 150 dm particles
        				
        				#print "now printing outer radius"
        				#print outer_radius1
        				
        				totaldmmass = len(top13) *  0.0035271    # 0.0035271 is the mass of each dm particle in the simulation
        				
        				#print rrr1[:150]
        				#"now printing total particles"
        				#print rrr1
        				# was del rrr1[:50]
        				del rrr1[:13]
        				#print "printing new rrr"
        				#print rrr
        				
        				coun = coun + 1
        				#print outer_radius1
        			error.insert(iter,12.24744871391589)
        			
        			
        			#print "now printing last radiii rrr1"
        			#print rrr1[remainder - 1]
        			#### now insert the last outer radii
        			if remainder > 0:
        				outer_radius1.insert(iter,rrr1[remainder - 1])
        			
        			##### now insert the first outer radii
        			outer_radius1.insert(0,0)
        			#print "printing outer_radius of dark matters"
        			#print outer_radius1
        			     			
        			
        			darkmattermass_density = ([])
        			radial_distance1 = ([])
        			
        			
        			
        			#print "now printing outer radius"
        			#print outer_radius1 
        			m = 0
        			darkmass = ([])
        			while m < iter:
         				
        				
        				volume1 = (4.0/3.0)*3.14*((outer_radius1[m + 1])**3) - (4.0/3.0)*3.14*((outer_radius1[m])**3)
        				#print "now printing total DM mass"
        				
        				#print totaldmmass
        				#print "now printing volume1"
        				#print volume1
        				
        			
        				
        				density = totaldmmass / volume1
        				#print "printing densities"
        				#print density
        				
        				darkmattermass_density.insert(m,density)
        				#print darkmattermass_density
        				
        				radial_distance1.insert(m,outer_radius1[m + 1])	
        				
        				m = m + 1
        				darkmass.insert(m,totaldmmass)
        
    				lastmass = remainder * 0.0035271
        			radialdm_distance.insert(count,big_r)
        			if remainder > 0 :
        				volume2 = (4.0/3.0)*3.14*((outer_radius1[m + 1])**3) - (4.0/3.0)*3.14*((outer_radius1[m])**3)
        			
        				final_density = lastmass / volume2
        				darkmattermass_density.insert(m,final_density)
        		
        			little_r = little_r + 0.5    
        			big_r = big_r + 0.5 #units are kpc
        			count = count + 1
					
		except KeyError:
			break

		
		y1 =  darkmattermass_density 
		
		
		
		r1 = outer_radius1
	
		
	

		
#  these two lists y11 and r11 are not really relevant to the fit, they are declared data that was 
# successfully fit whereas the actually data we try to fit comes from r1 and y1 above
# which is generated for each halo that is taken
		
	
		
		
		filename = "darkmatterdensityhalo" + str(s) + "redshift" + str(t) + ".txt" 
		
		filename1 = "darkmatterradii" + str(s) + "redshift" + str(t) + ".txt"
		
		
		
		
			
		def format(value):
		
			return "%.18f" % value
		
		y2 = [format(x) for x in y1]
		
		del r1[0]
		
		
		def formats(values):
		
			return "%.8f" % values	
		
		
		r2 = [formats(x) for x in r1]

		import csv
		
		# Creating file for dm densities
		resultFile = open(filename,'wb')
		
		# Creating file for corresponding radii
		resultFile1 = open(filename1,'wb')
		print "printing lens"
		print len(r2),len(y2)
		
		wr = csv.writer(resultFile, dialect='excel')
		print "now printing ************************************* writerows"
		wr.writerows(y2)
		
		wr1 = csv.writer(resultFile1, dialect='excel')
		
		#resultfile.close()

		wr1.writerows(r2)
		
				
		radiistring.insert(nM,filename1)
		densitystring.insert(nM,filename)

					
		
					



### This iterative portion here allows the whole process to run over again and again until the last progenitor is reached
	filename_list.insert(nM,filename)
	filename1_list.insert(nM,filename1)
	
	nM = nM + 1
	
	#print "now printing filename list"





# Finally, after this iterative process has produced all the necessary textfiles,
# produce a final text file containing the list of all the text files produced so that
# the non linear regression program can receive this list and know which text files to
# call when fitting the data.


#print filename_list
#print filename1_list

filename2 = "halos.txt"
filename3 = "radii.txt"
filename4 = "listofradii.txt"
filename5 = "listofhalos.txt"

#######   Here I write filename_list to it's own text file which I will then import into regression so that I know which files to do regression on

data = open(filename2, "w")

for c in filename_list:
	data.write(c)

data.close()
	

data = open(filename3, "w")

for c in filename1_list:
	data.write(c)

data.close()


data = open(filename4,"w")

for c in radiistring:
	data.write("%s\n" % c)
	
data.close()


data = open(filename5,"w")

for c in densitystring:
	data.write("%s\n" % c)
	
data.close()
	




	

