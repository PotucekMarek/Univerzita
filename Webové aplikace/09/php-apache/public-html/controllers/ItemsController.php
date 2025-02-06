<?php
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}
include __DIR__ . '/../dbconnection.php';
include __DIR__ . '/../models/UserModel.php';

// Similar code to handle item operations
// Ensure $conn is used properly in models and views
include __DIR__ . '/../views/items.php';
?>