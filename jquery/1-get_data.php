<?php
$js_data = json_decode(file_get_contents('php://input'));
if ($js_data)
    echo "Data received";
else
    echo "Oops, No data received";
?>