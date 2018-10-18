from flask import jsonify, request
from mind import app
from mind import conn

@app.route('/event', methods=['GET'])
def get_events():
    # data = request.get_json()

    cursor = conn.cursor()
    cursor.execute("SELECT * from event_tbl")
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

    return jsonify(event=payload)