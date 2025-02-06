<!doctype html>
<html lang="en">
  <head>
    <title>Users</title>
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
      <h1 class="pb-3 border-bottom">Users</h1>

      <?php if ($successMessage): ?>
        <div class="alert alert-success alert-dismissible fade show" role="alert">
          <?php echo $successMessage; ?>
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
      <?php endif; ?>
      <?php if (isset($_SESSION['errorMessage'])): ?>
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
          <?php echo $_SESSION['errorMessage']; ?>
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        <?php unset($_SESSION['errorMessage']); ?>
      <?php endif; ?>

      <form method="POST" action="users">
        <input type="hidden" name="export_json" value="1">
        <button type="submit" class="btn btn-primary mb-3"><i class="bi bi-download"></i> Export to JSON</button>
      </form>

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
          <?php if (isset($users) && !empty($users)): ?>
            <?php foreach ($users as $user): ?>
              <tr id="user-<?php echo htmlspecialchars($user['id']); ?>">
                <th scope="row"><?php echo htmlspecialchars($user['id']); ?></th>
                <td><?php echo htmlspecialchars($user['name']); ?></td>
                <td><?php echo htmlspecialchars($user['lastName']); ?></td>
                <td><?php echo htmlspecialchars($user['email']); ?></td>
                <td><?php echo htmlspecialchars($user['phoneNumber']); ?></td>
                <td><?php echo htmlspecialchars($user['workRoom']); ?></td>
                <td>
                  <button class='btn btn-success btn-sm edit-btn' data-id='<?php echo htmlspecialchars($user['id']); ?>' data-name='<?php echo htmlspecialchars($user['name']); ?>' data-lastname='<?php echo htmlspecialchars($user['lastName']); ?>' data-email='<?php echo htmlspecialchars($user['email']); ?>' data-phonenumber='<?php echo htmlspecialchars($user['phoneNumber']); ?>' data-workroom='<?php echo htmlspecialchars($user['workRoom']); ?>'><i class='bi bi-pen'></i></button> 
                  <button class='btn btn-warning btn-sm password-btn' data-id='<?php echo htmlspecialchars($user['id']); ?>'><i class='bi bi-key'></i></button> 
                  
                  <!-- Form for deleting a user -->
                  <form method="POST" action="users" class="d-inline delete-user-form">
                    <input type="hidden" name="delete_user" value="1">
                    <input type="hidden" name="id" value="<?php echo htmlspecialchars($user['id']); ?>">
                    <button type="submit" class="btn btn-danger btn-sm delete-user-btn" data-id="<?php echo htmlspecialchars($user['id']); ?>"><i class='bi bi-trash'></i></button>
                  </form>
                </td>
              </tr>
            <?php endforeach; ?>
          <?php else: ?>
            <tr>
              <td colspan="7">No users found.</td>
            </tr>
          <?php endif; ?>
        </tbody>
      </table>

      <!-- edit user  -->
      <div class="modal fade" id="editUserModal" tabindex="-1" role="dialog" aria-labelledby="editUserModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="editUserModalLabel">Edit User</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <form method="POST" action="users">
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

      <!-- change password -->
      <div class="modal fade" id="changePasswordModal" tabindex="-1" role="dialog" aria-labelledby="changePasswordModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="changePasswordModalLabel">Change Password</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <form method="POST" action="users">
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
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function() {
            console.log("Document ready");

            // Edit button click handler
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

            // Password button click handler
            $('.password-btn').on('click', function() {
                const id = $(this).data('id');
                $('#changePasswordUserId').val(id);
                $('#changePasswordModal').modal('show');
            });

            // AJAX delete user
            $('.delete-user-btn').on('click', function(e) {
                e.preventDefault();
                const userId = $(this).data('id');
                const row = $(this).closest('tr');

                if (confirm('Are you sure you want to delete this user?')) {
                    $.ajax({
                        type: 'POST',
                        url: 'users',
                        data: {
                            delete_user: 1,
                            id: userId
                        },
                        success: function(response) {
                            const res = JSON.parse(response);
                            if (res.status === 'success') {
                                row.fadeOut(400, function() {
                                    $(this).remove();
                                });
                            } else {
                                alert('Failed to delete user.');
                            }
                        },
                        error: function() {
                            alert('Error deleting user.');
                        }
                    });
                }
            });

            // Close message after 3 seconds
            setTimeout(function() {
                $('.alert').alert('close');
            }, 3000);
        });
    </script>
    <script src="../js/main.js"></script>
  </body>
</html>