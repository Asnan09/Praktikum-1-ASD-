class Barang:
    def __init__(self, id_barang, nama, harga, stok, kategori):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori

class TokoBangunan:
    def __init__(self):
        self.barang_dict = {}

    def tambah_barang(self, barang):
        self.barang_dict[barang.id_barang] = barang

    def tampilkan_barang(self):
        print("Daftar Barang:")
        for id_barang, barang in self.barang_dict.items():
            print(f"ID: {id_barang}, Nama: {barang.nama}, Harga: {barang.harga}, Stok: {barang.stok}, Kategori: {barang.kategori}")

    def cari_barang(self, id_barang):
        if id_barang in self.barang_dict:
            barang = self.barang_dict[id_barang]
            print(f"ID: {id_barang}, Nama: {barang.nama}, Harga: {barang.harga}, Stok: {barang.stok}, Kategori: {barang.kategori}")
        else:
            print("Barang tidak ditemukan.")

    def update_barang(self, id_barang, field, value):
        if id_barang in self.barang_dict:
            barang = self.barang_dict[id_barang]
            if hasattr(barang, field):
                setattr(barang, field, value)
                print("Update berhasil.")
            else:
                print("Field tidak valid.")
        else:
            print("Barang tidak ditemukan.")

    def hapus_barang(self, id_barang):
        if id_barang in self.barang_dict:
            del self.barang_dict[id_barang]
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan.")

# Membuat objek toko
toko = TokoBangunan()

# Menambahkan beberapa barang ke dalam toko
toko.tambah_barang(Barang(1, "Cat Tembok", 50000, 100, "Cat"))
toko.tambah_barang(Barang(2, "Paku", 1000, 200, "Perkakas"))
toko.tambah_barang(Barang(3, "Semenn", 75000, 50, "Material Bangunan"))

# Menampilkan daftar barang
toko.tampilkan_barang()

# Mencari barang berdasarkan ID
toko.cari_barang(2)

# Update informasi barang
toko.update_barang(2, "harga", 1200)
toko.update_barang(3, "stok", 75)

# Hapus barang
toko.hapus_barang(1)

# Menampilkan daftar barang setelah modifikasi
toko.tampilkan_barang()
