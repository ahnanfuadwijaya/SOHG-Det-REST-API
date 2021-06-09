#main.py
import json, datetime
from flask import Flask, jsonify, request
from db import get_detections, open_connection

app = Flask(__name__)

datas = {"status" : 200, "Info" : "Testing Json"}
info = datetime.datetime.now()

@app.route('/', methods= ['POST'])
def testing():
    deteksi = request.args.get('detection')
    if request.method == 'POST':
        if deteksi == 'pistol':
            conn = open_connection()
            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO objects (date, time, detection) VALUES(%s, %s, %s)', (info.strftime("%x"), info.strftime("%X"), deteksi))
            conn.commit()
            conn.close()
            return 'Berhasil ditambahkan'
        if deteksi == 'knife':
            conn = open_connection()
            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO objects (date, time, detection) VALUES(%s, %s, %s)', (info.strftime("%x"), info.strftime("%X"), deteksi))
            conn.commit()
            conn.close()
            return 'Berhasil ditambahkan'


@app.route('/data', methods= ['GET'])
def testing():
    return json.dumps(get_detections())  

if __name__ == '__main__':
    app.run(debug=True)
