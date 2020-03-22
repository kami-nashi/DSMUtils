#! /usr/bin/env python3
import math

def CalcFuelMix(ExxBlendPCT,GasEthPCT,GasOct,GasGallons,ExxGallons):

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

    # Corrected stoich ratio for the blend. Enter this into the "Global Fuel Calculator" for "Stoichiometric Ratio" (VIEW|ECU > Direct Acccess > Fuel > Calculate ... > 3rd option)
    EstBlendRatio = float(((GasGallons*CalcGasStoich)+(ExxGallons*CalcE85Stoich))/(GasGallons+ExxGallons))

    # Corrected specific gravity for the blend
    EstSpecificGravity = float(((GasGallons*CalcGasSG)+(ExxGallons*CalcE85SG))/(GasGallons+ExxGallons))

    results = [EthPercent,Octane,CalcE85Stoich,CalcE85SG,CalcGasStoich,CalcGasSG,EstBlendRatio,EstSpecificGravity]

    return results

def CalcFuelReq(TgtAirflow,TgtAFR):
    ReqFuelPounds = float(TgtAirflow/TgtAFR)        # Pounds/Minute
    ReqFuelGallon = float(ReqFuelPounds * 60 / 6.2) # Gallons/Hour
    ReqFuelLiter = float(ReqFuelGallon*3.785)       # Liters/Hour
    results = [ReqFuelPounds,ReqFuelGallon,ReqFuelLiter]
    return results

def CalcFuelFlowRateMeasurement(PumpedGallons,PumpedTime):
    frGallon = ((PumpedGallons/PumpedTime)*3600)    # Gallons/Hour
    frLiter = frGallon*3.785                        # Liters/Hour
    frPound = (frGallon/60)*6.2                      # Pounds/Minute
    results = [frPound,frGallon,frLiter]
    return results

def CalcFuelWeight(FuelGallons):
    FuelWeight = 6.5                                # Pounds per gallon
    TotalWeight = FuelGallons*FuelWeight
    return TotalWeight

def CalcRequiredInjectorSize(BSFC,TgtCHP,InjDC,FuelPressure,InjCount):
    ReqInjGas = (((TgtCHP/InjCount)*(BSFC/InjDC))/math.sqrt(FuelPressure/43.5))* 10.5
    ReqInjE85 = ReqInjGas*(1/0.67)
    results = [ReqInjGas,ReqInjE85]
    return results

def CalcMAFCompAirflowCorrectionBoost(logMAP,logBoostEst,currentVE):
    revisedBoost = currentVE*((logMAP+14.7)/(logBoostEst+14.7))
    AdjAirflow = ((logMAP+14.7)/(logBoostEst+14.7))-1
    results = [AdjAirflow*100,revisedBoost]
    return results

def CalcMAFCompAirflowCorrectionWB(logAFREst,logWBO2,currentVE):
    AdjAirflow = (logWBO2/logAFREst)-1
    revisedWB = currentVE*(logWBO2/logAFREst)
    results = [AdjAirflow*100,revisedWB]
    return results

def CalcESTFuelandAirflow(InjRate,InjCount,InjDC,FuelPressure,AFR):
    #AFR = 10.7                                      # Air/Fuel Ratio, not clear why this is different from other entries, user input
    estFuelHour = InjCount*InjDC*(InjRate/10.5)*math.sqrt(FuelPressure/43.5)
    estFuelMin = estFuelHour*10.5
    estAirHour = estFuelHour*AFR
    estAirMin = estAirHour/60
    results = [estFuelHour, estFuelMin, estAirHour, estAirMin]
    return results