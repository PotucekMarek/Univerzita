<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['delete'])) {
  $idToDelete = $_POST['delete']; // load id of user

  $data = array(); // read data from .csv
  if (($handle = fopen("mydata.csv", "r")) !== FALSE) {
    while (($row = fgetcsv($handle, 1000, ",")) !== FALSE) {
      if ($row[0] != $idToDelete) { 
        $data[] = $row;  // delete row with the ID 
      }
    }
    fclose($handle);
  }

  $handle = fopen("mydata.csv", "w"); // write back to the CSV file
  foreach ($data as $row) {
    fputcsv($handle, $row);
  }
  fclose($handle);

  header("Location: users.php"); // redirection
  exit();
}
?>

<!doctype html>
<html lang="en">
<head>
  <title>Users</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="./css/custom.css" rel="stylesheet">  <!-- compiled Sass -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.5.0/font/bootstrap-icons.min.css">
</head>
<body>
  <?php
    include 'header.php';
    include 'sidebar.php';
  ?>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
    <h1 class="pb-3 border-bottom">Users</h1>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        <?php  //show user data from .csv
        if (($handle = fopen("mydata.csv", "r")) !== FALSE) {
          while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            echo "<tr>";
            echo "<th scope=\"row\">" . htmlspecialchars($data[0]) . "</th>";
            echo "<td>" . htmlspecialchars($data[1]) . "</td>";
            echo "<td>" . htmlspecialchars($data[2]) . "</td>";
            echo "<td>";
            echo "<form method='POST' action='users.php' style='display:inline;'>";
            echo "<button type='submit' name='delete' value='" . htmlspecialchars($data[0]) . "' class='btn btn-danger btn-sm'>";
            echo "<i class='bi bi-trash'></i>";
            echo "</button>";
            echo "</form>";
            echo "</td>";
            echo "</tr>";
          }
          fclose($handle);
        }
        ?>
      </tbody>
    </table>
  </main>
  <script src="./bootstrap.js"></script>
</body>
</html>