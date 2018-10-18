from flask import jsonify, request
from mind import app

from app import conn


@app.route('/clinic', methods=['GET'])
def get_clinics():
    # data = request.get_json()

    cursor = conn.cursor()
    cursor.execute("SELECT * from clinic")
    clinics = cursor.fetchall()

    return jsonify(clinics=clinics)


@app.route('/clinic/<id>', methods=['GET'])
def get_clinic(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * from Clinic where id=%s", (id,))
    clinic = cursor.fetchone()

    return jsonify(clinic=clinic)


@app.route('/clinic/add', methods=['POST'])
def add_clinics():
    data = request.get_json()['clinics']
    cursor = conn.cursor()

    for d in data:
        sql = "INSERT INTO Clinic (clinic_name, address, open_time, close_time, contact_no, description, latitude, longitude, clinic_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.executemany(sql, (d['clinic_name'], d['address'], d['open_time'], d['close_time'], d['contact_no'], d['description'], d['latitude'], d['longitude'], 0,))

    return jsonify(message='success')


@app.route('/clinic/delete/<id>', methods=['GET'])
def delete_clinic(id):
    sql = "DELETE FROM clinic where id=%s"
    cursor = conn.cursor()
    cursor.execute(sql, (id,))

    return jsonify(message='success')