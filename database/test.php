<?php
function generateAlphanumericId($length = 32)
{
        return substr(str_shuffle("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%?&"), 0, $length);
}

$id = generateAlphanumericId();
echo $id;
?>
