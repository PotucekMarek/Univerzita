<?php
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}
include __DIR__ . '/../dbconnection.php';
include __DIR__ . '/../models/LoginModel.php';

// Similar code to handle login operations
// Ensure $conn is used properly in models and views
include __DIR__ . '/../views/login.php';
?>