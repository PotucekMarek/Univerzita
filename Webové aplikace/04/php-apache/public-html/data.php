<?php
session_start();
// https://www.w3schools.com/bootstrap/bootstrap_modal.asp
include 'dbconnection.php';

// check if user is logged in
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}

// check if the user is admin
$isAdmin = isset($_SESSION['role']) && $_SESSION['role'] == 'admin';

// modal flags
$showEditModal = false;
$showPasswordModal = false;

// data update
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['update_user'])) {
    $id = htmlspecialchars($_POST['id']);
    $name = htmlspecialchars($_POST['name']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $email = htmlspecialchars($_POST['email']);
    $phoneNumber = htmlspecialchars($_POST['phoneNumber']);
    $workRoom = htmlspecialchars($_POST['workRoom']);

    if ($id) { // if id is present, updates user data
        $sql = "UPDATE user_table SET name=?, lastName=?, email=?, phoneNumber=?, workRoom=? WHERE id=?";
        if ($stmt = $conn->prepare($sql)) {
            $stmt->bind_param("sssssi", $name, $lastName, $email, $phoneNumber, $workRoom, $id);
            $stmt->execute();
            $stmt->close();
        }
    } 
    
    else { // if id is not present, insert user data
        $sql = "INSERT INTO user_table (name, lastName, email, phoneNumber, workRoom) VALUES (?, ?, ?, ?, ?)";
        if ($stmt = $conn->prepare($sql)) {
            $stmt->bind_param("sssss", $name, $lastName, $email, $phoneNumber, $workRoom);
            $stmt->execute();
            $stmt->close();
        }
    }

    $_SESSION['username'] = $name; // change username if user changed it
    header("Location: data.php");
    exit();
}

// change password
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['change_password'])) {
    $id = htmlspecialchars($_POST['id']);
    $newPassword = htmlspecialchars($_POST['newPassword']);
    $confirmPassword = htmlspecialchars($_POST['confirmPassword']);

    if ($newPassword === $confirmPassword) {
        $hashedPassword = password_hash($newPassword, PASSWORD_BCRYPT);
        $sql = "UPDATE login_table SET password=? WHERE user_id=?";
        
        if ($stmt = $conn->prepare($sql)) {
            $stmt->bind_param("si", $hashedPassword, $id);
            $stmt->execute();
            $stmt->close();
        }

        header("Location: data.php");
        exit();
    } 
    
    else {
        $passwordError = "Passwords do not match!";
        $showPasswordModal = true;
    }
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['edit_user'])) {
    $showEditModal = true;
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['show_change_password'])) {
    $showPasswordModal = true;
}

// draw out data from logged in user from database
$username = $_SESSION['username'];
$sql = "SELECT * FROM user_table WHERE name=?";
if ($stmt = $conn->prepare($sql)) {
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    $user = $result->fetch_assoc();
    $stmt->close();
}
?>

