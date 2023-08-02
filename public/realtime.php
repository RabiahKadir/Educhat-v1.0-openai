<?php
// Fungsi untuk membaca data dari Python
function read_data() {
    $cmd = "python realtime.py";
    $descriptorspec = array(
        0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
        1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
        2 => array("pipe", "w")   // stderr is a pipe that the child will write to
    );
    $process = proc_open($cmd, $descriptorspec, $pipes);
    if (!is_resource($process)) {
        die("Failed to execute command: $cmd");
    }
    stream_set_blocking($pipes[1], false);
    while (!feof($pipes[1])) {
        $data = fgets($pipes[1]);
        if ($data !== false) {
            yield $data;
        }
        usleep(10000);
    }
    fclose($pipes[1]);
    proc_close($process);
}

// Membaca data secara realtime dengan AJAX
if (isset($_GET['action']) && $_GET['action'] == 'realtime') {
    header('Content-Type: text/event-stream');
    header('Cache-Control: no-cache');
    foreach (read_data() as $data) {
        echo "data: $data\n\n";
        ob_flush();
        flush();
    }
}
?>
