# Meminta pengguna untuk memasukkan jumlah data 
jumlah_data = int(input("Berapa banyak data yang ingin Anda masukkan? "))

# Inisialisasi daftar untuk menyimpan data
data_siswa = []

# Loop untuk meminta input nama dan nilai
for i in range(jumlah_data):
    print(f"\nData ke-{ i + 1 }")
    nama = input("Masukkan nama: ")
    nilai = float(input("Masukkan nilai: "))

    # Menentukan status lulus
    if nilai >= 60:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    # simpan data ke dalam list
    data_siswa.append({"nama": nama, "nilai": nilai, "status": status})

# Menampilkan data secara berulang
print("\nMenampilkan data siswa:")
while True:
    for siswa in data_siswa:
        print(f"Nama: {siswa['nama']}, Nilai: {siswa['nilai']}, Status: {siswa['status']}")
   
    # Cek apakah ingin menampilkan data lagi
    ulang = input("\nTampilkan data lagi? (ya/tidak): ").lower()
    if ulang != "ya":
        print("Program selesai.")
        break