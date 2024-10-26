harga_tiket_reguler = 50000
harga_tiket_vip = 100000
diskon_member = 0.20

tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

if tipe_tiket == "reguler":
    harga_tiket = harga_tiket_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_tiket_vip
else:
    print("Tipe tiket tidak valid.")
    exit()

total_harga = harga_tiket * (1 - diskon_member) if status_member == "ya" else harga_tiket

print(f"Total harga yang harus dibayar: Rp{total_harga:,}")
