DELETE FROM tbl_detailtransaksi
WHERE qty > (
SELECT stok FROM tbl_barang)