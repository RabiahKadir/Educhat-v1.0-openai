<!DOCTYPE html>
<html>
<head>
    <title>Silahkan Input Text</title>
</head>
<body>
    <h1>Silahkan Input Text</h1>
    <form method="post">
        <textarea name="input"></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
    <?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        // Ambil input teks dari form
        $input = $_POST['input'];
        // Jalankan program Python dengan argumen berupa input teks
        $output = exec("python input.py " . escapeshellarg($input));
        // Tampilkan output dari program Python
        echo "<p>" . htmlspecialchars($output) . "</p>";
    }
    ?>
</body>
</html>
