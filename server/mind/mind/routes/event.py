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
                'event_id': r[0],
                'event_name': r[1],
                'event_desc': r[2],
                'event_url': r[3],
                'event_photo_url': r[4],
            })

    return jsonify(event=payload)