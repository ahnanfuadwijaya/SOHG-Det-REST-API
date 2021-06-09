#db.py
import os
import pymysql
from flask import jsonify


def open_connection():
    try:
        conn = pymysql.connect(host={Host_Name},
                         user={User_Name},
                         password={Password},
                         db={Database_name},
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_detections():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM objects;')
        detections = cursor.fetchall()
        if result > 0:
            got_detections = detections
        else:
            got_detections = 'No object detections in DB'
    conn.close()
    return got_detections
