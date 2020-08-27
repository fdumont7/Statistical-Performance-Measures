#Author: Faryn Dumont
#Formulas based from table 5 in 'Hydrologic and Water Quality Models: Performance Measures and Evaluation Criteria' by D. N. Moriasi, M. W. Gitau, N. Pai, P. Daggupati

import xlrd #whats used to read excel document.
import math

#TODO find way to skip non-visible sheets when printing calculations

class StatisticalPerformanceMeasures:

	def __init__(self):
		while True:
			try:
				myFile = input("What file would you like to open (please put in full location)\n")
				workBook = xlrd.open_workbook(myFile)
				break
			except OSError:
				print("invalid file name please try again")
		#on_demand is used to avoid loading worksheet data into memory
		self.workBook = xlrd.open_workbook(myFile, on_demand = True)

	def getNumSheets(self):
		numOfVisibleSheets = 0
		for i in range(self.workBook.nsheets):
			if self.workBook.sheet_by_index(i).visibility == 0:
				numOfVisibleSheets = numOfVisibleSheets + 1
		return numOfVisibleSheets

	#returns 1d list with the list containing all data from all sheets
	def getObservedOutflowAll(self):
		OO = []
		for i in range(len(self.workBook.sheet_names())):
			if self.workBook.sheet_by_index(i).visibility == 0:
				OO.extend(self.workBook.sheet_by_index(i).col_values(1)[1:])
		while('' in OO):
			OO.remove('')
		return OO

	#returns 1d list with the list containing all data from all sheets 
	def getSimulatedOutflowAll(self):
		SO = []
		for i in range(len(self.workBook.sheet_names())):
			if self.workBook.sheet_by_index(i).visibility == 0:
				SO.extend(self.workBook.sheet_by_index(i).col_values(4)[1:])
		while('' in SO):
			SO.remove('')
		return SO

	#returns 2d list with the list containing individual lists for each sheet
	def getObservedOutflowIndividual(self):
		OO = []
		for i in range(len(self.workBook.sheet_names())):
			if self.workBook.sheet_by_index(i).visibility == 0:
				OO.append(self.workBook.sheet_by_index(i).col_values(1)[1:])
				while ('' in OO[i]):
					OO[i].remove('')			
		return OO

	# returns 2d list with the list containing individual lists for each sheet
	def getSimulatedOutflowIndividual(self):
		SO = []
		for i in range(len(self.workBook.sheet_names())):
			if self.workBook.sheet_by_index(i).visibility == 0:
				SO.append(self.workBook.sheet_by_index(i).col_values(4)[1:])
			while ('' in SO):
				SO.remove('')
		return SO

	def calculateNSE(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		meanOO = sum(OO)/len(OO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (OO[i]-meanOO)**2
		return 1-top/bottom

	def calculatePBIAS(self,observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		top = 0.0
		bottom = sum(OO)
		for i in range(len(OO)):
			top = top + (OO[i]-SO[i])
		return (top/bottom)*100

	def calculateRSR(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		meanSO = sum(SO)/len(SO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (OO[i]-meanSO)**2
		return math.sqrt(top)/math.sqrt(bottom)

	def calculate_d(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		meanOO = sum(OO)/len(OO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (abs(SO[i]-meanOO)+abs(OO[i]-meanOO))**2
		return 1-top/bottom
			

