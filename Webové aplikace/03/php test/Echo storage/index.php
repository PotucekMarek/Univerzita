<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
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

    // Perform a query
    $result = $conn->query("SELECT * FROM your_table_name");

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