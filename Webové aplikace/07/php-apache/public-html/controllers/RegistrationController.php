<?php
include __DIR__ . '/../dbconnection.php';
include __DIR__ . '/../models/RegistrationModel.php';

$registrationModel = new RegistrationModel($conn);

if (isset($_POST['submit'])) {
    $username = $conn->real_escape_string($_POST['username']);
    $password = $conn->real_escape_string($_POST['password']);
    $cPassword = $conn->real_escape_string($_POST['cPassword']);
    $role = $conn->real_escape_string($_POST['role']);

    if ($password != $cPassword) {
        $msg = "Please Check Your Passwords!";
    } else {
        $registrationModel->registerUser($username, $password, $role);
        $msg = "You have been registered!";
        header("Location: /dashboard"); // redirect to dashboard
        exit();
    }
}

include __DIR__ . '/../views/registration.php';
?>