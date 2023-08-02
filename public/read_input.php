<?php
// Jalankan perintah Python dengan argumen berupa nama file dan simpan keluarannya ke variabel $output
$filename = 'input.txt';
$output = exec("python input.py $filename");
echo $output; // Tampilkan keluaran Python
?>
