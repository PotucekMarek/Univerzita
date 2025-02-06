<?php
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}

include __DIR__ . '/../dbconnection.php';

$response = [];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $logId = $_POST['id'] ?? null;

    if ($logId) {
        $stmt = $conn->prepare("DELETE FROM login_table WHERE id = ?");
        $stmt->bind_param("i", $logId);

        if ($stmt->execute()) {
            $response = [
                'status' => 'success',
                'message' => 'Log deleted successfully'
            ];
        } else {
            $response = [
                'status' => 'error',
                'message' => 'Failed to delete log'
            ];
        }

        $stmt->close();
    } else {
        $response = [
            'status' => 'error',
            'message' => 'Invalid log ID'
        ];
    }
} else {
    $response = [
        'status' => 'error',
        'message' => 'Invalid request method'
    ];
}

header('Content-Type: application/json');
echo json_encode($response);

$conn->close();
?>