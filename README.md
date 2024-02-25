class Barang:
    def __init__(self, id_barang, nama, harga, stok, kategori):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori

    def __str__(self):
        return f"ID: {self.id_barang}, Nama: {self.nama}, Harga: {self.harga}, Stok: {self.stok}, Kategori: {self.kategori}"

class TokoBangunan:
    def __init__(self): 
        self.barang_list = []

    def tambah_barang(self, barang):
        self.barang_list.append(barang)

    def tampilkan_barang(self):
        print("Daftar Barang:")
        for i, barang in enumerate(self.barang_list):
            print(f"{i+1}. {barang}")

    def cari_barang(self, id_barang):
        for i, barang in enumerate(self.barang_list):
            if barang.id_barang == id_barang:
                return i
        return -1

    def update_barang(self, id_barang, field, value):
        index = self.cari_barang(id_barang)
        if index != -1:
            if hasattr(self.barang_list[index], field):
                setattr(self.barang_list[index], field, value)
                print("Update berhasil.")
            else:
                print("Field tidak valid.")
        else:
            print("Barang tidak ditemukan.")

    def hapus_barang(self, id_barang):
        index = self.cari_barang(id_barang)
        if index != -1:
            del self.barang_list[index]
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan.")


toko = TokoBangunan()


toko.tambah_barang(Barang(1, "Cat Tembok", 50000, 100, "Cat"))
toko.tambah_barang(Barang(2, "Paku", 1000, 200, "Perkakas"))
toko.tambah_barang(Barang(3, "Semenn", 75000, 50, "Material Bangunan"))


toko.tampilkan_barang()


index = toko.cari_barang(2)
if index != -1:
    print(toko.barang_list[index])

toko.update_barang(2, "harga", 1200)
toko.update_barang(3, "stok", 75)


toko.hapus_barang(1)
