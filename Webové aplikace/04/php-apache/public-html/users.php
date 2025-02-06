<?php
session_start();
include 'dbconnection.php';

if (!isset($_SESSION['role']) || $_SESSION['role'] != 'admin') { // only admin may access this page
    header("Location: dashboard.php");
    exit();
}

// updating user data
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['update_user'])) {
    $id = htmlspecialchars($_POST['id']);
    $name = htmlspecialchars($_POST['name']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $email = htmlspecialchars($_POST['email']);
    $phoneNumber = htmlspecialchars($_POST['phoneNumber']);
    $workRoom = htmlspecialchars($_POST['workRoom']);

    $sql = "UPDATE user_table SET name=?, lastName=?, email=?, phoneNumber=?, workRoom=? WHERE id=?";
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("sssssi", $name, $lastName, $email, $phoneNumber, $workRoom, $id);
        $stmt->execute();
        $stmt->close();
    }
    header("Location: users.php");
    exit();
}

// changing password
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

        header("Location: users.php");
        exit();
    } else {
        $passwordError = "Passwords do not match!";
    }
}

// delete a user
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['delete'])) {
    $idToDelete = $_POST['delete'];

    $sql = "DELETE FROM user_table WHERE id = ?";
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("i", $idToDelete);
        $stmt->execute();
        $stmt->close();
    }
    // also delete user from login_table
    $sql = "DELETE FROM login_table WHERE user_id = ?";
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("i", $idToDelete);
        $stmt->execute();
        $stmt->close();
    }
    header("Location: users.php");
    exit();
}
?>

<!doctype html>
<html lang="en">
  <head>
    <title>Users and Items</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="./css/custom.css" rel="stylesheet">  <!-- compiled Sass -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.5.0/font/bootstrap-icons.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  </head>

  <body>
    <?php include 'header.php'; include 'sidebar.php'; ?>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
      <h1 class="pb-3 border-bottom">Users</h1>

      <table class="table mt-5">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
            <th scope="col">Work Room</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        
        <tbody>
          <?php
          // draw our user data from the database
          $sql = "SELECT id, name, lastName, email, phoneNumber, workRoom FROM user_table";
          if ($result = $conn->query($sql)) {
            while ($row = $result->fetch_assoc()) {
              echo "<tr>";
              echo "<th scope=\"row\">" . htmlspecialchars($row['id']) . "</th>";
              echo "<td>" . htmlspecialchars($row['name']) . "</td>";
              echo "<td>" . htmlspecialchars($row['lastName']) . "</td>";
              echo "<td>" . htmlspecialchars($row['email']) . "</td>";
              echo "<td>" . htmlspecialchars($row['phoneNumber']) . "</td>";
              echo "<td>" . htmlspecialchars($row['workRoom']) . "</td>";
              echo "<td>";
              echo "<button class='btn btn-success btn-sm edit-btn' data-id='" . htmlspecialchars($row['id']) . "' data-name='" . htmlspecialchars($row['name']) . "' data-lastname='" . htmlspecialchars($row['lastName']) . "' data-email='" . htmlspecialchars($row['email']) . "' data-phonenumber='" . htmlspecialchars($row['phoneNumber']) . "' data-workroom='" . htmlspecialchars($row['workRoom']) . "'><i class='bi bi-pen'></i></button> ";
              echo "<button class='btn btn-warning btn-sm password-btn' data-id='" . htmlspecialchars($row['id']) . "'><i class='bi bi-key'></i></button> ";
              echo "<form method='POST' action='users.php' style='display:inline;'>";
              echo "<button type='submit' name='delete' value='" . htmlspecialchars($row['id']) . "' class='btn btn-danger btn-sm'>";
              echo "<i class='bi bi-trash'></i>";
              echo "</button>";
              echo "</form>";
              echo "</td>";
              echo "</tr>";
            }
            $result->free();
          }
          ?>
        </tbody>
      </table>

      <!-- Edit User -->
      <div class="modal fade" id="editUserModal" tabindex="-1" role="dialog" aria-labelledby="editUserModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="editUserModalLabel">Edit User</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <form method="POST" action="users.php">
              <div class="modal-body">
                <input type="hidden" id="editUserId" name="id">
                <div class="form-group">
                  <label for="editUserName" class="form-label">First Name</label>
                  <input type="text" class="form-control" id="editUserName" name="name" required>
                </div>
                <div class="form-group">
                  <label for="editUserLastName" class="form-label">Last Name</label>
                  <input type="text" class="form-control" id="editUserLastName" name="lastName" required>
                </div>
                <div class="form-group">
                  <label for="editUserEmail" class="form-label">Email</label>
                  <input type="email" class="form-control" id="editUserEmail" name="email" required>
                </div>
                <div class="form-group">
                  <label for="editUserPhoneNumber" class="form-label">Phone Number</label>
                  <input type="text" class="form-control" id="editUserPhoneNumber" name="phoneNumber" required>
                </div>
                <div class="form-group">
                  <label for="editUserWorkRoom" class="form-label">Work Room</label>
                  <input type="text" class="form-control" id="editUserWorkRoom" name="workRoom" required>
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary" name="update_user">Save changes</button>
              </div>
            </form>
          </div>
        </div>
      </div>

      <!-- Change Password -->
      <div class="modal fade" id="changePasswordModal" tabindex="-1" role="dialog" aria-labelledby="changePasswordModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="changePasswordModalLabel">Change Password</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <form method="POST" action="users.php">
              <div class="modal-body">
                <input type="hidden" id="changePasswordUserId" name="id">
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
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary" name="change_password">Change Password</button>
              </div>
            </form>
          </div>
        </div>
      </div>

    </main>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <script src="./bootstrap.js"></script>

    
    <script>
      // using jQuery for edit and change password buttons
      $(document).ready(function() {
        $('.edit-btn').on('click', function() {
          const id = $(this).data('id');
          const name = $(this).data('name');
          const lastName = $(this).data('lastname');
          const email = $(this).data('email');
          const phoneNumber = $(this).data('phonenumber');
          const workRoom = $(this).data('workroom');

          $('#editUserId').val(id);
          $('#editUserName').val(name);
          $('#editUserLastName').val(lastName);
          $('#editUserEmail').val(email);
          $('#editUserPhoneNumber').val(phoneNumber);
          $('#editUserWorkRoom').val(workRoom);

          $('#editUserModal').modal('show');
        });

        $('.password-btn').on('click', function() {
          const id = $(this).data('id');
          $('#changePasswordUserId').val(id);
          $('#changePasswordModal').modal('show');
        });
      });
    </script>
  </body>
</html>

<?php
$conn->close();
?>