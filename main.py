from flask import Flask
from flask import render_template
import db_dump as dump

import pymysql

app = Flask(__name__)

#db = 'dummy_data'
#sql = "select timestamp, rpm, airflow, fronto2, timing, inttemp, cooltemp, knockret, speed, throtpos from " + db+ ";"

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
   return render_template("base.html", table=results)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=4000, use_reloader=True)