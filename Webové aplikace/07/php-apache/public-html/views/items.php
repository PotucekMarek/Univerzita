<?php
include 'dbconnection.php';
$successMessage = "";

// only admin have access to this site
if (!isset($_SESSION['role']) || $_SESSION['role'] != 'admin') {
    header("Location: dashboard");
    exit();
}


// insert into database
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['add_item'])) {
    $name = htmlspecialchars($_POST['name']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $email = htmlspecialchars($_POST['email']);
    $phoneNumber = htmlspecialchars($_POST['phoneNumber']);
    $workRoom = htmlspecialchars($_POST['workRoom']);

    $sql = "INSERT INTO user_table (name, lastName, email, phoneNumber, workRoom) VALUES (?, ?, ?, ?, ?)";
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("sssss", $name, $lastName, $email, $phoneNumber, $workRoom);
        $stmt->execute();
        $stmt->close();
    }

    $successMessage = "Successfully added a new user!";
}
?>

<!doctype html>
<html lang="en">
  <head>
    <title>Items</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../css/custom.css" rel="stylesheet">  <!-- compiled Sass -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.5.0/font/bootstrap-icons.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="../bootstrap-icons.css">
  </head>
  <body>
    <?php include 'header.php'; include 'sidebar.php'; ?>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
      <h1 class="pb-3 border-bottom">Add user</h1>
      
      <form method="POST" action="items">
        <div class="mb-3">
          <label for="name" class="form-label">First Name</label>
          <input type="text" class="form-control" id="name" name="name" required>
        </div>
        <div class="mb-3">
          <label for="lastName" class="form-label">Last Name</label>
          <input type="text" class="form-control" id="lastName" name="lastName" required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" name="email" required>
        </div>
        <div class="mb-3">
          <label for="phoneNumber" class="form-label">Phone Number</label>
          <input type="text" class="form-control" id="phoneNumber" name="phoneNumber" required>
        </div>
        <div class="mb-3">
          <label for="workRoom" class="form-label">Work Room</label>
          <input type="text" class="form-control" id="workRoom" name="workRoom" required>
        </div>
        <button type="submit" class="btn btn-primary" name="add_item">Add User</button>
      </form>

      <?php if ($successMessage): ?>
        <div class="alert alert-success alert-dismissible fade show" role="alert">
          <?php echo $successMessage; ?>
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
      <?php endif; ?>
    </main>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <script src="./bootstrap.js"></script>
    
    <script>
      $(document).ready(function() {
        setTimeout(function() {
          $('.alert').alert('close');
        }, 3000);
      });
    </script>
  </body>
</html>

<?php
$conn->close();
?>