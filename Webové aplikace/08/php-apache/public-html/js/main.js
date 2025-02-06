
// for edit and change password buttons
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

  $('.delete-btn').on('click', function() {
    const id = $(this).data('id');
    $('#deleteUserId').val(id);
    $('#deleteUserModal').modal('show');
  });
});