<!doctype html>
<html lang="en">
  <head>
    <title>User Data</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="./css/custom.css" rel="stylesheet">  <!-- compiled sass -->
    <link rel="stylesheet" href="./bootstrap-icons.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  </head>
  <body>
    <?php include 'header.php'; include 'sidebar.php'; ?>
    <div class="container-fluid">
      <div class="row">
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
          <h1 class="pb-3 border-bottom">User Data</h1>
          <section class="mt-5">
            <?php if ($user): ?>
              <p><strong>First Name:</strong> <?php echo htmlspecialchars($user['name']); ?></p>
              <p><strong>Last Name:</strong> <?php echo htmlspecialchars($user['lastName']); ?></p>
              <p><strong>Email:</strong> <?php echo htmlspecialchars($user['email']); ?></p>
              <p><strong>Phone Number:</strong> <?php echo htmlspecialchars($user['phoneNumber']); ?></p>
              <p><strong>Work Room:</strong> <?php echo htmlspecialchars($user['workRoom']); ?></p>
              <p><strong>Role:</strong> <?php echo $isAdmin ? 'Admin' : 'User'; ?></p>
              <form method="post" action="data.php">
                <input type="hidden" name="edit_user" value="1">
                <button type="submit" class="btn btn-success btn-sm"><i class="bi bi-pen"></i> Edit</button>
              </form>
              <form method="post" action="data.php">
                <input type="hidden" name="show_change_password" value="1">
                <button type="submit" class="btn btn-warning btn-sm"><i class="bi bi-key"></i> Change Password</button>
              </form>
            <?php else: ?>
              <p>No user data found. Please add your details:</p>
              <form method="post" action="data.php">
                <input type="hidden" name="edit_user" value="1">
                <button type="submit" class="btn btn-primary btn-sm"><i class="bi bi-plus"></i> Add Data</button>
              </form>
            <?php endif; ?>
          </section>
        </main>
      </div>
    </div>

    <!-- edit User -->
    <div class="modal fade<?php if ($showEditModal) echo ' show d-block'; ?>" id="editUserModal" tabindex="-1" role="dialog" aria-labelledby="editUserModalLabel" aria-hidden="true" style="<?php if ($showEditModal) echo 'display: block;'; ?>">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editUserModalLabel">Edit User</h5>
            <form method="post" action="data.php">
              <button type="submit" class="close" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </form>
          </div>
          <form method="POST" action="data.php">
            <div class="modal-body">
              <input type="hidden" id="editUserId" name="id" value="<?php echo $user ? htmlspecialchars($user['id']) : ''; ?>">
              <div class="form-group">
                <label for="editUserName" class="form-label">First Name</label>
                <input type="text" class="form-control" id="editUserName" name="name" value="<?php echo $user ? htmlspecialchars($user['name']) : ''; ?>" required>
              </div>
              <div class="form-group">
                <label for="editUserLastName" class="form-label">Last Name</label>
                <input type="text" class="form-control" id="editUserLastName" name="lastName" value="<?php echo $user ? htmlspecialchars($user['lastName']) : ''; ?>" required>
              </div>
              <div class="form-group">
                <label for="editUserEmail" class="form-label">Email</label>
                <input type="email" class="form-control" id="editUserEmail" name="email" value="<?php echo $user ? htmlspecialchars($user['email']) : ''; ?>" required>
              </div>
              <div class="form-group">
                <label for="editUserPhoneNumber" class="form-label">Phone Number</label>
                <input type="text" class="form-control" id="editUserPhoneNumber" name="phoneNumber" value="<?php echo $user ? htmlspecialchars($user['phoneNumber']) : ''; ?>" required>
              </div>
              <div class="form-group">
                <label for="editUserWorkRoom" class="form-label">Work Room</label>
                <input type="text" class="form-control" id="editUserWorkRoom" name="workRoom" value="<?php echo $user ? htmlspecialchars($user['workRoom']) : ''; ?>" required>
              </div>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-secondary" name="edit_user">Close</button>
              <button type="submit" class="btn btn-primary" name="update_user">Save changes</button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- change Password -->
    <div class="modal fade<?php if ($showPasswordModal) echo ' show d-block'; ?>" id="changePasswordModal" tabindex="-1" role="dialog" aria-labelledby="changePasswordModalLabel" aria-hidden="true" style="<?php if ($showPasswordModal) echo 'display: block;'; ?>">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="changePasswordModalLabel">Change Password</h5>
            <form method="post" action="data.php">
              <button type="submit" class="close" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </form>
          </div>
          <form method="POST" action="data.php">
            <div class="modal-body">
              <input type="hidden" id="changePasswordUserId" name="id" value="<?php echo $user ? htmlspecialchars($user['id']) : ''; ?>">
              <div class="form-group">
                <label for="newPassword" class="form-label">New Password</label>
                <input type="password" class="form-control" id="newPassword" name="newPassword" required>
              </div>
              <div class="form-group">
                <label for="confirmPassword" class="form-label">Confirm Password</label>
                <input type="password" class="form-control" id="confirmPassword" name="confirmPassword" required>
              </div>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-secondary" name="change_password">Close</button>
              <button type="submit" class="btn btn-primary" name="change_password">Change Password</button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  </body>
</html>

<?php
$conn->close();
?>