<?php
session_start();
include 'dbconnection.php';

// Simple router to handle requests
$request = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$method = $_SERVER['REQUEST_METHOD'];

switch ($request) {
    case '/' :
    case '/dashboard':
        require __DIR__ . '/controllers/DashboardController.php';
        break;

    case '/users' :
        require __DIR__ . '/controllers/UsersController.php';
        break;

    case '/items' :
        require __DIR__ . '/controllers/ItemsController.php';
        break;

    case '/registration' :
        require __DIR__ . '/controllers/RegistrationController.php';
        break;

    case '/login' :
        if ($method === 'POST') {
            // Handle the login form submission
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
                    header("Location: /dashboard"); // redirect to dashboard
                    exit();
                } else {
                    $msg = "Please check your inputs!";
                }
            } else {
                $msg = "Please check your inputs!";
            }
            echo "<p class='mt-3'>$msg</p>";
        } else {
            require __DIR__ . '/controllers/LoginController.php';
        }
        break;

    case '/data' :
        require __DIR__ . '/controllers/DataController.php';
        break;

    case '/others' :
        require __DIR__ . '/views/others.php';
        break;

    default:
        http_response_code(404);
        echo "404 Not Found";
        break;
}
?>