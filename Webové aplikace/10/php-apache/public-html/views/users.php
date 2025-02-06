<!doctype html>
<html lang="en">
  <head>
    <title>Users and Items</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="css/custom.css" rel="stylesheet">  <!-- compiled Sass -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.5.0/font/bootstrap-icons.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link href="../css/custom.css" rel="stylesheet">  <!-- compiled sass -->
    <link rel="stylesheet" href="../bootstrap-icons.css">
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
            <th scope="col">Emaily</th>
            <th scope="col">Phone</th>
            <th scope="col">Work Room</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        
        <tbody>
          <?php foreach ($users as $user): ?>
            <tr>
              <th scope="row"><?php echo htmlspecialchars($user['id']); ?></th>
              <td><?php echo htmlspecialchars($user['name']); ?></td>
              <td><?php echo htmlspecialchars($user['lastName']); ?></td>
              <td><?php echo htmlspecialchars($user['email']); ?></td>
              <td><?php echo htmlspecialchars($user['phoneNumber']); ?></td>
              <td><?php echo htmlspecialchars($user['workRoom']); ?></td>
              <td>
                <button class='btn btn-success btn-sm edit-btn' data-id='<?php echo htmlspecialchars($user['id']); ?>' data-name='<?php echo htmlspecialchars($user['name']); ?>' data-lastname='<?php echo htmlspecialchars($user['lastName']); ?>' data-email='<?php echo htmlspecialchars($user['email']); ?>' data-phonenumber='<?php echo htmlspecialchars($user['phoneNumber']); ?>' data-workroom='<?php echo htmlspecialchars($user['workRoom']); ?>'><i class='bi bi-pen'></i></button> 
                <button class='btn btn-warning btn-sm password-btn' data-id='<?php echo htmlspecialchars($user['id']); ?>'><i class='bi bi-key'></i></button> 
                <button class='btn btn-danger btn-sm delete-btn' data-id='<?php echo htmlspecialchars($user['id']); ?>' data-toggle='modal' data-target='#deleteConfirmModal'><i class='bi bi-trash'></i></button>
              </td>
            </tr>
          <?php endforeach; ?>
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
            <form method="POST" action="../controllers/UsersController.php">
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
                  <label for="editUserEmail" class="form-label">Emaily</label>
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
            <form method="POST" action="../controllers/UsersController.php">
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

      <!-- Delete Confirm Modal -->
      <div class="modal fade" id="deleteConfirmModal" tabindex="-1" role="dialog" aria-labelledby="deleteConfirmModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="deleteConfirmModalLabel">Confirm Delete</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              Are you sure you want to delete this user?
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">No</button>
              <button type="button" class="btn btn-danger" id="confirmDeleteBtn">Yes</button>
            </div>
          </div>
        </div>
      </div>

      <button class="btn btn-secondary mb-3" id="saveToJsonBtn">Save to JSON</button>

    </main>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

    <script>
      // using jQuery for edit and change password buttons
      $(document).ready(function() {
        var deleteUserId;

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

        $('.delete-btn').on('click', function() {
          deleteUserId = $(this).data('id');
          $('#deleteConfirmModal').modal('show');
        });

        $('#confirmDeleteBtn').on('click', function() {
          $.ajax({
            url: '../controllers/UsersController.php',
            type: 'POST',
            data: { delete_user: true, id: deleteUserId },
            success: function(response) {
              window.location.reload();
            }
          });
        });

        $('#saveToJsonBtn').on('click', function() {
          $.ajax({
            url: '../controllers/UsersController.php',
            type: 'POST',
            data: { export_json: true },
            success: function(response) {
              alert(response);
            }
          });
        });
      });
    </script>
  </body>
</html>