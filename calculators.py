#! /usr/bin/env python3
import math

def CalcFuelMix():

     # Fuel Values - Calculated/Derived (User Values)
    ExxBlendPCT = float(.85)                # Percent -> 0.NN
    GasEthPCT = float(.10)                  # Percent ethanol -> 0.NN
    GasOct = float(93)                      # Pump gas or non-e85 octane rating
    GasGallons = float(5.00)                # Amount of gas in the tank or mix
    ExxGallons = float(5.00)                # Amount of ethanol in the tank or mix

    # Fuel Constants
    cGasSG = float(0.720)                   # Pure Gas Specific Gravity, typically 0.739
    cGasStoich = float(14.64)               # Pure Gas Stoich Ratio, typically 14.64
    cEthSG = float(0.796)                   # Pure Ethanol Specific Gravity, typically 0.796
    cEthStoich = float(9.01)                # Pure Ethanol Stoich Ration, typically 9.01
    cEthOctane = float(113)                 # Octane Rating of Ethanol, typically 105
    cEthCut = float(87)                     # "Cut" Ethanol Octane

    # Calculated Octane
    CalcEthOctane = float((ExxBlendPCT*cEthOctane)+((1-ExxBlendPCT)*cEthCut)) #float(103)

    # Percetage of Ethanol #((gallonsEXX*EXXEthPCT)+(GallonsGas*GasETHPCT) / (GallonsGAS + GallonsEXX)
    EthPercent = float((((ExxGallons*ExxBlendPCT) + (GasGallons*GasEthPCT)) / (GasGallons+ExxGallons))*100)

    # Corrected Stoich Ratio for pump gas after adjusting for blend percent of (c4)
    # Pump gas with 10% ethanol will be 14.0 to 14.1 where as pure gas will be 14.64
    CalcGasStoich = float((cEthStoich * GasEthPCT) + (cGasStoich * (1 - GasEthPCT)))

    # Specific gravity of pump gas, based on blend percentage
    CalcGasSG = float((cEthSG * GasEthPCT) + (cGasSG * (1 - GasEthPCT)))

    # Specific Gravity of E85 based on blend percentage in (C9)
    CalcE85SG = float((cEthSG * ExxBlendPCT) + (cGasSG * (1 - ExxBlendPCT)))

    # Calculated value of E85 based on blend percentage in (C9)
    CalcE85Stoich = float((cEthStoich * ExxBlendPCT) + (cGasStoich * (1 - ExxBlendPCT)))

    # Adjusted octane rating for the blend
    Octane = ((GasGallons*GasOct)+(ExxGallons*CalcEthOctane))/(GasGallons+ExxGallons)

    # Corrected stoich ratio for the blend. Enter this into the "Global Fuel Calculator" for "Stoichiometric Ratio" (VIEW|ECU > Direct Accces > Fuel > Calculate ... > 3rd option)
    EstBlendRatio = float(((GasGallons*CalcGasStoich)+(ExxGallons*CalcE85Stoich))/(GasGallons+ExxGallons))

    # Corrected specific gravity for the blend
    EstSpecificGravity = float(((GasGallons*CalcGasSG)+(ExxGallons*CalcE85SG))/(GasGallons+ExxGallons))

    results = [EthPercent,Octane,CalcE85Stoich,CalcE85SG,CalcGasStoich,CalcGasSG,EstBlendRatio,EstSpecificGravity]

    return results

def CalcFuelReq():
    TgtAirflow = 55                                 # Target airflow, in lbs/min
    TgtAFR = 8.0                                    # Target AFR
    ReqFuelPounds = float(TgtAirflow/TgtAFR)        # Pounds/Minute
    ReqFuelGallon = float(ReqFuelPounds * 60 / 6.2) # Gallons/Hour
    ReqFuelLiter = float(ReqFuelGallon*3.785)       # Liters/Hour
    results = [ReqFuelPounds,ReqFuelGallon,ReqFuelLiter]
    return results

