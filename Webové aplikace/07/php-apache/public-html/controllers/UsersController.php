<?php
include __DIR__ . '/../dbconnection.php';
include __DIR__ . '/../models/UserModel.php';

$userModel = new UserModel($conn);

// only admin has access to this site
if (!isset($_SESSION['role']) || $_SESSION['role'] != 'admin') {
    header("Location: /dashboard");
    exit();
}

// Handle AJAX request for user deletion
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['delete_user']) && isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
    $id = htmlspecialchars($_POST['id']);
    $userModel->deleteUser($id); // Assuming you have a deleteUser method in your UserModel
    echo json_encode(['status' => 'success', 'message' => 'User deleted successfully.']);
    exit();
}

// user update
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['update_user'])) {
    $id = htmlspecialchars($_POST['id']);
    $name = htmlspecialchars($_POST['name']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $email = htmlspecialchars($_POST['email']);
    $phoneNumber = htmlspecialchars($_POST['phoneNumber']);
    $workRoom = htmlspecialchars($_POST['workRoom']);

    $userModel->updateUser($id, $name, $lastName, $email, $phoneNumber, $workRoom);

    header("Location: /users");
    exit();
}

// password change
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['change_password'])) {
    $id = htmlspecialchars($_POST['id']);
    $newPassword = htmlspecialchars($_POST['newPassword']);
    $confirmPassword = htmlspecialchars($_POST['confirmPassword']);

    if ($newPassword === $confirmPassword) {
        $hashedPassword = password_hash($newPassword, PASSWORD_BCRYPT);
        $userModel->changePassword($id, $hashedPassword);
        header("Location: /users");
        exit();
    } else {
        $passwordError = "Passwords do not match!";
    }
}

// user delete (non-AJAX fallback)
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['delete_user'])) {
    $id = htmlspecialchars($_POST['id']);
    $userModel->deleteUser($id); // Assuming you have a deleteUser method in your UserModel
    $_SESSION['successMessage'] = "User deleted successfully.";
    header("Location: /users");
    exit();
}

// exporting users to JSON
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['export_json'])) {
    $users = $userModel->getAllUsers();
    $json_data = json_encode($users, JSON_PRETTY_PRINT);
    file_put_contents(__DIR__ . '/../data_file/users.json', $json_data);
    $_SESSION['successMessage'] = "User data saved to JSON file successfully.";
    header("Location: /users");
    exit();
}

$users = $userModel->getAllUsers();

// clear the success message from the session
$successMessage = isset($_SESSION['successMessage']) ? $_SESSION['successMessage'] : null;
unset($_SESSION['successMessage']);

include __DIR__ . '/../views/users.php';
?>