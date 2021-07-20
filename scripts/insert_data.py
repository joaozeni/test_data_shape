from pytz import timezone
import pandas
import psycopg2
from datetime import datetime
from dateutil import parser
import json
import re

try:
    conn = psycopg2.connect("dbname='sensors_db' user='postgres' password='postgres' host='localhost'")
except:
    print("DB connection failed.")
    quit()

cur = conn.cursor()

print('Inserting equipments')
equipment_file = open('equipment.json')
equipment_data = json.load(equipment_file)
for equipment in equipment_data:
    id = equipment['equipment_id']
    code = equipment['code']
    group_name = equipment['group_name']
    cur.execute(f"INSERT INTO equipments (id, code, group_name) VALUES ({id}, '{code}', '{group_name}')")

conn.commit()
equipment_file.close()

payments_dict = dict()
id_mapper = dict()
payment_id = 1

print('Inserting sensors')
sensors = pandas.read_csv('equipment_sensors.csv', header=0, sep=';')
equipment_dict = dict()
for index, item in sensors.iterrows():
    sensor_id = item['sensor_id']
    equipment_id = item['equipment_id']
    cur.execute(f"INSERT INTO sensors (id, equipment_id) VALUES ({sensor_id}, {equipment_id})")
    equipment_dict[sensor_id] = equipment_id

conn.commit()

print('Inserting failures')
failure_id = 1
pat = r'(?<=\[)(.*?)(?=\])' # pattern to match the data between braclets
pat_2 = r'[-+]?\d*\.\d+' # pattern to match the floats
local_time = timezone('Etc/GMT')
failure_file = open('equipment_failure_sensors.log')
failures = failure_file.readlines()
for failure in failures:
    date, sensor_id = re.findall(pat, failure)
    temperature, vibration = re.findall(pat_2, failure)
    id = failure_id
    sensor_id = int(sensor_id)
    equipment_id = equipment_dict[sensor_id]
    date = parser.parse(date)
    temperature = float(temperature)
    vibration = float(vibration)
    cur.execute(f"INSERT INTO failures (id, sensor_id, equipment_id, failure_date, temperature, vibration) VALUES ({id}, {sensor_id}, {equipment_id}, '{date}', {temperature}, {vibration})")
    failure_id += 1

conn.commit()
failure_file.close()

cur.close()
conn.close()

