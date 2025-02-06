<?php

// prihlasovaci udaje
$host = 'db'; 
$user = 'root';
$pass = 'toor';

echo "<p>Webserver works!</p>";

// overeni pripojeni k databazi
$connection = new mysqli($host, $user, $pass);

if ($connection->connect_error) {
    die("<p>Connection failed: " . $conn->connect_error ."</p>");
} else {
    echo "<p>Connected to MySQL server successfully!</p>";
}

?>
