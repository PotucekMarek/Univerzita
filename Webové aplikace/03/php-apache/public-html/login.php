<?php
session_start();

define("ID_NUMBER", "idnumber.txt"); // new file to store id

function getIdNumber() {
  if (!file_exists(ID_NUMBER)) {
    file_put_contents(ID_NUMBER, 1); // create file with id 1 if it doesn't exist
    return 1;
  } else {
    return (int)file_get_contents(ID_NUMBER); // get number from file
  }
}

function incrementIdNumber() {
  $id = getIdNumber() + 1;
  file_put_contents(ID_NUMBER, $id);
  return $id;
}
?>

<!doctype html>
<html>
  <head>
    <title>Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="./css/custom.css" rel="stylesheet">  <!-- compiled sass -->
    <link rel="stylesheet" href="./bootstrap-icons.css">
    <?php
      include 'header.php';
      include 'sidebar.php';
    ?>
  </head>
  <body>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
      <h1 class="pb-3 border-bottom">Login</h1>
      <section class="mt-5">
        <form method="POST" action="login.php">
          <div class="col-md-6 mb-3">
            <label for="inputName" class="form-label">Name</label>
            <input type="text" class="form-control" id="inputName" name="fname" required>
          </div>
          <div class="col-md-6 mb-3">
            <label for="inputLast" class="form-label">Last name</label>
            <input type="text" class="form-control" id="inputLast" name="lname" required>
          </div>
          <div class="col-12">
            <button type="submit" class="btn btn-primary">Sign in</button>
          </div>
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
          $fname = htmlspecialchars($_POST['fname']); // prevention from XSS
          $lname = htmlspecialchars($_POST['lname']);

          $_SESSION['username'] = $fname; // store name in session
          $_SESSION['fullname'] = $fname . ' ' . $lname;
          $idnumber = incrementIdNumber();

          $fs = fopen("mydata.csv", "a");
          fputcsv($fs, [$fname, $lname, $idnumber]);
          fclose($fs);

          header("Location: dashboard.php"); // redirection
          exit();    
        }
        ?>
      </section>
    </main>
    <script src="./bootstrap.js"></script>
  </body>
</html>