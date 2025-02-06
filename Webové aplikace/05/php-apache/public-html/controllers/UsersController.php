<?php
include 'dbconnection.php';
include 'models/UserModel.php';

$userModel = new UserModel($conn);

// Handle user update
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['update_user'])) {
    $id = htmlspecialchars($_POST['id']);
    $name = htmlspecialchars($_POST['name']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $email = htmlspecialchars($_POST['email']);
    $phoneNumber = htmlspecialchars($_POST['phoneNumber']);
    $workRoom = htmlspecialchars($_POST['workRoom']);

    $userModel->updateUser($id, $name, $lastName, $email, $phoneNumber, $workRoom);

    header("Location: users");
    exit();
}

// Handle password change
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['change_password'])) {
    $id = htmlspecialchars($_POST['id']);
    $newPassword = htmlspecialchars($_POST['newPassword']);
    $confirmPassword = htmlspecialchars($_POST['confirmPassword']);

    if ($newPassword === $confirmPassword) {
        $hashedPassword = password_hash($newPassword, PASSWORD_BCRYPT);
        $userModel->changePassword($id, $hashedPassword);
        header("Location: users");
        exit();
    } else {
        $passwordError = "Passwords do not match!";
    }
}

// Handle user delete
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['delete'])) {
    $id = htmlspecialchars($_POST['delete']);
    $stmt = $conn->prepare("DELETE FROM user_table WHERE id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $stmt->close();

    header("Location: users");
    exit();
}

$users = $userModel->getAllUsers();

include 'views/users.php';
?>