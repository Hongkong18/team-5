from flask import jsonify, request
from mind import app
from mind import conn

@app.route('/user', methods=['GET'])
def get_users():
    # data = request.get_json()

    cursor = conn.cursor()
    cursor.execute("SELECT * from user_tbl")
    result = cursor.fetchall()
    print(result)
    payload = []
    for r in result:
        payload.append({
                'user_id': r[0],
                'age_range': r[1],
                'gender': r[2],
                'myself': r[3]
            })

    return jsonify(user=payload)