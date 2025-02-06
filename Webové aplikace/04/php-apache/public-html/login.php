<?php
session_start();
include 'dbconnection.php';
?>

<!doctype html>
<html>
    <head>
        <title>Login</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="./css/custom.css" rel="stylesheet">  <!-- compiled sass -->
        <link rel="stylesheet" href="./bootstrap-icons.css">
        <?php include 'header.php'; include 'sidebar.php'; ?>
    </head>

    <body>
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
            <h1 class="pb-3 border-bottom">Login</h1>
            <section class="mt-5">
                <form method="POST" action="login.php">

                    <div class="col-md-6 mb-3">
                        <label for="inputName" class="form-label">Username</label>
                        <input type="text" class="form-control" id="inputName" name="username" required>
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="inputPassword" class="form-label">Password</label>
                        <input type="password" class="form-control" id="inputPassword" name="password" required>
                    </div>

                    <div class="col-12">
                        <button type="submit" class="btn btn-primary" name="submit">Sign in</button>
                    </div>


                    <p>Don't have an account? <a href="registration.php">Register here</a>.</p>
                </form>

                <?php
                if (isset($_POST['submit'])) {
                    $username = $conn->real_escape_string($_POST['username']);
                    $password = $conn->real_escape_string($_POST['password']);

                    $sql = $conn->query("SELECT id, password, role FROM login_table WHERE username='$username'");
                    if ($sql->num_rows > 0) {
                        $data = $sql->fetch_array();
                        if (password_verify($password, $data['password'])) {
                            // store in session
                            $_SESSION['username'] = $username; 
                            $_SESSION['role'] = $data['role']; 
                            $msg = "You have been logged in!";
                            header("Location: dashboard.php"); // redirect to dashboard
                            exit();
                        } else {
                            $msg = "Please check your inputs!";
                        }
                    } else {
                        $msg = "Please check your inputs!";
                    }
                    echo "<p class='mt-3'>$msg</p>";
                }
                ?>
            </section>
        </main>
    <script src="./bootstrap.js"></script>
    </body>
</html>

