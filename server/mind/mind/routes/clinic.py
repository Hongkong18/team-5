from flask import jsonify, request
from mind import app
import json

from mind import conn

from decimal import Decimal

class fakefloat(float):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return str(self._value)

def defaultencode(o):
    if isinstance(o, Decimal):
        # Subclass float with custom repr?
        return fakefloat(o)
    raise TypeError(repr(o) + " is not JSON serializable")


@app.route('/clinic', methods=['GET'])
def get_clinics():
    # data = request.get_json()

    cursor = conn.cursor()
    cursor.execute("SELECT * from clinic_tbl")
    result = cursor.fetchall()
    print(result)
    payload = []
    for r in result:
        payload.append({
                'clinic_id': r[0],
                'clinic_name': r[1],
                'address': r[2],
                'contact_no': str(r[3]),
                'description': r[4],
                'latitude': float(r[5]),
                'longitude': float(r[6]),
                'clinic_count': r[7],
                'open_time': str(r[8]),
                'close_time': str(r[9]),
                'photo_url': r[10]
            })

    
    return jsonify(clinic=payload)

@app.route('/clinic/<id>', methods=['GET'])
def get_clinic(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * from clinic_tbl where id=%s", (id,))
    clinic = cursor.fetchone()

    return jsonify(clinic=clinic)


@app.route('/clinic/add', methods=['POST'])
def add_clinics():
    data = request.get_json()['clinics']
    cursor = conn.cursor()

    for d in data:
        sql = "INSERT INTO clinic_tbl (clinic_name, address, open_time, close_time, contact_no, description, latitude, longitude, clinic_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.executemany(sql, (d['clinic_name'], d['address'], d['open_time'], d['close_time'], d['contact_no'], d['description'], d['latitude'], d['longitude'], 0,))

    return jsonify(message='success')


@app.route('/clinic/delete/<id>', methods=['GET'])
def delete_clinic(id):
    sql = "DELETE FROM clinic_tbl where id=%s"
    cursor = conn.cursor()
    cursor.execute(sql, (id,))

    return jsonify(message='success')
