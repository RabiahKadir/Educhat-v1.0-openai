<form method="post">
    Masukkan teks: <textarea  type="textarea" cols="30" name="teks"></textarea>
    <input type="submit" name="submit" value="Submit">
</form>

<?php
if(isset($_POST['submit'])) {
    $teks = $_POST['teks'];
    $pattern = "/\[(.*?)\]/"; // pola regular expression untuk mencari teks dalam kurung siku

    preg_match_all($pattern, $teks, $matches); // mencari semua teks dalam kurung siku

    if(empty($matches[1])) {
        // tidak ada tanda kurung siku
        echo "Tidak ada teks yang ditemukan.";
    } else {
        // menampilkan semua teks yang berada di dalam kurung siku
        echo "Teks Output adalah: <br>";
        foreach ($matches[1] as $teks_dalam_kurung) {
            echo $teks_dalam_kurung . "<br>";
        }
    }
}
?>
