<?php
class UserModel {
    private $conn;

    public function __construct($db) {
        $this->conn = $db;
    }

    public function getUserByName($username) {
        $stmt = $this->conn->prepare("SELECT * FROM user_table WHERE name = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $result = $stmt->get_result();
        $user = $result->fetch_assoc();
        $stmt->close();
        return $user;
    }

    public function getUserById($id) {
        $stmt = $this->conn->prepare("SELECT * FROM user_table WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        $user = $result->fetch_assoc();
        $stmt->close();
        return $user;
    }

    public function getAllUsers() {
        $stmt = $this->conn->prepare("SELECT id, name, lastName, email, phoneNumber, workRoom FROM user_table");
        $stmt->execute();
        $result = $stmt->get_result();
        $users = $result->fetch_all(MYSQLI_ASSOC);
        $stmt->close();
        return $users;
    }

    public function updateUser($id, $name, $lastName, $email, $phoneNumber, $workRoom) {
        $stmt = $this->conn->prepare("UPDATE user_table SET name = ?, lastName = ?, email = ?, phoneNumber = ?, workRoom = ? WHERE id = ?");
        $stmt->bind_param("sssssi", $name, $lastName, $email, $phoneNumber, $workRoom, $id);
        $stmt->execute();
        $stmt->close();
    }

    public function createUser($name, $lastName, $email, $phoneNumber, $workRoom) {
        $stmt = $this->conn->prepare("INSERT INTO user_table (name, lastName, email, phoneNumber, workRoom) VALUES (?, ?, ?, ?, ?)");
        $stmt->bind_param("sssss", $name, $lastName, $email, $phoneNumber, $workRoom);
        $stmt->execute();
        $stmt->close();
    }

    public function changePassword($id, $hashedPassword) {
        $stmt = $this->conn->prepare("UPDATE login_table SET password = ? WHERE user_id = ?");
        $stmt->bind_param("si", $hashedPassword, $id);
        $stmt->execute();
        $stmt->close();
    }

    public function deleteUser($id) {
        $stmt = $this->conn->prepare("DELETE FROM user_table WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $stmt->close();
    }

    public function getRecentUsers($limit) {
        $stmt = $this->conn->prepare("SELECT * FROM user_table ORDER BY id DESC LIMIT ?");
        $stmt->bind_param("i", $limit);
        $stmt->execute();
        $result = $stmt->get_result();
        $users = [];
        while ($user = $result->fetch_assoc()) {
            $users[] = $user;
        }
        $stmt->close();
        return $users;
    }
}
?>