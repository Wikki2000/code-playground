<?php
include "models/functions.php";

if ($_SERVER['REQUEST_METHOD'] === 'GET')
{
    $id = $_GET['id'];
    $con = connect_to_database('localhost', 'root', '');
    $con->select_db("myshop");
    $sql = "DELETE FROM clients WHERE `id` = ?";
    $stmt = $con->prepare($sql);

    $stmt->bind_param("i", $id);
    $stmt->execute();
    header("Location: 1-index.php");
}
?>