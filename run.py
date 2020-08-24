from StatisticalPerformanceMeasures import StatisticalPerformanceMeasures


SPM = StatisticalPerformanceMeasures()

#print(FI.getSimulatedOutflow())
print("NSE = ", SPM.calculateNSE() , "\nPBIAS = ", SPM.calculatePBIAS(), "\nRSR = ", SPM.calculateRSR(), "\nd = ", SPM.calculate_d())