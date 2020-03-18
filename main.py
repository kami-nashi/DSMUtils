from flask import Flask
from flask import render_template
from flask import jsonify
from flask import Response

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
   #log_table = lpath
   #logs = dump.log_api(log_table)
   return render_template("base.html", table=results,lpath=lpath)


@app.route('/logs/json/<log_table>', methods=['GET'])
def get_tasks(log_table):
    #log_table = 'dummy_data'
    log = json.loads(dump.log_api(log_table))
    jlog = json.dumps(log, indent=4)
    #print(jlog)
    resp = Response(jlog, status=200, mimetype='application/json')
    return resp


@app.route('/calc')
def calc():
   return render_template('calc.html')


@app.route('/action', methods=['POST'])
def update(ExxBlendPCT,GasEthPCT,GasOct,GasGallons,ExxGallons):

    ExxBlendPCT = float(ExxBlendPCT*.10)
    GasEthPCT = float(GasEthPCT*.10)
    #input = [ExxBlendPCT,GasEthPCT,float(GasOct),float(GasGallons),float(ExxGallons)]
    results = calc.CalcFuelMix(ExxBlendPCT,GasEthPCT,float(GasOct),float(GasGallons),float(ExxGallons))
    # results = CalcFuelMix()
    # print("Percentage Ethanol: \t\t", results[0], "%")
    # print("Octane Rating: \t\t\t", results[1])
    # print("Calculated E85 Stoich: \t\t", results[2])
    # print("Calculated E85 Specific Gravity:", results[3])
    # print("Calculated Gas Stoich: \t\t", results[4])
    # print("Calculated Gas Specific Gravity:", results[5])
    # print("Estimated Stoich Ratio: \t", results[6])
    # print("Estimated Specific Gravity: \t", results[7])
    return jsonify({'PCTeth':results[0],'OCTrating':results[1],'CalcEsg':results[2],'CalcEst':results[3],'CalcGsg':results[4],'CalcGst':results[5],'EstSTr':results[6],'EstSG':results[7]})
#   member = Member.query.filter_by(id=request.form['id']).first()
#   member.name = request.form['name']
#   member.email = request.form['email']
#   member.random = randint(1, 10000)
#   db.session.commit()
#   print(input)
#   return jsonify({'result': 'success', 'member_num': member.random})


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=4000, use_reloader=True)