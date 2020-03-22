from flask import Flask
from flask import render_template
from flask import jsonify
from flask import Response
from flask import request

import calculators as calc
import db_dump as dump

import json
import pymysql

app = Flask(__name__)

def buildMenu():
    sql = "SHOW TABLES FROM dsmutils_csv;"
    results = dump.dbconnect(sql)
    return results

@app.route("/")
def index():
   return render_template('template.html', table=buildMenu())

@app.route('/logs/<lpath>')
def log_tables(lpath):
   return render_template("logs.html", table=buildMenu(),lpath=lpath)

@app.route('/logs/json/<log_table>', methods=['GET'])
def get_tasks(log_table):
    log = json.loads(dump.log_api(log_table))
    jlog = json.dumps(log, indent=4)
    resp = Response(jlog, status=200, mimetype='application/json')
    return resp

@app.route('/CalcMAFCompAirflowCorrectionWB')
def CalcMAFCompAirflowCorrectionWB():
    jMath = 1
    return render_template('CalcMAFCompAirflowCorrectionWB.html', table=buildMenu(), jMath=jMath)

@app.route('/submit_CalcMAFCompAirflowCorrectionWB', methods=['POST'])
def submit_CalcMAFCompAirflowCorrectionWB():
    if request.method == 'POST':
        logAFREst = request.form['logAFREst']
        logWBO2 = request.form['logWBO2']
        currentVE = request.form['currentVE']
        calcu = calc.CalcMAFCompAirflowCorrectionWB(float(logAFREst), float(logWBO2), float(currentVE))
        results = calcu
        return render_template('CalcMAFCompAirflowCorrectionWB.html', table=buildMenu(), jMath=results)
    else:
        return render_template('CalcMAFCompAirflowCorrectionWB.html', table=buildMenu())

@app.route('/CalcMAFCompAirflowCorrectionBoost')
def CalcMAFCompAirflowCorrectionBoost():
    jMath = 1
    return render_template('CalcMAFCompAirflowCorrectionBoost.html', table=buildMenu(), jMath=jMath)

@app.route('/submit_CalcMAFCompAirflowCorrectionBoost', methods=['POST'])
def submit_CalcMAFCompAirflowCorrectionBoost():
    if request.method == 'POST':
        logMAP = request.form['logMAP']
        logBoostEst = request.form['logBoostEst']
        currentVE = request.form['currentVE']
        calcu = calc.CalcMAFCompAirflowCorrectionBoost(float(logMAP), float(logBoostEst), float(currentVE))
        results = calcu
        return render_template('CalcMAFCompAirflowCorrectionBoost.html', table=buildMenu(), jMath=results)
    else:
        return render_template('CalcMAFCompAirflowCorrectionBoost.html', table=buildMenu())

@app.route('/CalcESTFuelandAirflow')
def CalcESTFuelandAirflow():
    jMath = 1
    return render_template('calcESTFuelandAirflow.html', table=buildMenu(), jMath=jMath)

@app.route('/submit_CalcESTFuelandAirflow', methods=['POST'])
def submit_CalcESTFuelandAirflow():
    if request.method == 'POST':
        InjRate = request.form['InjRate']
        InjCount = request.form['InjCount']
        InjDC = request.form['InjDC']
        FuelPressure = request.form['FuelPressure']
        AFR = request.form['AFR']
        calcu = calc.CalcESTFuelandAirflow(float(InjRate), float(InjCount), float(InjDC)/100, float(FuelPressure), float(AFR))
        results = calcu
        return render_template('calcESTFuelandAirflow.html', table=buildMenu(), jMath=results)
    else:
        return render_template('calcESTFuelandAirflow.html', table=buildMenu())

@app.route('/CalcRequiredInjectorSize')
def CalcRequiredInjectorSize():
    jMath = 1
    return render_template('CalcRequiredInjectorSize.html', jMath=jMath)

