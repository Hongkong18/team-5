from flask import jsonify, request
from mind import app
from mind import conn


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


@app.route('/clinic/address/<address>', methods=['GET'])
def get_clinics_by_address(address):
    cursor = conn.cursor()
    address = '%' + address + '%'
    cursor.execute("SELECT * from clinic_tbl where address like %s", address)
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



@app.route('/clinic/name/<clinic_name>', methods=['GET'])
def get_clinics_by_name(clinic_name):
    cursor = conn.cursor()
    clinic_name = '%' + clinic_name + '%'
    cursor.execute("SELECT * from clinic_tbl where clinic_name like %s", clinic_name)
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


@app.route('/clinic/type/<type>', methods=['GET'])
def get_clinics_by_type(type):
    cursor = conn.cursor()
    type = '%' + type + '%'
    cursor.executemany("SELECT * from clinictype_tbl where type_en like %s or type_tc like %s or type_sc like %s", [type, type, type])
    result = cursor.fetchall()
    search = []
    for r in result:
        search.append(str(r[0]))

    cursor.executemany("SELECT * from clinic_tbl where clinic_id in (%s)", search)
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


@app.route('/clinic/id/<id>', methods=['GET'])
def get_clinic_by_id(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * from clinic_tbl where clinic_id=%s", id)
    r = cursor.fetchone()
    print(r)

    payload = [{
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
    }]

    return jsonify(clinic=payload)


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
    sql = "DELETE FROM clinic_tbl where clinic_id=%s"
    cursor = conn.cursor()
    cursor.execute(sql, (id,))

    return jsonify(message='success')
