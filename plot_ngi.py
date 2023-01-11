#!/usr/bin/python

# Plots (pcolormesh) the ngi files in the list

import numpy as np
import matplotlib.pyplot as plt
import glob
from netCDF4 import Dataset


#dataPath = "/home/cesar/Documents/python/tesis/create_data_set/ngiData/"
dataPath = "/media/ngi/JM91J/2014/"    # Path to .ngi files
outPath =  "/home/cesar/Documents/python/tesis/create_data_set/images/binary/"    # Path to save images

ngiList = glob.glob1(dataPath,"*ngi")    # List of .ngi files
#ngiList=["JM91J_2014203022304.ngi"]


for ngiFile in ngiList:

	ngiData = Dataset(dataPath+ngiFile)  # Read data

	xPower=np.array(ngiData.variables["X-mode_power"][:])
	xPowerT=xPower.transpose()  								
	oPower=np.array(ngiData.variables["O-mode_power"][:])
	oPowerT=oPower.transpose()
	tPower=np.array(ngiData.variables["total_power"][:])
	tPowerT=tPower.transpose()
	ranges=np.array(ngiData.variables["Range"][:])		
	freqs=np.array(ngiData.variables["Frequency"][:])  


	print "O mode power:",np.shape(oPowerT)
	print "X mode power:",np.shape(xPowerT)
	print "Total power:",np.shape(tPowerT)
	print "Ranges:",np.shape(ranges)
	print "Frequencies:",np.shape(freqs)


	"""
	plt.clf()
	plt.subplot(1,3,1)
	plt.pcolormesh(freqs, ranges, xPowerT)
	plt.grid(True)
	plt.subplot(1,3,2)
	plt.pcolormesh(freqs, ranges, oPowerT)
	plt.grid(True)
	plt.subplot(1,3,3)
	plt.pcolormesh(freqs, ranges, tPowerT)
	plt.grid(True)

	plt.show()
	"""
	
	plt.clf()
	plt.pcolormesh(freqs, ranges, oPowerT)
	plt.grid(False)
	plt.show()
	plt.savefig(outPath+ngiFile[:-4]+".png")
	
