# menghitung harga tiket
hari = input("Masukkan hari (senin-minggu): ").capitalize()
tiket = input("Pilih jenis tiket (anak-anak, dewasa, vip): ").upper()
jumlah = int(input("Masukkan jumlah tiket: "))


if hari in ["Senin", "Selasa", "Rabu", "Kamis"]:
    if tiket == "ANAK-ANAK":
        harga = 30000
    elif tiket == "DEWASA":
        harga = 50000
    elif tiket == "VIP":
        harga = 100000
    else:
        harga = None
elif hari in ["Jumat", "Sabtu", "Minggu"]:
    if tiket == "ANAK-ANAK":
        harga = 40000
    elif tiket == "DEWASA":
        harga = 70000
    elif tiket == "VIP":
        harga = 150000
    else:
        print("jenis tiket tidak valid")
        harga = None
else:
    harga = None   


if harga is not None:
    total_harga = harga * jumlah
    print(f"Harga tiket untuk {tiket} pada hari {hari} adalah Rp{harga}. Total harga untuk {jumlah} tiket adalah Rp{total_harga}.")
else:
    print("Input hari atau jenis tiket tidak valid. silahkan coba lagi.")    