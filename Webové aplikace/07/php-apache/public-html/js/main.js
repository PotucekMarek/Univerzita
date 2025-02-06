$(document).ready(function() {
  console.log("main.js: Document ready");

  // Edit button click handler
  $('.edit-btn').on('click', function() {
      console.log('Edit button clicked');
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
      console.log('Password button clicked');
      const id = $(this).data('id');
      $('#changePasswordUserId').val(id);
      $('#changePasswordModal').modal('show');
  });
});