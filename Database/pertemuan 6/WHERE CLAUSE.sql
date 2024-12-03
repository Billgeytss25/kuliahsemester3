SELECT * FROM tbl_barang WHERE kode_supplier
IN ( SELECT kode_supplier FROM supplier
WHERE nama_supplier LIKE "PT.ABC%")