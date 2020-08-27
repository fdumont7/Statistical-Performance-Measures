from StatisticalPerformanceMeasures import StatisticalPerformanceMeasures


SPM = StatisticalPerformanceMeasures()
option = 0
while option == 0:
	option = int(input("Please choose an option\n1 - Get individual sheet calculations\n2 - Get combined sheet calculations\n3 - Get both options\nOption:"))
	if option <= 0 or option > 3:
		option = 0
		print("invalid option")

if option == 1:
	for i in range(SPM.getNumSheets()):
		print("\nSheet", i+1)
		print("NSE =", SPM.calculateNSE(SPM.getObservedOutflowIndividual()[i], SPM.getSimulatedOutflowIndividual()[i]),
			"\nPBIAS =", SPM.calculatePBIAS(SPM.getObservedOutflowIndividual()[i], SPM.getSimulatedOutflowIndividual()[i]),
			"\nRSR =", SPM.calculateRSR(SPM.getObservedOutflowIndividual()[i], SPM.getSimulatedOutflowIndividual()[i]),
			"\nd =", SPM.calculate_d(SPM.getObservedOutflowIndividual()[i], SPM.getSimulatedOutflowIndividual()[i]))
elif option == 2:
	print("NSE = ", SPM.calculateNSE(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()),
      "\nPBIAS = ", SPM.calculatePBIAS(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()),
      "\nRSR = ", SPM.calculateRSR(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()),
      "\nd = ", SPM.calculate_d(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()))
elif option == 3:
	for i in range(SPM.getNumSheets()):
		print("\nSheet", i+1)
		print("NSE =", SPM.calculateNSE(SPM.getObservedOutflowIndividual()[i], SPM.getSimulatedOutflowIndividual()[i]),
			"\nPBIAS =", SPM.calculatePBIAS(SPM.getObservedOutflowIndividual()[i], SPM.getSimulatedOutflowIndividual()[i]),
			"\nRSR =", SPM.calculateRSR(SPM.getObservedOutflowIndividual()[i], SPM.getSimulatedOutflowIndividual()[i]),
			"\nd =", SPM.calculate_d(SPM.getObservedOutflowIndividual()[i], SPM.getSimulatedOutflowIndividual()[i]))
	print("\nAll Sheets")
	print("NSE = ", SPM.calculateNSE(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()),
      "\nPBIAS = ", SPM.calculatePBIAS(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()),
      "\nRSR = ", SPM.calculateRSR(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()),
      "\nd = ", SPM.calculate_d(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()))