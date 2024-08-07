<?php
include "models/functions.php";

$id = "";
$name = "";
$email = "";
$phone ="";

# Setting variables for error messages
$success_msg = "";
$user_error_msg = "";

$con = connect_to_database('localhost', 'root', '');
$con->select_db("myshop");

if ($_SERVER['REQUEST_METHOD'] === "GET")
{
    # GET method: Show the data of the client
    $id = $_GET['id']; // The id is sent together with the link

    $sql = "SELECT * FROM `clients` WHERE `id` = $id";
    $tb_obj = $con->query($sql);
    $clients = $tb_obj->fetch_assoc();

    $name = $clients["name"];
    $email = $clients["email"];
    $phone = $clients["phone"];
}
else
{
    # POST method: Update the data of the client
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $phone = htmlspecialchars($_POST['phone']);
    $id = htmlspecialchars($_POST['id']);

    # Check if all form field are entered
    if (empty($name) || empty($email) || empty($phone))
        $error_msg = "All the fields are required";
    else
    {
        # Use bind method to prevent sql injection
        $sql = "UPDATE `clients` SET `name` = ?, `email` = ?, `phone` = ? WHERE `id` = ?";
        $stmt = $con->prepare($sql);
        $stmt->bind_param("ssss", $name, $email, $phone, $id);
        $stmt->execute();

        $stmt->close();
        $con->close();
        header("Location: 1-index.php");
    }
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="styles/1-style.css">
    <title>My shop</title>
</head>
<body>
    <div class="container">
        <h2 style="text-align: center">Edit client</h2>

        <?php
        if (!empty($error_msg))
        {
            echo "
                <div class='alert alert-danger alert-dismissible fade in'>
                    <strong>Error! </strong>$error_msg
                    <a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>
                </div>
                ";
        }
        else if (!empty($success_msg))
        {
            echo "
                <div class='alert alert-success alert-dismissible fade in'>
                    <strong>Successful! </strong>$success_msg
                    <a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>
                </div>
                ";
        }
        else if (!empty($user_error_msg))
        {
            echo "
                <div class='alert alert-success alert-dismissible fade in'>
                    <strong>Error! </strong>$user_error_msg
                    <a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>
                </div>
                ";
        }
        ?>
        <form method="post">
            <input type="hidden" name="id" value="<?php echo $id; ?>">
            <div class="form-group">
                <label>Name</label>
                <input class="form-control" name="name" placeholder="Enter full name" value="<?php echo $name; ?>">
            </div>

            <div class="form-group">
                <label>Email</label>
                <input class="form-control" name="email" placeholder="Enter valid email address" value="<?php echo $email; ?>">
            </div>

            <div class="form-group">
                <label>Contact</label>
                <input class="form-control" name="phone" placeholder="Enter phone number" value="<?php echo $phone; ?>">
            </div>
            <div class="grp-btn">
                <button type="submit" name="submit" class="btn btn-primary">Save</button>
                <a class="btn btn-danger" href="1-index.php">Back</a>
            </div>
        </form>
    </div>
</body>
</html>