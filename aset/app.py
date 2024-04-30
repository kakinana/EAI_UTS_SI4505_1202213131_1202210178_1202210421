from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from datetime import datetime


app = Flask(__name__)

#MySQLconfig
app.config['MYSQL_HOST'] = 'mysql-19d09cf6-dharu-4c33.d.aivencloud.com'
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_zVuKoNmfyrV6gpVNMuN'
app.config['MYSQL_DB'] = 'utseai'
app.config['MYSQL_PORT'] = 16228
mysql = MySQL(app)


@app.route('/showaset')
def showaset():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM aset")
    
    column_name = [i[0] for i in cursor.description]

    # obat = cursor.fetchall()
    data =[]
    for row in cursor.fetchall():
        data.append(dict(zip(column_name,row)))

    cursor.close()
    return jsonify(data)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug = True)