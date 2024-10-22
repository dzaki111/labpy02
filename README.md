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

## Struktur Program
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
```
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

## Struktur Program
- **Input:**
  - Gaji (int)
  - Status berkeluarga (Y/T)
  - Status kepemilikan rumah (Y/T)
  
- **Output:**
  - Apakah gaji sudah di atas UMR atau belum
  - Kewajiban mengikuti asuransi jika sudah berkeluarga
  - Kewajiban membayar pajak rumah jika punya rumah

## Contoh Penggunaan
## gaji di atas UMR
```
Masukkan gaji: 3500000
Sudah berkeluarga? (Y/T): Y
Punya rumah? (Y/T): y

Gaji sudah diatas UMR
Wajib ikutan asuransi dan menabung untuk pensiun
Tidak wajib bayar pajak rumah
```
# berikut hasil screenshot visual studio code

![Screenshot 2024-10-22 112409](https://github.com/user-attachments/assets/d3dbfa6e-de98-43c6-b9f7-31b0e1fc9b68)

## gaji dibawah UMR
```
Masukkan gaji: 2500000
Sudah berkeluarga? (Y/T): y
Punya rumah? (Y/T): Y

Gaji belum UMR
Tidak wajib bayar pajak rumah
```
# berikut hasil screenshot visual studio code

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

## Struktur Program
- **Input:**
  - Bilangan A (int)
  - Bilangan B (int)
  - Bilangan C (int)
  
- **Output:**
  - "BENAR" jika salah satu dari kondisi penjumlahan dua bilangan sama dengan bilangan ketiga terpenuhi.
  - "SALAH" jika tidak ada kondisi penjumlahan yang terpenuhi.

## Contoh Penggunaan
```
Masukkan bilangan A: 3
Masukkan bilangan B: 5
Masukkan bilangan C: 8

BENAR
```
Pada contoh di atas, program mencetak "BENAR" karena A + B = C (3 + 5 = 8).

```
Masukkan bilangan A: 4
Masukkan bilangan B: 6
Masukkan bilangan C: 10

BENAR
```
Pada contoh ini, program mencetak "BENAR" karena A + B = C (4 + 6 = 10).

```
Masukkan bilangan A: 1
Masukkan bilangan B: 2
Masukkan bilangan C: 5

SALAH
```
## beriku screenshot visual studio code 

![Screenshot 2024-10-22 114110](https://github.com/user-attachments/assets/ef996678-ac15-40cd-bea3-5d968110639d)

Di sini, program mencetak "SALAH" karena tidak ada kombinasi A + B, B + C, atau C + A yang sama dengan salah satu bilangan lainnya.

## Penjelasan
- Program menerima tiga bilangan sebagai input dari pengguna.
- Program menggunakan operator logika **or** untuk mengecek apakah salah satu dari tiga kemungkinan penjumlahan (A + B = C, B + C = A, atau C + A = B) benar.
- Jika salah satu kondisi tersebut benar, program mencetak "BENAR", dan jika tidak, mencetak "SALAH".

