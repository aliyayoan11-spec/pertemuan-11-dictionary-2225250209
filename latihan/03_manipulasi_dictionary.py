data = {"nama": "Ayu", "nilai": 85}
data["kelas"] = "A"       # Menambah data baru
data["nilai"] = 90        # Mengubah value
print(data)
data.pop("kelas")         # Menghapus key
print(data)