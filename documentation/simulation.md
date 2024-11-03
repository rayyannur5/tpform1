# Simulasi Percobaan Simple Load Balancer
## Run Worker server
> python worker.py --port 5001
> python worker.py --port 5002
> python worker.py --port 5003
## Run Broker server
opsional env --port. Nilai default 80 (HTTP port)
> python broker.py
## Run client 
### menggunakan program
> python client.py --id long/short --loop 20

melakukan request ke server dengan iterasi yang ditentukan
##### Tampilan terminal client
![terminal client](../images/simulation-pic-01.png)
gambar diatas menampilkan 20 request ke server dengan jenis proses short sebanyak 20 kali. Dapat dilihat worker yang memproses bergantian antara 5001, 5002, atau 5003.
##### Tampilan broker
![terminal client](../images/simulation-pic-02.png)
##### Tampilan worker 0 (port 5001)
![terminal client](../images/simulation-pic-03.png)
##### Tampilan worker 1 (port 5002)
![terminal client](../images/simulation-pic-04.png)
##### Tampilan worker 2 (port 5003)
![terminal client](../images/simulation-pic-05.png)

### menggunakan web browser
##### Tampilan web browser
![alt text](../images/simulation-browser-1.png)
##### Tampilan broker
![alt text](../images/simulation-browser-2.png)
Muncul dua request baru pada worker 1 dan 2. Request pertama merupakan get ke favicon.ico, maka tidak dilanjutkan prosesnya. Sedangkan worker index kedua yaitu port 5003 yaitu request get ke localhost/appID=long, maka akan di proses dan akan memberikan response yang bisa dilihat ditampilan website
