<?php
// membuat koneksi menggunakan database
$connect = mysqli_connect("localhost", "root", "", "sikampus");
if (!$connect) {
    die("Koneksi gagal: " . mysqli_connect_error());
} else {
    echo "Koneksi Berhasil";
}
