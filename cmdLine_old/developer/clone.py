#!/usr/bin/python
#ccfxcsvToMetric.py: This script calculates clone-metric from csv file generated by ccfxoutToCsv.py script

import sys
import csv

#=====================================================================#
#Global variables

DEBUG = 0
clones = {}
dict_index = []

#=====================================================================#
def debug_print(str):
	if DEBUG:
		print str

#=====================================================================#
class Change:

	def __init__(self,cl):
				
		self.fileIndex,self.lineRange = cl.split(".")
		self.fileName = ""
		self.start,self.end = self.lineRange.split("-")
				

#************************************************************************#
	
	def __str__(self):

		return  str(self.fileIndex) + " : " + str(self.fileName) + " : " + str(self.start) + " : " +  str(self.end) 

		
