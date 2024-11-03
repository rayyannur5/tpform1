# Penjelasan broker.py
## Module/Libraries
- socket => digunakan untuk jaringan komputer
- threading => digunakan untuk multithreading (multi proses dalam satu aplikasi) / asynchronous
- argpase => digunakan untuk parsing environment variable
- datetime => digunakan untuk mendapatkan waktu 
## Methods
### handleclient()
#### parameter
1. client_conn => koneksi klien dan membawa request dari klien
2. client_addr => address klien
#### flow
1. Membaca request clien
2. Percabangan strategi memilih worker, opsi even/round robin. jika even maka akan dicari worker dengan request paling kecil. sedangkan round robin akan bergantian secara berurutan dari worker paling awal hingga akhir
3. membuat socket ke worker
4. mengirimkan request client menuju worker
5. membaca response worker, lalu mengirimkan response ke client
5. menutup koneksi socket worker

### Main method
#### flow
1. membaca environment variable berupa host dan port. 
2. membuka socket pada port 80 / sesuai dengan port dari env. Pemilihan port 80 karena port tersebut digunakan pada koneksi HTTP.
3. membaca koneksi client dan melempar ke handleClient