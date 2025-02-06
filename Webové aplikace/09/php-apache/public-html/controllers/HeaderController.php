<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

include_once 'dbconnection.php';
include_once 'models/UserModel.php';

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
