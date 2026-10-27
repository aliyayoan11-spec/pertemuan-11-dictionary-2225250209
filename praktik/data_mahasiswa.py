def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# 1. Menyiapkan dictionary data_mahasiswa dengan NIM sebagai key utama
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 2. Uji pencarian mahasiswa
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)
if hasil:
    print(f"Pencarian {nim_cari}: {hasil}")
else:
    print("Data tidak ditemukan")

# 3. Menambahkan mahasiswa baru
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

# 4. Memperbarui nilai mahasiswa tertentu (A002 menjadi 82)
data_mahasiswa["A002"]["nilai"] = 82

# 5. Menampilkan seluruh data menggunakan items()
print("\n--- Rekap Seluruh Mahasiswa ---")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")

# 6. Menghitung rata-rata nilai kelas
rata = rata_rata_nilai(data_mahasiswa)
print(f"\nRata-rata nilai seluruh mahasiswa = {rata:.2f}")