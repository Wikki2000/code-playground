<?php
include 'models\functions.php';

$db_name = 'myshop';
$tb_name = 'clients';
$tb_attr =  "id INT AUTO_INCREMENT PRIMARY KEY UNIQUE, " . 
            "name VARCHAR(50) NOT NULL UNIQUE, " .
            "email VARCHAR(50) NOT NULL UNIQUE, " .
            "phone VARCHAR(50), " .
            "create_at DATETIME DEFAULT CURRENT_TIMESTAMP";




$con = connect_to_database('localhost', 'root', '');
create_database($db_name, $con);
$con->select_db($db_name);
create_table($db_name, $tb_name, $tb_attr, $con);
$tb_obj = $con->query('SELECT * FROM clients');

if (!$tb_obj)
{
    die("Error" .$tb_obj->error);
    exit(1);
}
$con->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <title>My shop</title>
</head>
<style>
    #btn{
        margin-left: 90%;
    }
</style>
<body>
    <div class="container">
        <h2 style="text-align: center">List of Clients <a class="btn btn-primary" id="btn" href="1-create_new.php">Add new client</a></h2>

        <table class="table">
            <thead>
                <tr>
                    <th>S/N</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>create_at</th>
                    <th>Action</th>
                </tr>
            </thead>

            <tbody>
                <?php
                while($row = $tb_obj->fetch_assoc())
                {
                    echo "
                    <tr>
                        <td>$row[id]</td>
                        <td>$row[name]</td>
                        <td>$row[email]</td>
                        <td>$row[phone]</td>
                        <td>$row[create_at]</td>
                        <td>
                            <!- Send the id number of row to the href link by GET method ->
                            <a class='btn btn-primary' href='1-edit_client.php?id=$row[id]'>Edit</a>
                            <a class='btn btn-danger' href='1-delete_client.php?id=$row[id]'>Delete</a>
                        </td>
                    </tr>
                    ";
                }
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>