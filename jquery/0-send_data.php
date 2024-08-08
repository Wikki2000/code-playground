<?php
// Create an associative array
$dict = ['name' => 'server', 'type' => 'php'];

// Encode the array as JSON
$json_str = json_encode($dict);

// Output the JSON string
echo $json_str;
?>
