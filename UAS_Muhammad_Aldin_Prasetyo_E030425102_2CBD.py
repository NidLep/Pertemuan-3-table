print("SISTEM PAKAR DENGAN POHON KEPUTUSAN MENGENAI MASALAH JARINGAN")
print("=============================================================")
print("Jawab dengan 'y' (Ya) atau 't' (Tidak)")

a9 = input("Apakah Ping IP Publik OK? (y/t) : ").lower()
if a9 == "y":
    a16 = input("Apakah Koneksi jaringan pusat ke jaringan lokal OK? (y/t) : ").lower()
    if a16 == "y":
        a14 = input("Apakah Port Squid pada Server Proxy OK? (y/t) : ").lower()
        if a14 == "y":
            a3 = input("Apakah MySQL pada Load Balancer OK? (y/t) : ").lower()   
            if a3 == "y":
                a5 = input("Apakah Port Lighttpd pada Load Blancer OK? (y/t) : ").lower()               
                if a5 == "y":
                    a2 = input("Apakah Login Captive Portal OK? (y/t) : ").lower()               
                    if a2 == "y":
                        a7 = input("apakah Domain publik OK? (y/t) : ").lower()                  
                        if a7 == "y":
                            print("Kesimpulan : Tidak ada masalah pada jaringan")
                        else:
                            print("Ada masalah pada DNS Publik")    
                    else:
                        a1 = input("Apakah Captive Portal OK? (y/t) : ").lower()                   
                        if a1 == "y":
                            print("Ada masalah pada LDAP")
                        else:
                            print("Ada masalah pada DNS Publik")    
                else:
                    print("Ada masalah pada Load Balancer/Captive Portal")
            else:
                a7 = input("apakah Domain publik OK? (y/t) : ").lower()             
                if a7 == "y":
                    a1 = input("Apakah Captive Portal OK? (y/t) : ").lower()              
                    if a1 == "y":
                        print("Ada masalah pada Load Balancer/Captive Portal")
                    else:
                        a4 = input("Apakah IP Load Balancer OK? (y/t) : ").lower()                   
                        if a4 == "y":
                            print("Ada Kesalahan pengaturan pada client, coba cek pengaturan IP Client")
                        else:
                            print("Ada masalah pada Load Balancer/Captive Portal")
                else:
                    print("Ada Kesalahan pengaturan pada client, coba cek pengaturan IP Client")
        else:
            print("Ada masalah pada Proxy")
    else:
        print("Ada masalah pada Firewall")
else:   
    a1 = input("Apakah Captive Portal OK? (y/t) : ").lower() 
    if a1 == "y":
        print("Ada Masalah pada ISP/Provider")
    else:
        a16 = input("Apakah Koneksi jaringan pusat ke jaringan lokal OK? (y/t) : ").lower()   
        if a16 == "y":
            a17 = input("Apakah Ping Gateway OK? (y/t) : ").lower()         
            if a17 == "y":
                print("Ada Masalah pada Router/Switch")
            else:
                print("Ada Kesalahan pengaturan pada client, coba cek pengaturan IP Client")
        else:
            print("Antara jaringan client dengan jaringan pusat terputus, coba cek koneksi jaringan client ke jaringan pusat")