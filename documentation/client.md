# Penjelasan client.py
## Module/Libraries
- socket => digunakan untuk jaringan komputer
- subprocess => digunakan untuk menjalankan perintah terminal dengan output
- argpase => digunakan untuk parsing environment variable
- datetime => digunakan untuk mendapatkan waktu 
## Methods
### execute()
#### parameter
1. command => perintah terminal
flow
1. Menjalankan subprocess dengan command dan decode(). decode artinya mengubah binary menjadi data string.
### main method
flow
1. parsing environment variable berupa appID dan loop
2. looping berdasarkan variable loop
3. melakukan eksekusi terminal curl ip-broker?appID={appID} // menggunakan queryParameter GET

