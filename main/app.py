from flask import Flask , render_template
import requests

app = Flask(__name__)

#layanan karyawan

def get_karyawan():
    response = requests.get('http://127.0.0.1:5002/karyawan')
    return response.json()

#layanan poliklink
def get_poli():
    response = requests.get('http://127.0.0.1:5001/poliklinik')
    return response.json()

def get_dokter():
    response = requests.get('http://127.0.0.1:5001/dokter')
    return response.json()

def get_jadwal():
    response = requests.get('http://127.0.0.1:5001/jadwaldokter')
    return response.json()

#layanan aset dan obat

def get_obat():
    response = requests.get('http://127.0.0.1:5004/showobat')
    return response.json()

def get_aset():
    response = requests.get('http://127.0.0.1:5003/showaset')
    return response.json()

#layanan pasien

def get_pasien():
    response = requests.get('http://localhost:5005/pasien')
    return response.json()

#layanan medrec
def get_medrec():
    response = requests.get('http://localhost:5006/medrec')
    return response.json()

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/adminpage')
def admin():
    return render_template('index.html')

@app.route('/karyawan')
def showkaryawan():
    kar = get_karyawan()
    return render_template('karyawan.html', kar=kar)

@app.route('/poliklinik')
def showpoli():
    pol = get_poli()
    return render_template('poliklinik.html',pol=pol)

@app.route('/poliklinik/dokter')
def dokter():
    dok = get_dokter()
    jad = get_jadwal()
    return render_template('dokter.html',dok=dok,jad=jad)

@app.route('/obat')
def showobat():
    obaat = get_obat()
    return render_template('obat.html',obaat=obaat)

@app.route('/aset')
def showaset():
    aset = get_aset()
    return render_template('aset.html',aset=aset)

@app.route('/pasien')
def showpasien():
    pas = get_pasien()
    return render_template('pasien.html',pas=pas)

@app.route('/medrec')
def showmedrec():
    medic = get_medrec()
    return render_template('medrec.html',medic=medic)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000) 