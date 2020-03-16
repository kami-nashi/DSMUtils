from flask import Flask
from flask import render_template

import pymysql

app = Flask(__name__)

def dbconnect():
   host = "10.68.25.61"
   user = "dsm_user"
   password = "password"
   db = "dsmutils_csv"
   con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
   cur = con.cursor()
   cur.execute("SHOW TABLES FROM dsmutils_csv;")
   tables = cur.fetchall()
   con.close()
   return tables

some_name = 'Ashley'

@app.route('/logs/lpath')
def log_tables(lpath):
    return render_template("basic.html")

@app.route("/")
def index():
  results = dbconnect()
  return render_template('base.html', table=results)

lpath = dbconnect()

for row in lpath:
  npath = row['Tables_in_dsmutils_csv']

  @app.route('/logs/' + npath)
  def logs():
    results = dbconnect()
    return render_template('base.html', table=results)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=4000)
