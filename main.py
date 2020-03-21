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

some_name = 'Ashley'

@app.route("/")
def index():
   sql= "SHOW TABLES FROM dsmutils_csv;"
   results = dump.dbconnect(sql)
   return render_template('base.html', table=results)

@app.route('/logs/<lpath>')
def log_tables(lpath):
   sql= "SHOW TABLES FROM dsmutils_csv;"
   results = dump.dbconnect(sql)
   return render_template("base.html", table=results,lpath=lpath)


@app.route('/logs/json/<log_table>', methods=['GET'])
def get_tasks(log_table):
    log = json.loads(dump.log_api(log_table))
    jlog = json.dumps(log, indent=4)
    resp = Response(jlog, status=200, mimetype='application/json')
    return resp

@app.route('/CalcFuelWeight')
def CalcFuelFlowWeight():
    jMath = 1
    return render_template('calcFuelWeight.html', jMath=jMath)

@app.route('/submit_calcFuelWeight', methods=['POST'])
def submit_CalcFuelWeight():
    if request.method == 'POST':
        FuelGallons = request.form['FuelGallons']
        calcu = calc.CalcFuelWeight(float(FuelGallons))
        results = calcu
        jMath = jsonify({'FuelWeight':results})
        return render_template('calcFuelWeight.html', jMath=results)
    else:
        return render_template('calcFuelWeight.html')

@app.route('/CalcFuelFlowRateMeasurement')
def CalcFuelFlowRateMeasurement():
    jMath = 1
    return render_template('CalcFuelFlowRateMeasurement.html', jMath=jMath)

@app.route('/submit_CalcFuelFlowRateMeasurement', methods=['POST'])
def submit_CalcFuelFlowRateMeasurement():
    if request.method == 'POST':
        PumpedGallons = request.form['PumpedGallons']
        PumpedTime = request.form['PumpedTime']
        calcu = calc.CalcFuelFlowRateMeasurement(float(PumpedGallons),float(PumpedTime))
        results = calcu
        jMath = jsonify({'frPound':results[0],'frGallon':results[1],'frLiter':results[2]})
        return render_template('CalcFuelFlowRateMeasurement.html', jMath=results)
    else:
        return render_template('CalcFuelFlowRateMeasurement.html')

@app.route('/calcFuelReq')
def calcFuelReq():
    jMath = 1
    return render_template('calcFuelReq.html', jMath=jMath)

@app.route('/submit_calcFuelReq', methods=['POST'])
def submit_calcFuelReq():
    if request.method == 'POST':
        TgtAirflow = request.form['TgtAirflow']
        TgtAFR = request.form['TgtAFR']
        calcu = calc.CalcFuelReq(float(TgtAirflow),float(TgtAFR))
        results = calcu
        jMath = jsonify({'ReqFuelPounds':results[0],'ReqFuelGallon':results[1],'ReqFuelLiter':results[2]})
        return render_template('calcFuelReq.html', jMath=results)
    else:
        return render_template('calcFuelReq.html')

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
        jMath = jsonify({'PCTeth':results[0],'OCTrating':results[1],'CalcEsg':results[2],'CalcEst':results[3],'CalcGsg':results[4],'CalcGst':results[5],'EstSTr':results[6],'EstSG':results[7]})
        return render_template('calcFuelMix.html', jMath=results)
    else:
        return render_template('calcFuelMix.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, use_reloader=True,debug=True)