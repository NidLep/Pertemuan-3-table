#dictionary hobi mahasiswa (nama sebagai key, hobi sebagai value)
hobi_mahasiswa = {
    "Rina": ["Membaca", "Menyanyi", "Berkebun"],
    "Agus": ["Olahraga", "Membaca", "Memasak"],
    "Dewi": ["Menyanyi", "Melukis", "Olahraga"],
}
semua_hobi_unik = set().union(*hobi_mahasiswa.values())
print("Hobi unik yang dimiliki oleh mahasiswa :", semua_hobi_unik)
print("banyak hobi unik yang dimiliki oleh mahasiswa :", len(semua_hobi_unik))
print("hobi apa saja yang dimiliki Rina dan Agus :", set(hobi_mahasiswa["Rina"]) & set(hobi_mahasiswa["Agus"]))
print("mahasiswa yang memiliki hobi Membaca :", [name for name, hobbies in hobi_mahasiswa.items() if "Membaca" in hobbies])