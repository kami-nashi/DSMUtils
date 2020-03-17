#! /usr/bin/env python3
import json
import pymysql

def dbconnect(sql):
   host = "10.68.25.61"
   user = "dsm_user"
   password = "password"
   db = "dsmutils_csv"
   con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
   cur = con.cursor()
   cur.execute(sql)
   tables = cur.fetchall()
   con.close()
   return tables

def log_api(log_table):
   db = log_table
   sql = "select timestamp, rpm, airflow, fronto2, timing, inttemp, cooltemp, knockret, speed, throtpos from " + db + ";"
   dump = dbconnect(sql)
   log = {}
   log[db] = []
   for i in dump:
      time = i['timestamp']
      log[db].append({'time': i['timestamp'], 'rpm': i['rpm'], 'airflow': float(i['airflow']), 'fronto2': float(i['fronto2']), 'timing': float(i['timing']), 'inttemp': float(i['inttemp']), 'cooltemp': float(i['cooltemp']), 'knockret': float(i['knockret']), 'speed': float(i['speed']), 'throtpos': float(i['throtpos'])})

   jlog = json.dumps(log, indent=4)

   print(jlog)