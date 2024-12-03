# menampilkan jumlah total jumlah barang yg sudah dilakukan pengadaan
SELECT kode_barang, 
SUM(jumlah) AS jumlah_brg,
(SELECT jumlah FROM detail_pengadaan
WHERE detail_pengadaan.kode_barang =
tbl_barang.kode_barang) AS jml_pengadaan
FROM tbl_barang;