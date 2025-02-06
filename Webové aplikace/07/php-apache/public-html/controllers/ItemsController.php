<?php
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}
include __DIR__ . '/../dbconnection.php';
include __DIR__ . '/../models/UserModel.php';
include __DIR__ . '/../views/items.php';
?>