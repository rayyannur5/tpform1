# Penjelasan broker.py
## Module/Libraries
- socket => digunakan untuk jaringan komputer
- time => digunakan untuk menjeda program, berfungsi menyimulasikan proses panjang dan pendek
- urllib.parse => digunakan untuk parsing url query parameter
- argpase => digunakan untuk parsing environment variable
- datetime => digunakan untuk mendapatkan waktu 
## Methods
### main method
flow
1. membaca environment variable
2. membuka server socket dengan port sesuai dengan env
3. membaca request dari broker
4. parsing url query parameter untuk mendapatkan jenis proses yang akan dijalankan
5. Melakukan proses
6. memberikan response berupa HTTP response 200 dengan body hello world dan worker yang berjalan melakukan proses tersebut
