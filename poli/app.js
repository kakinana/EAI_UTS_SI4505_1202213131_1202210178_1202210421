const express = require('express')
const app = express()

const mysql = require('mysql');

// Buat koneksi ke database MySQL
const connection = mysql.createConnection({
    host: 'tugasduadwbi-tugasduadwbi.a.aivencloud.com',
    port: '22273',
    user: 'avnadmin',
    password: 'AVNS_ZDlr9ve2e04PDMAixdK',
    database: 'poli'
});

connection.connect((err) => {
    if (err) throw err;
    
});

// Endpoint /dokter dengan metode GET
app.get('/dokter', (req, res) => {
    // Jalankan query SQL untuk mengambil data dari tabel Dokter
    connection.query('SELECT dokter.nama_dokter, dokter.spesialisasi, poliklinik.nama_poliklinik FROM dokter INNER JOIN poliklinik ON dokter.id_poliklinik = poliklinik.id_poliklinik', (error, results, fields) => {
        if (error) {
            console.error('Error saat menjalankan query:', error);
            res.status(500).json({ error: 'Terjadi kesalahan saat mengambil data dari server' });
            return;
        }
        // Kirim data sebagai respons
        res.json(results);
    });
});

// Endpoint untuk mendapatkan data poliklinik
app.get('/poliklinik', (req, res) => {
    // Jalankan query untuk mengambil data dari tabel Poliklinik
    connection.query('SELECT * FROM poliklinik', (error, results, fields) => {
        if (error) {
            res.status(500).json({ error: 'Terjadi kesalahan dalam mengambil data dari database.' });
            return;
        }
        res.json(results); // Mengirimkan data poliklinik dalam bentuk JSON sebagai respons
    });
});

app.get('/jadwaldokter', (req, res) => {
    // Jalankan query untuk mengambil data dari tabel jadwaldokter
    connection.query('SELECT jadwal_dokter.*, dokter.nama_dokter FROM jadwal_dokter INNER JOIN dokter ON jadwal_dokter.id_dokter = dokter.id_dokter', (error, results, fields) => {
        if (error) {
            res.status(500).json({ error: 'Terjadi kesalahan dalam mengambil data dari database.' });
            return;
        }
        res.json(results); // Mengirimkan data jadwal dokter dalam bentuk JSON sebagai respons
    });
});

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
    console.log(`Server berjalan di port ${PORT}`);
});
