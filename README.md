# labpy02
#### Nama   = DZAKI ARIF RAHMAN  
#### Kelas  = TI.24.A4  
#### NIM    = 312410312  
#### Matkul = BAHASA PEMOGRAMAN

# LATIHAN 1
# Program Perhitungan Nilai Akhir Siswa

## Deskripsi
Program ini menerima input nilai UTS (Ujian Tengah Semester), UAS (Ujian Akhir Semester), dan nilai tugas dari pengguna, 
kemudian menghitung nilai akhir siswa berdasarkan bobot tertentu:
- 20% untuk nilai tugas
- 40% untuk nilai UTS
- 40% untuk nilai UAS

Program ini juga menampilkan nilai huruf berdasarkan nilai akhir, serta menentukan apakah siswa "LULUS" atau "TIDAK LULUS" 
berdasarkan kriteria nilai akhir.

## Cara Kerja Program
1. Program meminta input dari pengguna untuk nama, nilai UTS, nilai UAS, dan nilai tugas.
2. Program kemudian menghitung nilai akhir dengan rumus:
   ```
   akhir = (nilai_tugas * 0.2) + (nilai_uts * 0.4) + (nilai_uas * 0.4)
   ```
3. Setelah nilai akhir dihitung, program menentukan keterangan "LULUS" atau "TIDAK LULUS" dengan syarat:
   - **LULUS** jika nilai akhir lebih dari 60.
   - **TIDAK LULUS** jika nilai akhir kurang dari atau sama dengan 60.
   
4. Program juga mengonversi nilai akhir menjadi nilai huruf dengan kriteria:
   - **A** jika nilai akhir lebih dari 80
   - **B** jika nilai akhir lebih dari 70
   - **C** jika nilai akhir lebih dari 50
   - **D** jika nilai akhir lebih dari 40
   - **E** jika nilai akhir kurang dari atau sama dengan 40

5. Program kemudian mencetak hasilnya ke layar.

## contoh input dan output
- **Input:**
  - Nama siswa
  - Nilai UTS (float)
  - Nilai UAS (float)
  - Nilai Tugas (float)
  
- **Output:**
  - Nama siswa
  - Nilai UTS
  - Nilai UAS
  - Nilai Tugas
  - Nilai Akhir
  - Nilai Huruf
  - Keterangan ("LULUS" atau "TIDAK LULUS")

## Contoh Penggunaan
```python
Masukkan nama: Budi
Masukkan nilai UTS: 75
Masukkan nilai UAS: 85
Masukkan nilai Tugas: 80

Nama : Budi
Nilai UTS : 75.0
Nilai UAS : 85.0
Nilai Tugas: 80.0
Nilai Akhir: 80.0

Nilai Huruf : B
Keterangan: LULUS
```
## screenshot visual studio code

