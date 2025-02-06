<!doctype html>
<html lang="en">
  <head>
    <title>User Data</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../css/custom.css" rel="stylesheet"> <!-- compiled sass -->
    <link rel="stylesheet" href="../bootstrap-icons.css">
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
              <form method="post" action="data">
                <input type="hidden" name="edit_user" value="1">
                <button type="submit" class="btn btn-success btn-sm"><i class="bi bi-pen"></i> Edit</button>
              </form>
              <form method="post" action="data">
                <input type="hidden" name="show_change_password" value="1">
                <button type="submit" class="btn btn-warning btn-sm"><i class="bi bi-key"></i> Change Password</button>
              </form>
            <?php else: ?>
              <p>No user data found. Please add your details:</p>
              <form method="post" action="data">
                <input type="hidden" name="edit_user" value="1">
                <button type="submit" class="btn btn-primary btn-sm"><i class="bi bi-plus"></i> Add Data</button>
              </form>
            <?php endif; ?>
          </section>
        </main>
      </div>
    </div>

    <!-- edit user -->
    <div class="modal fade<?php if ($showEditModal) echo ' show d-block'; ?>" id="editUserModal" tabindex="-1" role="dialog" aria-labelledby="editUserModalLabel" aria-hidden="true" style="<?php if ($showEditModal) echo 'display: block;'; ?>">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editUserModalLabel">Edit User</h5>
            <form method="post" action="data">
              <button type="submit" class="close" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </form>
          </div>
          <form method="POST" action="data">
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

    <!-- change password -->
    <div class="modal fade<?php if ($showPasswordModal) echo ' show d-block'; ?>" id="changePasswordModal" tabindex="-1" role="dialog" aria-labelledby="changePasswordModalLabel" aria-hidden="true" style="<?php if ($showPasswordModal) echo 'display: block;'; ?>">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="changePasswordModalLabel">Change Password</h5>
            <form method="post" action="data">
              <button type="submit" class="close" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </form>
          </div>
          <form method="POST" action="data">
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