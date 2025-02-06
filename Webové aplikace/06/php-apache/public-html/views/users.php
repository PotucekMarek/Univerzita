

<!doctype html>
<html lang="en">
<head>
    <title>Users and Items</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../css/custom.css" rel="stylesheet">  <!-- compiled Sass -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.5.0/font/bootstrap-icons.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>

<body>
    <?php include 'header.php'; include 'sidebar.php'; ?>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
        <h1 class="pb-3 border-bottom">Users</h1>

        <div id="feedback" class="alert d-none" role="alert"></div>

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
                            <button type='button' class='btn btn-danger btn-sm delete-btn' data-id='<?php echo htmlspecialchars($user['id']); ?>'><i class='bi bi-trash'></i></button>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>

        <!-- Edit User Modal -->
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

        <!-- Change Password Modal -->
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

        <!-- Confirm Delete Modal -->
        <div class="modal fade" id="confirmDeleteModal" tabindex="-1" role="dialog" aria-labelledby="confirmDeleteModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="confirmDeleteModalLabel">Confirm Delete</h5>
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

    </main>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <script>
      $(document).ready(function() {
        let userIdToDelete = null;

        $('.edit-btn').on('click', function() {
          const data = $(this).data();
          $('#editUserId').val(data.id);
          $('#editUserName').val(data.name);
          $('#editUserLastName').val(data.lastname);
          $('#editUserEmail').val(data.email);
          $('#editUserPhoneNumber').val(data.phonenumber);
          $('#editUserWorkRoom').val(data.workroom);
          $('#editUserModal').modal('show');
        });

        $('.password-btn').on('click', function() {
            $('#changePasswordUserId').val($(this).data('id'));
            $('#changePasswordModal').modal('show');
        });

        $('.delete-btn').on('click', function() {
            userIdToDelete = $(this).data('id');
            $('#confirmDeleteModal').modal('show');
        });

        $('#confirmDeleteBtn').on('click', function() {
        if (userIdToDelete) {
            $.post('controllers/delete_user.php', { id: userIdToDelete }, function(response) {
                if (response.trim() === 'success') {
                    $('button[data-id="' + userIdToDelete + '"]').closest('tr').remove();
                    $('#confirmDeleteModal').modal('hide');
                }
            });
        }
      });
    });
  </script>
</body>
</html>