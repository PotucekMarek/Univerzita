<?php

class RegistrationModel {
    private $conn;

    public function __construct($db) {
        $this->conn = $db;
    }

    public function registerUser($username, $password, $role) {
        $hash = password_hash($password, PASSWORD_BCRYPT);
        $stmt = $this->conn->prepare("INSERT INTO login_table (username, password, role) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $username, $hash, $role);
        $stmt->execute();
        $stmt->close();
    }
}
?>