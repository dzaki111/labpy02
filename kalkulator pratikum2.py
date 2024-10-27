angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ").strip()
angka2 = float(input("Masukkan angka kedua: "))

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

print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")
