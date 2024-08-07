<?php
include "models/functions.php";

$name = "";
$email = "";
$contact ="";

# Setting variables for error messages
$error_msg = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST' and isset($_POST['submit']))
{
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $contact = htmlspecialchars($_POST['contact']);

    $tb_name = "clients";
    $tb_atrr = ['name', 'email', 'phone'];
    $tb_val = [$name, $email, $contact];

    # Check if all form field are entered
    if (empty($name) || empty($email) || empty($contact))
        $error_msg = "All the fields are required";
    else
    {
        $con = connect_to_database("localhost", "root", "");
        $con->select_db('myshop');
        $tb_obj = $con->query("SELECT * FROM clients");

        $user_exist = TRUE;
        while ($row = $tb_obj->fetch_assoc())
        {
            if (strcasecmp($row['name'], $name ) == 0 ||
                strcasecmp($row['email'], $email) == 0)
            {
                $user_exist = FALSE;
                $user_error_msg = "User already exists";
                break;
            }
        }
        if ($user_exist)
        {
            insert_data($tb_name, $tb_atrr, $tb_val, $con);
            $success_msg = "Client added";
            header("Location: 1-index.php");
        }
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
        <h2 style="text-align: center">Add new client to table</h2>

        <!- php code to display error ->
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
    /*
        I remove it since i want to redirect it to main page and not display the success message
        else if (!empty($success_msg))
        {
            echo "
                <div class='alert alert-success alert-dismissible fade in'>
                    <strong>Successful! </strong>$success_msg
                    <a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>
                </div>
                ";
        }
    */
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
                <input class="form-control" name="contact" placeholder="Enter phone number" value="<?php echo $contact; ?>">
            </div>
            <div class="grp-btn">
                <button type="submit" name="submit" class="btn btn-primary">Save</button>
                <a class="btn btn-danger" href="1-index.php">Back</a>
            </div>
        </form>
    </div>
</body>
</html>