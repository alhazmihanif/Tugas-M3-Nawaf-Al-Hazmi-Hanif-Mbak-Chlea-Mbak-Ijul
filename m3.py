#Soal No 1
print("Soal No 1")#
nama=input("Masukkan nama Anda: ")
usia= int(input("Masukkan usia Anda: "))
alamat=input("Masukkan alamat Anda: ")
print("Nama:", nama)
print("Usia:", usia)
print("Alamat:", alamat)
#Soal No 2
print("Soal No 2")
modalawal= float(input('Mau Nge-modal berape pruy? '))
targetkeuntungan= modalawal*20/100
print("Target keuntungan:",targetkeuntungan)
#Soal No 3
print("Soal No 3")
tanggal=input("Sekarang tanggal berape pruy? ")
bulan=input("Sekarang bulan ape pruy? ")
tahun=input("Sekarang tahun berape pruy? ")
print(tanggal, bulan, tahun, sep="-")
#Soal No 4
print("Soal No 4")
print('ID \t Produk \t Harga')
print('-'*36)
#Soal No 5
print("Soal No 5")
barang = "Kalkulator Saintifik"
harga = 245000.5
print(f"Harga {barang} adalah Rp{harga:,.2f}")
#Soal No 6
print("Soal No 6")
lebar = 65  
def garis(karakter="="):
    print(karakter * lebar)

def baris(teks):
    # otomatis pas-in border kiri-kanan
    print(f"| {teks:<{lebar - 4}} |")

def main():
    print("=== INPUT DATA MAHASISWA ===\n")

    nama = input("1. Nama Lengkap      : ")
    usia = int(input("2. Usia (tahun)      : "))
    kontak = input("3. No. Kontak/HP     : ")
    alamat = input("4. Alamat Asal       : ")
    kampus = input("5. Kampus            : ")
    fakultas = input("6. Fakultas          : ")
    prodi = input("7. Program Studi     : ")
    nrp = input("8. NRP               : ")
    angkatan = int(input("9. Angkatan (tahun)  : "))       
    sks = int(input("10. Jumlah SKS       : "))            
    matkul = input("11. Mata Kuliah      : ")
    dream_job = input("12. Target Karier    : ")

    # CETAK DASHBOARD
    print()
    garis("=")
    baris("DASBOR PROFIL MAHASISWA & RENCANA KARIER".center(lebar - 4))
    garis("=")

    baris("INFORMASI PERSONAL")
    garis("-")
    baris(f"Nama Lengkap    : {nama}")
    baris(f"Usia & Kontak   : {usia} Tahun | {kontak}")
    baris(f"Alamat Asal     : {alamat}")
    garis("-")

    baris("INFORMASI AKADEMIK")
    garis("-")
    baris(f"Kampus          : {kampus}")
    baris(f"Fakultas / Dept : {fakultas} / {prodi}")
    baris(f"NRP / Angkatan  : {nrp}   / {angkatan}")
    baris(f"SKS & Matkul    : {sks} SKS | {matkul}")
    garis("=")

    baris("TARGET KARIER (DREAM JOB)".center(lebar - 4))
    baris(dream_job.upper().center(lebar - 4))
    garis("=")
if __name__ == "__main__":
    main()

