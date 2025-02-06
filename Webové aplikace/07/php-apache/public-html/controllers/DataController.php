<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

include_once 'dbconnection.php';
include_once 'models/UserModel.php';

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$userModel = new UserModel($conn);

// check if user is logged in
if (!isset($_SESSION['username'])) {
    header("Location: login");
    exit();
}

// check if the user is admin
$isAdmin = isset($_SESSION['role']) && $_SESSION['role'] == 'admin';

// flags
$showEditModal = false;
$showPasswordModal = false;

// data update
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['update_user'])) {
    $id = htmlspecialchars($_POST['id']);
    $name = htmlspecialchars($_POST['name']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $email = htmlspecialchars($_POST['email']);
    $phoneNumber = htmlspecialchars($_POST['phoneNumber']);
    $workRoom = htmlspecialchars($_POST['workRoom']);

    if ($id) { // if id is present, updates user data
        $userModel->updateUser($id, $name, $lastName, $email, $phoneNumber, $workRoom);
    } else { // if id is not present, insert user data
        $userModel->createUser($name, $lastName, $email, $phoneNumber, $workRoom);
    }

    $_SESSION['username'] = $name; // change username if user changed it
    header("Location: data");
    exit();
}

// change password
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['change_password'])) {
    $id = htmlspecialchars($_POST['id']);
    $newPassword = htmlspecialchars($_POST['newPassword']);
    $confirmPassword = htmlspecialchars($_POST['confirmPassword']);

    if ($newPassword === $confirmPassword) {
        $hashedPassword = password_hash($newPassword, PASSWORD_BCRYPT);
        $userModel->changePassword($id, $hashedPassword);

        header("Location: data");
        exit();
    } else {
        $passwordError = "Passwords do not match!";
        $showPasswordModal = true;
    }
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['edit_user'])) {
    $showEditModal = true;
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['show_change_password'])) {
    $showPasswordModal = true;
}

// draw out data from logged in user from database
$username = $_SESSION['username'];
$user = $userModel->getUserByName($username);

include 'views/data.php';
?>