from StatisticalPerformanceMeasures import StatisticalPerformanceMeasures


SPM = StatisticalPerformanceMeasures()

print(SPM.getNumSheets())
print("NSE = ", SPM.calculateNSE(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()) ,
      "\nPBIAS = ", SPM.calculatePBIAS(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()),
      "\nRSR = ", SPM.calculateRSR(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()),
      "\nd = ", SPM.calculate_d(SPM.getObservedOutflowAll(), SPM.getSimulatedOutflowAll()))