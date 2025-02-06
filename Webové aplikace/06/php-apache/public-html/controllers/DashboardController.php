<?php
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}
include __DIR__ . '/../dbconnection.php';
include __DIR__ . '/../models/UserModel.php';

$userModel = new UserModel($conn);
$recentUsers = $userModel->getRecentUsers(10);

include __DIR__ . '/../views/dashboard.php';
?>