![Screenshot 2024-10-22 105052](https://github.com/user-attachments/assets/bf968f14-87b8-472c-9ac6-d18f8ba454f8)

## Penjelasan
- **Tugas, UTS, dan UAS** dimasukkan oleh pengguna sebagai input dengan tipe `float`.
- Nilai akhir dihitung menggunakan bobot tertentu (20% tugas, 40% UTS, 40% UAS).
- Berdasarkan nilai akhir, program menentukan nilai huruf dan keterangan kelulusan.

# LATIHAN 2
# Program Pengecekan Gaji, Status Keluarga, dan Kepemilikan Rumah

## Deskripsi
Program ini menerima input gaji, status keluarga (sudah berkeluarga atau belum), dan status kepemilikan rumah dari pengguna, 
kemudian melakukan beberapa pengecekan sebagai berikut:
1. Apakah gaji di atas UMR (Upah Minimum Regional).
2. Jika gaji di atas UMR, program akan mengecek apakah pengguna sudah berkeluarga untuk menentukan kewajiban mengikuti asuransi dan menabung.
3. Program juga mengecek apakah pengguna memiliki rumah untuk menentukan kewajiban membayar pajak rumah.

## Cara Kerja Program
1. Program meminta input dari pengguna untuk gaji, status berkeluarga, dan status kepemilikan rumah.
2. Jika gaji lebih dari 3.000.000, program akan mencetak "Gaji sudah di atas UMR". Jika tidak, akan mencetak "Gaji belum UMR".
3. Jika pengguna sudah berkeluarga, program akan mencetak "Wajib ikutan asuransi dan menabung untuk pensiun", 
   namun jika belum berkeluarga, akan mencetak "Tidak perlu ikutan asuransi".
4. Jika pengguna memiliki rumah, program akan mencetak "Wajib bayar pajak rumah". Jika tidak memiliki rumah, 
   akan mencetak "Tidak wajib bayar pajak rumah".

## contoh input output
- **Input:**
  - Gaji (int)
  - Status berkeluarga (Y/T)
  - Status kepemilikan rumah (Y/T)
  
- **Output:**
  - Apakah gaji sudah di atas UMR atau belum
  - Kewajiban mengikuti asuransi jika sudah berkeluarga
  - Kewajiban membayar pajak rumah jika punya rumah

## Contoh Penggunaan
# gaji di atas UMR
```python
Masukkan gaji: 3500000
Sudah berkeluarga? (Y/T): Y
Punya rumah? (Y/T): y

Gaji sudah diatas UMR
Wajib ikutan asuransi dan menabung untuk pensiun
Tidak wajib bayar pajak rumah
```
## berikut hasil screenshot visual studio code

![Screenshot 2024-10-22 112409](https://github.com/user-attachments/assets/d3dbfa6e-de98-43c6-b9f7-31b0e1fc9b68)

# gaji dibawah UMR
```python
Masukkan gaji: 2500000
Sudah berkeluarga? (Y/T): y
Punya rumah? (Y/T): Y

Gaji belum UMR
Tidak wajib bayar pajak rumah
```
## berikut hasil screenshot visual studio code

![Screenshot 2024-10-22 112111](https://github.com/user-attachments/assets/25b1a8a4-280a-4744-9ed3-cfa0c5f8d7b7)


## Penjelasan
- **Pengecekan berkeluarga dan punya rumah**: Variabel `berkeluarga` dan `punya_rumah` dicek dengan perbandingan input terhadap "Y" 
  menggunakan `input().strip().upper() == "Y"`, yang memastikan bahwa input diubah menjadi huruf kapital dan mengabaikan spasi yang tidak perlu.
- Program ini menggunakan `if-else` untuk menentukan pesan yang akan ditampilkan berdasarkan kondisi gaji, status keluarga, dan status kepemilikan rumah.

# LATIHAN 3
# Program Pengecekan Relasi Antara Tiga Bilangan

## Deskripsi
Program ini menerima input tiga bilangan A, B, dan C, kemudian melakukan pengecekan apakah jumlah dua bilangan dari tiga bilangan tersebut sama dengan bilangan ketiga.

## Cara Kerja Program
1. Program meminta input dari pengguna untuk tiga bilangan (A, B, dan C).
2. Program mengecek apakah salah satu dari kondisi berikut terpenuhi:
   - Apakah A + B = C?
   - Apakah B + C = A?
   - Apakah C + A = B?
3. Jika salah satu dari kondisi tersebut terpenuhi, program akan mencetak "BENAR". Jika tidak ada kondisi yang terpenuhi, program akan mencetak "SALAH".

## contoh input dan output
- **Input:**
  - Bilangan A (int)
  - Bilangan B (int)
  - Bilangan C (int)
  
- **Output:**
  - "BENAR" jika salah satu dari kondisi penjumlahan dua bilangan sama dengan bilangan ketiga terpenuhi.
  - "SALAH" jika tidak ada kondisi penjumlahan yang terpenuhi.

## Contoh Penggunaan
```python
Masukkan bilangan A: 3
Masukkan bilangan B: 5
Masukkan bilangan C: 8

BENAR
```
Pada contoh di atas, program mencetak "BENAR" karena A + B = C (3 + 5 = 8).

```python
Masukkan bilangan A: 4
Masukkan bilangan B: 6
Masukkan bilangan C: 10

BENAR
```
Pada contoh ini, program mencetak "BENAR" karena A + B = C (4 + 6 = 10).

```python
Masukkan bilangan A: 1
Masukkan bilangan B: 2
Masukkan bilangan C: 5

SALAH
```
Pada contoh ini, program mencetak "SALAH" karena A + B = C (1 + 2 = 5).
## beriku screenshot visual studio code 

![Screenshot 2024-10-22 114110](https://github.com/user-attachments/assets/ef996678-ac15-40cd-bea3-5d968110639d)

Di sini, program mencetak "SALAH" karena tidak ada kombinasi A + B, B + C, atau C + A yang sama dengan salah satu bilangan lainnya.

## Penjelasan
- Program menerima tiga bilangan sebagai input dari pengguna.
- Program menggunakan operator logika **or** untuk mengecek apakah salah satu dari tiga kemungkinan penjumlahan (A + B = C, B + C = A, atau C + A = B) benar.
- Jika salah satu kondisi tersebut benar, program mencetak "BENAR", dan jika tidak, mencetak "SALAH".

# KASUS 1 
# Program Pemesanan Tiket Bioskop

## Deskripsi
Program ini digunakan untuk menghitung total harga tiket bioskop berdasarkan tipe tiket yang dipilih oleh pengguna (reguler atau VIP) dan status keanggotaan (member atau bukan). Program ini mendukung pemberian diskon sebesar 20% untuk pengguna yang memiliki kartu member.

## Fitur Program
- **Dukungan untuk dua tipe tiket**: `reguler` (Rp50.000) dan `VIP` (Rp100.000).
- **Diskon khusus** untuk pemegang kartu member, yaitu diskon sebesar 20% dari harga tiket.
- **Penghitungan otomatis** harga total berdasarkan tipe tiket dan status member pengguna.

## Petunjuk Penggunaan

1. **Masukkan tipe tiket**:
   - Ketik `reguler` jika Anda ingin membeli tiket reguler.
   - Ketik `vip` jika Anda ingin membeli tiket VIP.
   
2. **Masukkan status member**:
   - Ketik `ya` jika Anda memiliki kartu member.
   - Ketik `tidak` jika Anda tidak memiliki kartu member.
   
3. Program akan menampilkan **total harga tiket** yang harus dibayar, setelah menghitung diskon jika berlaku.

## cara kerja program

### 1. Variabel Harga
```python
harga_tiket_reguler = 50000
harga_tiket_vip = 100000
diskon_member = 0.20
```
Variabel ini digunakan untuk menyimpan harga tiket reguler, harga tiket VIP, dan persentase diskon bagi pengguna dengan kartu member.

### 2. Meminta Input Pengguna
```python
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()
```
Kode di atas meminta pengguna untuk memasukkan tipe tiket dan status member. Input pengguna diubah menjadi huruf kecil agar validasi lebih mudah.

### 3. Pemilihan Harga Tiket
```python
if tipe_tiket == "reguler":
    harga_tiket = harga_tiket_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_tiket_vip
else:
    print("Tipe tiket tidak valid.")
    exit()
```
Bagian ini menentukan harga tiket berdasarkan input tipe tiket. Jika tipe tiket tidak valid, program akan menampilkan pesan kesalahan dan berhenti.

### 4. Menghitung Total Harga dengan Diskon (Jika Berlaku)
```python
total_harga = harga_tiket * (1 - diskon_member) if status_member == "ya" else harga_tiket
```
Menggunakan operator ternary, kode ini menghitung total harga:
- Jika pengguna memiliki kartu member (`ya`), harga tiket akan dikalikan dengan `(1 - diskon_member)`.
- Jika tidak memiliki kartu member, harga tiket tetap.

### 5. Menampilkan Total Harga
```python
print(f"Total harga yang harus dibayar: Rp{total_harga:,}")
```
Bagian ini menampilkan total harga tiket dalam format rupiah.

# Contoh input dan Output TIKET REGULER

- **Input**:
  ```python
  Masukkan tipe tiket (reguler/vip): reguler
  Apakah Anda memiliki kartu member? (ya/tidak): ya
  ```
- **Output**:
  ```python
  Total harga yang harus dibayar: Rp40,000
  ```
## hasil screenshot vsc

![Screenshot 2024-10-25 153050](https://github.com/user-attachments/assets/af3b09fa-35bf-4fd4-9364-648d076aefd6)

# Contoh input dan Output TIKET VIP 

- **Input**:
  ```python
  Masukkan tipe tiket (reguler/vip): vip
  Apakah Anda memiliki kartu member? (ya/tidak): ya
  ```
- **Output**:
  ```python
  Total harga yang harus dibayar: Rp80,000
  ```
## hasil screenshot vsc

![Screenshot 2024-10-25 153151](https://github.com/user-attachments/assets/d179dabc-5924-4c08-92db-ffbe1d6f9c7d)

## Cara Menjalankan Program
1. Pastikan Python telah terinstal di sistem Anda.
2. Simpan kode di atas dalam file `tiket_bioskop.py`.
3. Buka terminal atau command prompt, navigasikan ke folder tempat file disimpan, lalu jalankan perintah:
   ```bash
   python tiket_bioskop.py
   ```
## FLOWCHARTNYA

![Screenshot 2024-10-26 172000](https://github.com/user-attachments/assets/affa24f1-e80a-4ba0-8e10-f947004f5a5c)

# KASUS 2
# Program Kalkulator Sederhana

Program ini adalah kalkulator sederhana yang dapat melakukan empat operasi aritmatika dasar: penjumlahan, pengurangan, perkalian, dan pembagian. Pengguna hanya perlu memasukkan dua angka dan memilih operator, dan program akan menampilkan hasil perhitungan.

## Fitur Program
- Mendukung empat operasi aritmatika:
  - **Penjumlahan** (`+`)
  - **Pengurangan** (`-`)
  - **Perkalian** (`*`)
  - **Pembagian** (`/`)
- **Validasi pembagian dengan nol** untuk mencegah kesalahan saat melakukan operasi pembagian.

## Cara Menggunakan Program
1. Masukkan angka pertama saat diminta.
2. Pilih operator aritmatika dari pilihan berikut: `+`, `-`, `*`, `/`.
3. Masukkan angka kedua saat diminta.
4. Program akan menghitung hasil sesuai operator dan menampilkan hasilnya di layar.

## Struktur Kode dan Penjelasan

### 1. Input dari Pengguna
```python
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ").strip()
angka2 = float(input("Masukkan angka kedua: "))
```
Bagian ini meminta pengguna untuk memasukkan dua angka (`angka1` dan `angka2`) serta operator aritmatika yang diinginkan. `input()` mengambil data dari pengguna, dan `float()` mengonversi input menjadi angka desimal.

### 2. Memilih Operasi dengan Struktur `if-elif-else`
```python
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
        exit()
    hasil = angka1 / angka2
else:
    print("Operator tidak valid.")
    exit()
```
Bagian ini menggunakan struktur `if-elif-else` untuk menentukan operasi berdasarkan operator yang dimasukkan pengguna:
- `+` untuk penjumlahan.
- `-` untuk pengurangan.
- `*` untuk perkalian.
- `/` untuk pembagian. Sebelum melakukan pembagian, program memeriksa jika `angka2` adalah nol untuk menghindari kesalahan.

### 3. Menampilkan Hasil
```python
print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")
```
Setelah operasi selesai, hasil perhitungan ditampilkan dalam format yang mudah dibaca.

## Contoh input dan Output PENJUMLAHAN

- **Input**:
  ```python
  Masukkan angka pertama: 10
  Masukkan operator (+, -, *, /): +
  Masukkan angka kedua: 5
  ```
- **Output**:
  ```python
  Hasil: 10 + 5 = 15.0
  ```
## Contoh input dan Output PENGURANGAN

- **Input**:
  ```python
  Masukkan angka pertama: 10
  Masukkan operator (+, -, *, /): -
  Masukkan angka kedua: 5
  ```
- **Output**:
  ```python
  Hasil: 10 - 5 = 5.0
  ```
## Contoh input dan Output PEKALIAN

- **Input**:
  ```[ython
  Masukkan angka pertama: 10
  Masukkan operator (+, -, *, /): *
  Masukkan angka kedua: 5
  ```
- **Output**:
  ```python
  Hasil: 10 * 5 = 50.0
  ```
## Contoh input dan Output PEMBAGIAN

- **Input**:
  ```python
  Masukkan angka pertama: 10
  Masukkan operator (+, -, *, /): /
  Masukkan angka kedua: 5
  ```
- **Output**:
  ```python
  Hasil: 10 / 5 = 2.0
  ```
  
## hasil screenshot vsc

![Screenshot 2024-10-27 154808](https://github.com/user-attachments/assets/5ac7e443-083b-4d33-87c6-f1448784a6e5)

## Cara Menjalankan Program
1. Pastikan Python telah terinstal di sistem Anda.
2. Simpan kode di atas dalam file bernama `kalkulator.py`.
3. Buka terminal atau command prompt, navigasikan ke folder tempat file disimpan, lalu jalankan perintah:
   ```bash
   python kalkulator pratikum2.py
   ```

## FLOWCHARTNYA

![Screenshot 2024-10-27 153830](https://github.com/user-attachments/assets/3d99b859-6ac9-4b99-b360-b53c130d5248)

