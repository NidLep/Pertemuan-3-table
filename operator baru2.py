# menghitung nilai akhir
tugas = int(input("masukkan nilai tugas: "))
uas = int(input("masukkan nilai uas: "))
praktikum = int(input("masukkan nilai praktikum: "))

nilai_akhir = (tugas * 0.2) + (uas * 0.3) + (praktikum * 0.5)

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 75:
    grade = "B"
elif nilai_akhir >= 60:
    grade = "C"
else:
    grade = "D/E (Tidak lulus)"

print(f"nilai akhir anda = {nilai_akhir}")
print(f"grade: {grade}")