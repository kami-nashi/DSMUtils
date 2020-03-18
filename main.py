from flask import Flask
from flask import render_template
from flask import jsonify
import db_dump as dump

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


##############################################################################
@app.route('/logs/json/<log_table>', methods=['GET'])
def get_tasks(log_table):
    #log_table = 'dummy_data'
    jlog = dump.log_api(log_table)
    return jsonify(jlog)
##############################################################################

#@app.route('/logs/json/<lpath>', methods=['GET'])
#def get_tasks(lpath):
#    db = lpath
#    jlog = dump.log_api(db)
#    print(db)
#    return jsonify(jlog)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=4000, use_reloader=True)