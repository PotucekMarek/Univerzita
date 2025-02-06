<?php
include __DIR__ . '/../dbconnection.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['id'])) {
    $id = intval($_POST['id']);
    
    // Prepare and execute delete statements for both tables
    $stmt = $conn->prepare("DELETE FROM user_table WHERE id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $stmt->close();

    $stmt = $conn->prepare("DELETE FROM login_table WHERE id = ?"); // Assuming 'id' is the correct column name
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $stmt->close();

    echo "success";
    $conn->close();
} else {
    echo "error: invalid request";
}
?>