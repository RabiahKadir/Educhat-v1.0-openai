<?php
$command = escapeshellcmd('python userinput.py');
$output = shell_exec($command);
$lines = explode("\n", $output);
foreach ($lines as $line) {
    echo $line . "<br>";
}
?>