<?php
class LoginModel {
    private $conn;

    public function __construct($conn) {
        $this->conn = $conn;
    }

    public function getUserByUsername($username) {
        $sql = "SELECT * FROM login_table WHERE username=?";
        if ($stmt = $this->conn->prepare($sql)) {
            $stmt->bind_param("s", $username);
            $stmt->execute();
            $result = $stmt->get_result();
            $user = $result->fetch_assoc();
            $stmt->close();
            return $user;
        }
        return null;
    }

    public function changePassword($id, $hashedPassword) {
        $sql = "UPDATE login_table SET password=? WHERE user_id=?";
        if ($stmt = $this->conn->prepare($sql)) {
            $stmt->bind_param("si", $hashedPassword, $id);
            return $stmt->execute();
        }
        return false;
    }

    public function registerUser($username, $hashedPassword, $role) {
        $sql = "INSERT INTO login_table (username, password, role) VALUES (?, ?, ?)";
        if ($stmt = $this->conn->prepare($sql)) {
            $stmt->bind_param("sss", $username, $hashedPassword, $role);
            return $stmt->execute();
        }
        return false;
    }

    public function deleteUserLogin($id) {
        $sql = "DELETE FROM login_table WHERE user_id = ?";
        if ($stmt = $this->conn->prepare($sql)) {
            $stmt->bind_param("i", $id);
            return $stmt->execute();
        }
        return false;
    }
}
?>