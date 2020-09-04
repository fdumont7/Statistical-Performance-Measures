from StatisticalPerformanceMeasures import StatisticalPerformanceMeasures

OOtitle = "Observed Outflow (GPM)"
SOtitle = "Simulated Outflow (GPM)"
SPM = StatisticalPerformanceMeasures()
option = 0
OOI = SPM.getOutflowIndividual(OOtitle)
SOI = SPM.getOutflowIndividual(SOtitle)
OOA = SPM.getOutflowAll(OOtitle)
SOA = SPM.getOutflowAll(SOtitle)

while option == 0:
	option = int(input("Please choose an option\n1 - Get individual sheet calculations\n2 - Get combined sheet calculations\n3 - Get both options\nOption:"))
	if option <= 0 or option > 3:
		option = 0
		print("invalid option")

if option == 1:
	for i in range(SPM.getNumSheets()):
		print("\nSheet", i+1)
		print("\nr =", SPM.calculate_r(OOI[i], SOI[i]),
			"\nR^2 = ", SPM.calculateR2(OOI[i], SOI[i]),
			"\nNSE =", SPM.calculateNSE(OOI[i], SOI[i]),
			"\nd =", SPM.calculate_d(OOI[i], SOI[i]),
			"\nRMSE = ", SPM.calculateRMSE(OOI[i], SOI[i]),
			"\nMAE = ", SPM.calculateMAE(OOI[i], SOI[i]),
			"\nMean RE = ", SPM.calculateMeanRE(OOI[i], SOI[i]),
			"\nMedian RE =", SPM.calculateMedianRE(OOI[i], SOI[i]),
			"\nRSR =", SPM.calculateRSR(OOI[i], SOI[i]),
			"\nPBIAS =", SPM.calculatePBIAS(OOI[i], SOI[i]),
			"\nSS = ", SPM.calculateSS(OOI[i], SOI[i]))
		#if SPM.calculateSS(OOI[i], SOI[i]) == SPM.calculateNSE(OOI[i], SOI[i]):
			#print("\nSS is the same as NSE")
			
elif option == 2:
	print("\nr =", SPM.calculate_r(OOA, SOA),
			"\nR^2 = ", SPM.calculateR2(OOA, SOA),
			"\nNSE =", SPM.calculateNSE(OOA, SOA),
			"\nd =", SPM.calculate_d(OOA, SOA),
			"\nRMSE = ", SPM.calculateRMSE(OOA, SOA),
			"\nMAE = ", SPM.calculateMAE(OOA, SOA),
			"\nMean RE = ", SPM.calculateMeanRE(OOA, SOA),
			"\nMedian RE =", SPM.calculateMedianRE(OOA, SOA),
			"\nRSR =", SPM.calculateRSR(OOA, SOA),
			"\nPBIAS =", SPM.calculatePBIAS(OOA, SOA),
			"\nSS = ", SPM.calculateSS(OOA, SOA))

elif option == 3:
	for i in range(SPM.getNumSheets()):
		print("\nSheet", i+1)
		print("\nr =", SPM.calculate_r(OOI[i], SOI[i]),
			"\nR^2 = ", SPM.calculateR2(OOI[i], SOI[i]),
			"\nNSE =", SPM.calculateNSE(OOI[i], SOI[i]),
			"\nd =", SPM.calculate_d(OOI[i], SOI[i]),
			"\nRMSE = ", SPM.calculateRMSE(OOI[i], SOI[i]),
			"\nMAE = ", SPM.calculateMAE(OOI[i], SOI[i]),
			"\nMean RE = ", SPM.calculateMeanRE(OOI[i], SOI[i]),
			"\nMedian RE =", SPM.calculateMedianRE(OOI[i], SOI[i]),
			"\nRSR =", SPM.calculateRSR(OOI[i], SOI[i]),
			"\nPBIAS =", SPM.calculatePBIAS(OOI[i], SOI[i]),
			"\nSS = ", SPM.calculateSS(OOI[i], SOI[i]))
	print("\nAll Sheets")
	print("\nr =", SPM.calculate_r(OOA, SOA),
			"\nR^2 = ", SPM.calculateR2(OOA, SOA),
			"\nNSE =", SPM.calculateNSE(OOA, SOA),
			"\nd =", SPM.calculate_d(OOA, SOA),
			"\nRMSE = ", SPM.calculateRMSE(OOA, SOA),
			"\nMAE = ", SPM.calculateMAE(OOA, SOA),
			"\nMean RE = ", SPM.calculateMeanRE(OOA, SOA),
			"\nMedian RE =", SPM.calculateMedianRE(OOA, SOA),
			"\nRSR =", SPM.calculateRSR(OOA, SOA),
			"\nPBIAS =", SPM.calculatePBIAS(OOA, SOA),
			"\nSS = ", SPM.calculateSS(OOA, SOA))