#Author: Faryn Dumont
#Formulas based from table 5 in 'Hydrologic and Water Quality Models: Performance Measures and Evaluation Criteria' by D. N. Moriasi, M. W. Gitau, N. Pai, P. Daggupati

import xlrd #whats used to read excel document.
import math
import sys
import statistics

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
	
	#returns a 1-D list with  the list containing all data from all sheets. Header determines if its observed or simulated.
	def getOutflowAll(self, header = "h"):
		if header == "h":
			Outflow = []
			for i in range(self.workBook.nsheets):
				if self.workBook.sheet_by_index(i).visibility == 0:
					OO.extend(self.workBook.sheet_by_index(i).col_values(1)[1:])	
		else:
			Outflow = []
			myHeader = "none"
			num = 1
			for i in range(self.workBook.nsheets):
				num = 1
				if self.workBook.sheet_by_index(i).visibility == 0:
					while myHeader.strip() != header.strip() and num < self.workBook.sheet_by_index(i).ncols:						
						myHeader = self.workBook.sheet_by_index(i).col_values(num)[0]
						num = num + 1
					if num > self.workBook.sheet_by_index(i).ncols:
						statement = "invalid Workbook. Please check sheet "+ str(i+1) + " to make sure there is outflow data"
						sys.exit(statement)
					Outflow.extend(self.workBook.sheet_by_index(i).col_values(num-1)[1:])
					myHeader = "none"
		while('' in Outflow):
			Outflow.remove('')
		return Outflow

	#returns a 2-D list with individual sheets outflow. header determines if its observed or simulated
	def getOutflowIndividual(self, header = "h"):
		if header == "h":
			Outflow = []
			for i in range(self.workBook.nsheets):
				if self.workBook.sheet_by_index(i).visibility == 0:
					OO.append(self.workBook.sheet_by_index(i).col_values(1)[1:])	
		else:
			Outflow = []
			myHeader = "none"
			num = 1
			for i in range(self.workBook.nsheets):
				num = 1
				if self.workBook.sheet_by_index(i).visibility == 0:
					while myHeader.replace(" ", "") != header.replace(" ", "") and num <= self.workBook.sheet_by_index(i).ncols:	
						myHeader = self.workBook.sheet_by_index(i).col_values(num)[0]
						num = num + 1
					if num > self.workBook.sheet_by_index(i).ncols:
						statement = "invalid Workbook. Please check sheet "+ str(i+1) + " to make sure there is outflow data"
						sys.exit(statement)
					Outflow.append(self.workBook.sheet_by_index(i).col_values(num-1)[1:])
					myHeader = "none"
		while('' in Outflow):
			Outflow.remove('')
		return Outflow

	def calculate_r(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		meanOO = sum(OO)/len(OO)
		meanSO = sum(SO)/len(SO)
		top = 0.0
		bottomLeft = 0.0
		bottomRight = 0.0
		for i in range(len(OO)):
			top = top + ((OO[i] - meanOO)*(SO[i] - meanSO))
			bottomLeft = bottomLeft + (OO[i] - meanOO)**2
			bottomRight = bottomRight + (SO[i] - meanSO)**2
		if bottomRight == 0 or bottomLeft == 0:
			return "divide by zero error"
		return top/(math.sqrt(bottomLeft)*math.sqrt(bottomRight))

	def calculateR2(self, observedOutflow, simulatedOutflow):
		r = self.calculate_r(observedOutflow, simulatedOutflow)
		if type(r) == str:
			return r
		return self.calculate_r(observedOutflow, simulatedOutflow)**2

		
	def calculateNSE(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		meanOO = sum(OO)/len(OO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (OO[i]-meanOO)**2
		if bottom == 0:
			return "divide by zero error"
		return 1-top/bottom

	def calculate_d(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		meanOO = sum(OO)/len(OO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (abs(SO[i]-meanOO)+abs(OO[i]-meanOO))**2
		if bottom == 0:
			return "divide by zero error"
		return 1-top/bottom

	def calculateRMSE(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		num = 0.0
		for i in range(len(OO)):
			num = num + (OO[i]-SO[i])**2
		return math.sqrt((1/len(OO))*num)

	def calculateMAE(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		num = 0.0
		for i in range(len(OO)):
			num = num + abs(OO[i]-SO[i])
		return (1/len(OO))*num

	def getRE(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		RE = []
		for i in range(len(OO)):
			if OO[i] != 0:
				num = 100 * abs((OO[i]-SO[i]/OO[i]))
				RE.append(num)
		return RE
	
	def calculateMeanRE(self, observedOutflow, simulatedOutflow):
		RE = self.getRE(observedOutflow, simulatedOutflow)
		if len(RE) == 0:
			return 0.0
		return sum(RE)/len(RE)		

	def calculateMedianRE(self,observedOutflow, simulatedOutflow):
		RE = self.getRE(observedOutflow, simulatedOutflow)
		if len(RE) == 0:
			return 0.0
		return statistics.median(RE)


	def calculateRSR(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		meanSO = sum(SO)/len(SO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (OO[i]-meanSO)**2
		if bottom == 0:
			return "divide by zero error"
		return math.sqrt(top)/math.sqrt(bottom)

	def calculatePBIAS(self,observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		top = 0.0
		bottom = sum(OO)
		for i in range(len(OO)):
			top = top + (OO[i]-SO[i])
		if bottom == 0:
			return "divide by zero error"
		return (top/bottom)*100

	def calculateSS(self, observedOutflow, simulatedOutflow):
		OO = observedOutflow
		SO = simulatedOutflow
		top = 0.0
		bottom = 0.0
		meanOO = sum(OO)/len(OO)
		for i in range(len(OO)):
			top = top + (SO[i]-OO[i])**2
			bottom = bottom + (meanOO - OO[i])**2
		if bottom == 0:
			return "divide by zero error"
		return 1 - top/bottom


	

	
			

