from flask import Flask, jsonify, request , render_template
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql-19d09cf6-dharu-4c33.d.aivencloud.com'
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_zVuKoNmfyrV6gpVNMuN'
app.config['MYSQL_DB'] = 'eai'
app.config['MYSQL_PORT'] = 16228

mysql = MySQL(app)

@app.route('/medrec', methods=['GET', 'POST'])
def pasien():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM medrec")
        kolom = [i[0] for i in cursor.description]
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(kolom, row)))
        cursor.close()
        return jsonify(data)
    
    elif request.method =='POST':
        nama = request.json['nama']
        birth = request.json['birth']
        address = request.json['address']
        disease = request.json['disease']
        handling = request.json['handling']
        medic = request.json['medicine_pat']
        time = request.json['timestamp']
        

        cursor = mysql.connection.cursor()
        sql = "INSERT INTO medrec (name_pat,birthdate_pat,address_pat,timestamp,disease,handling,medicine_pat) VALUES (%s,%s,%s,%s,%s,%s,%s)"

        val = (nama,birth,address,time,disease,handling,medic)
        cursor.execute(sql,val)

        mysql.connection.commit()

        return jsonify({'message':'data berhasil masuk'})
        cursor.close()
    

@app.route('/detailmedrec',methods =['GET'])
def detailpasien():
    if 'id' in request.args:
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM medrec WHERE id = %s"
        val = (request.args['id'])
        cursor.execute(sql,val)
        kolom = [i[0] for i in cursor.description]
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(kolom,row)))

        
        return jsonify(data)
        cursor.close()


@app.route('/editmedrec', methods = ['PUT'])
def editmedrec():
    if 'id' in request.args:
        data = request.get_json()

        cursor = mysql.connection.cursor()
        sql = "UPDATE medrec SET name_pat = %s, birthdate_pat = %s, address_pat = %s, timestap = %s, disease =%s, handling =%s ,medicine_pat =%s WHERE id = %s"
        val = (data['nama'],data['birth'],data['address'],data['time'],data['disease'],data['handling'],data['medicine_pat'],request.args['id'])
        cursor.execute(sql, val)
        mysql.connection.commit()
        cursor.close()  

        return jsonify({'message': 'data berhasil diubah'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5006, debug = True)