def CalcFuelFlowRateMeasurement():
    PumpedGallons = 44.4
    PumpedTime = 3600                               # In Seconds
    frGallon = ((PumpedGallons/PumpedTime)*3600)    # Gallons/Hour
    frLiter = frGallon*3.785                        # Liters/Hour
    frPound = (frLiter/60)*6.2                      # Pounds/Minute
    results = [frPound,frGallon,frLiter]
    return results

def CalcFuelWeight():
    FuelWeight = 6.5                                # Pounds per gallon
    FuelGallons = 5                                 # Amount of fuel, in gallons, user input
    TotalWeight = FuelGallons*FuelWeight
    return TotalWeight

def CalcRequiredInjectorSize():
    BSFC = 0.65                                     # Not clear what this does, but its a constant
    TgtCHP = 400                                    # Target Crank HP, user input
    InjDC = .80                                     # Injector Duty Cycle, in percent. 80% = .80, user input
    FuelPressure = 43.5                             # Base Fuel Pressure, lb's, user input
    InjCount = 4                                    # Number of injectors, user input
    ReqInjGas = (((TgtCHP/InjCount)*(BSFC/InjDC))/math.sqrt(FuelPressure/43.5))* 10.5
    ReqInjE85 = ReqInjGas*(1/0.67)
    results = [ReqInjGas,ReqInjE85]
    return results


def CalcMAFCompAirflowCorrectionBoost():
    logMAP = 26.7                                   # User Input
    logBoostEst = 29.2                              # User Input
    currentVE = 99                                  # Currently configured VE, user input
    revisedBoost = currentVE*((logMAP+14.7)/(logBoostEst+14.7))
    AdjAirflow = ((logMAP+14.7)/(logBoostEst+14.7))-1
    results = [AdjAirflow,revisedBoost]
    return results

def CalcMAFCompAirflowCorrectionWB():
    logAFREst = 10.8                                # User Input
    logWBO2 = 10.5                                  # Measured AFR via Wideband, user input
    AdjAirflow = (logWBO2/logAFREst)-1
    currentVE = 99                                  # Currently configured VE, user input
    revisedWB = currentVE*(logWBO2/logAFREst)
    results = [AdjAirflow,revisedWB]
    return results

def CalcESTFuelandAirflow():
    InjRate = 1100                                  # Injector rate, in CC, user input
    InjCount = 4                                    # Injector count, user input
    InjDC = .397                                    # Injector duty cycle, percent. 39.7 = .397, user input
    FuelPressure = 43.0                             # Base fuel pressure, user input
    AFR = 10.7                                      # Air/Fuel Ratio, not clear why this is different from other entries, user input

    estFuelHour = InjCount*InjDC*(InjRate/10.5)*math.sqrt(FuelPressure/43.5)
    estFuelMin = estFuelHour*10.5
    estAirHour = estFuelHour*AFR
    estAirMin = estAirHour/60

    results = [estFuelHour, estFuelMin, estAirHour, estAirMin]
    return results

# Diagnostic Prints, to be removed in the future.
#results = CalcFuelMix()
#print("Percentage Ethanol: \t\t", results[0], "%")
#print("Octane Rating: \t\t\t", results[1])
#print("Calculated E85 Stoich: \t\t", results[2])
#print("Calculated E85 Specific Gravity:", results[3])
#print("Calculated Gas Stoich: \t\t", results[4])
#print("Calculated Gas Specific Gravity:", results[5])
#print("Estimated Stoich Ratio: \t", results[6])
#print("Estimated Specific Gravity: \t", results[7])
#print(CalcFuelReq())
#print(CalcRequiredInjectorSize())
#print(CalcESTFuelandAirflow())
#print(CalcFuelFlowRateMeasurement())
#print(CalcFuelWeight())
#print(CalcMAFCompAirflowCorrectionBoost())
#print(CalcMAFCompAirflowCorrectionWB())