@app.route('/submit_CalcRequiredInjectorSize', methods=['POST'])
def submit_CalcRequiredInjectorSize():
    if request.method == 'POST':
        BSFC = request.form['BSFC']
        InjDC = request.form['InjDC']
        TgtCHP = request.form['TgtCHP']
        FuelPressure = request.form['FuelPressure']
        InjCount = request.form['InjCount']
        calcu = calc.CalcRequiredInjectorSize(float(BSFC), float(TgtCHP), float(InjDC)/100, float(FuelPressure), int(InjCount))
        results = calcu
        return render_template('CalcRequiredInjectorSize.html', table=buildMenu(), jMath=results)
    else:
        return render_template('CalcRequiredInjectorSize.html', table=buildMenu())

@app.route('/CalcFuelWeight')
def CalcFuelFlowWeight():
    jMath = 1
    return render_template('calcFuelWeight.html', table=buildMenu(), jMath=jMath)

@app.route('/submit_calcFuelWeight', methods=['POST'])
def submit_CalcFuelWeight():
    if request.method == 'POST':
        FuelGallons = request.form['FuelGallons']
        calcu = calc.CalcFuelWeight(float(FuelGallons))
        results = calcu
        return render_template('calcFuelWeight.html', jMath=results)
    else:
        return render_template('calcFuelWeight.html', table=buildMenu())

@app.route('/CalcFuelFlowRateMeasurement')
def CalcFuelFlowRateMeasurement():
    jMath = 1
    return render_template('CalcFuelFlowRateMeasurement.html', table=buildMenu(), jMath=jMath)

@app.route('/submit_CalcFuelFlowRateMeasurement', methods=['POST'])
def submit_CalcFuelFlowRateMeasurement():
    if request.method == 'POST':
        PumpedGallons = request.form['PumpedGallons']
        PumpedTime = request.form['PumpedTime']
        calcu = calc.CalcFuelFlowRateMeasurement(float(PumpedGallons),float(PumpedTime))
        results = calcu
        return render_template('CalcFuelFlowRateMeasurement.html', table=buildMenu(), jMath=results)
    else:
        return render_template('CalcFuelFlowRateMeasurement.html', table=buildMenu())

@app.route('/calcFuelReq')
def calcFuelReq():
    jMath = 1
    return render_template('calcFuelReq.html', table=buildMenu(), jMath=jMath)

@app.route('/submit_calcFuelReq', methods=['POST'])
def submit_calcFuelReq():
    if request.method == 'POST':
        TgtAirflow = request.form['TgtAirflow']
        TgtAFR = request.form['TgtAFR']
        calcu = calc.CalcFuelReq(float(TgtAirflow),float(TgtAFR))
        results = calcu
        return render_template('calcFuelReq.html', table=buildMenu(), jMath=results)
    else:
        return render_template('calcFuelReq.html', table=buildMenu())

@app.route('/calcFuelMix')
def calcFuelMix():
    jMath = 1
    return render_template('calcFuelMix.html', jMath=jMath)

@app.route('/submit_calcFuelMix', methods=['POST'])
def submit_calcFuelMix():
    if request.method == 'POST':
        ExxBlendPCT = request.form['ExxBlendPCT']
        GasEthPCT = request.form['GasEthPCT']
        GasOct = request.form['GasOct']
        GasGallons = request.form['GasGallons']
        ExxGallons = request.form['ExxGallons']
        fExxBlendPCT = float(ExxBlendPCT)/100
        fGasEthPCT = float(GasEthPCT)/100
        calcu = calc.CalcFuelMix(fExxBlendPCT,fGasEthPCT,float(GasOct),float(GasGallons),float(ExxGallons))
        results = calcu
        return render_template('calcFuelMix.html', table=buildMenu(), jMath=results)
    else:
        return render_template('calcFuelMix.html', table=buildMenu())

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, use_reloader=True,debug=True)