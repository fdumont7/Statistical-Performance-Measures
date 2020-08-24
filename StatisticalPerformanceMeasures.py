import xlrd #whats used to read excel document. get by 'pip install xlrd'
import math
#currently the target station is the last item in the document.
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
		
		

	def getObservedOutflow(self):
		OO = []
		for i in range(len(self.workBook.sheet_names())):
			OO.extend(self.workBook.sheet_by_index(i).col_values(1)[1:])

		while('' in OO):
			OO.remove('')
		return OO
		
	def getSimulatedOutflow(self):
		SO = []
		for i in range(len(self.workBook.sheet_names())):
			SO.extend(self.workBook.sheet_by_index(i).col_values(4)[1:])

		while('' in SO):
			SO.remove('')

		return SO

	def calculateNSE(self):
		OO = self.getObservedOutflow()
		SO = self.getSimulatedOutflow()
		meanOO = sum(OO)/len(OO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (OO[i]-meanOO)**2

		return 1-top/bottom

	def calculatePBIAS(self):
		OO = self.getObservedOutflow()
		SO = self.getSimulatedOutflow()
		top = 0.0
		bottom = sum(OO)
		for i in range(len(OO)):
			top = top + (OO[i]-SO[i])

		return (top/bottom)*100

	def calculateRSR(self):
		OO = self.getObservedOutflow()
		SO = self.getSimulatedOutflow()
		meanSO = sum(SO)/len(SO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (OO[i]-meanSO)**2
		return math.sqrt(top)/math.sqrt(bottom)

	def calculate_d(self):
		OO = self.getObservedOutflow()
		SO = self.getSimulatedOutflow()
		meanOO = sum(OO)/len(OO)
		top = 0.0
		bottom = 0.0
		for i in range(len(OO)):
			top =top + (OO[i]-SO[i])**2
			bottom = bottom + (abs(SO[i]-meanOO)+abs(OO[i]-meanOO))**2

		return 1-top/bottom
			

