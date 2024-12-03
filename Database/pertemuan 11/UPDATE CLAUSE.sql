# update stok tbl_baranng berdasarkan
# detail_pengadaan
UPDATE tbl_barang
SET stok = stok + (
SELECT IFNULL(SUM(jumlah),0)
FROM detail_pengadaan WHERE 
detail_pengadaan.kode_barang =
tbl_barang.kode_barang)