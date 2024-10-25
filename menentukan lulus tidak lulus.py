
nama = input("Masukkan nama: ")
uts = float(input("Masukkan nilai UTS: ")) 
uas = float(input("Masukkan nilai UAS: ")) 
tugas = float(input("Masukkan nilai Tugas: "))  


akhir = (tugas * 0.2) + (uts * 0.4) + (uas * 0.4)

keterangan = "LULUS" if akhir > 60.0 else "TIDAK LULUS"

if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

print("\nNama :", nama)
print("Nilai UTS :", uts)
print("Nilai UAS :", uas)
print("Nilai Tugas:", tugas)
print("Nilai Akhir:", akhir)
print("\nNilai Huruf :", huruf)
print("Keterangan:", keterangan)
