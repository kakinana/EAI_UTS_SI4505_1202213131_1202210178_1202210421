from flask import Flask, jsonify, request , render_template
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql-19d09cf6-dharu-4c33.d.aivencloud.com'
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_zVuKoNmfyrV6gpVNMuN'
app.config['MYSQL_DB'] = 'eai'
app.config['MYSQL_PORT'] = 16228

mysql = MySQL(app)

@app.route('/pasien', methods=['GET', 'POST'])
def pasien():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM pasien")
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
        blood = request.json['blood']
        

        cursor = mysql.connection.cursor()
        sql = "INSERT INTO pasien (name_pat,birthdate_pat,address_pat,bloodtype_pat) VALUES (%s,%s,%s,%s)"

        val = (nama,birth,address,blood)
        cursor.execute(sql,val)

        mysql.connection.commit()

        return jsonify({'message':'data berhasil masuk'})
        cursor.close()
    

@app.route('/detailpasien',methods =['GET'])
def detailpasien():
    if 'id' in request.args:
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM pasien WHERE id = %s"
        val = (request.args['id'])
        cursor.execute(sql,val)
        kolom = [i[0] for i in cursor.description]
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(kolom,row)))

        
        return jsonify(data)
        cursor.close()


@app.route('/editpasien', methods = ['PUT'])
def editmedrec():
    if 'id' in request.args:
        data = request.get_json()

        cursor = mysql.connection.cursor()
        sql = "UPDATE pasien SET name_pat = %s, birthdate_pat = %s, address_pat = %s, bloodtype_pat = %s WHERE id = %s"
        val = (data['nama'],data['birth'],data['address'],data['blood'],request.args['id'])
        cursor.execute(sql, val)
        mysql.connection.commit()
        cursor.close()  

        return jsonify({'message': 'data berhasil diubah'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5005, debug = True)