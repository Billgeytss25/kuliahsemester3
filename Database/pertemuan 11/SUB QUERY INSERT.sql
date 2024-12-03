# ingin insert nama barang di tbl_barang 
# berasal dari tbl_pengadaan
INSERT INTO tbl_barang(kode_barang,
nama_barang, harga_jual,stok,harga_pengadaan)
SELECT detail_pengadaan.kode_barang,
"Pop Mie Pedass",
detail_pengadaan.jumlah
FROM detail_pengadaan
WHERE detail_pengadaan.kode_barang
NOT IN (SELECT kode_barang FROM tbl_barang)