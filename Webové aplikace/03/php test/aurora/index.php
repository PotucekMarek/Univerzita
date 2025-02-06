<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test sql</title>
</head>
<body>
    <?php
    include 'config.php';

    // Create connection
    $conn = new mysqli($host, $user, $password, $database);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    echo "<h1>Connected successfully</h1>";
    // Perform a query
    $result = $conn->query("SELECT * FROM my_table");

    // Check for errors
    if (!$result) {
        die("Query failed: " . $conn->error);
    }

    // Fetch and display data
    echo "<table border='1'>";
    echo "<tr><th>ID</th><th>Name</th></tr>";
    while ($row = $result->fetch_assoc()) {
        echo "<tr><td>{$row['id']}</td><td>{$row['name']}</td></tr>";
    }
    echo "</table>";

    // Close connection
    $conn->close();
    ?>
</body>
</html>