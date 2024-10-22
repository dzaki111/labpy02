# labpy02

#### Nama   = DZAKI ARIF RAHMAN  
#### Kelas  = TI.24.A4  
#### NIM    = 312410312  
#### Matkul = BAHASA PEMOGRAMAN

# screenshot visual studio code

![Screenshot 2024-10-22 104107](https://github.com/user-attachments/assets/0a2f2536-b124-497b-9627-2b8759364776)

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
Nilai Akhir: 81.0

Nilai Huruf : A
Keterangan: LULUS
```

## Penjelasan
- **Tugas, UTS, dan UAS** dimasukkan oleh pengguna sebagai input dengan tipe `float`.
- Nilai akhir dihitung menggunakan bobot tertentu (20% tugas, 40% UTS, 40% UAS).
- Berdasarkan nilai akhir, program menentukan nilai huruf dan keterangan kelulusan.
