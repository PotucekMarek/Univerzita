<!doctype html>
<html>
<head>
    <title>Register</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../css/custom.css" rel="stylesheet"> <!-- compiled sass -->
    <link rel="stylesheet" href="../bootstrap-icons.css">
    <?php include 'header.php'; include 'sidebar.php'; ?>
</head>
<body>
<main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
    <h1 class="pb-3 border-bottom">Register</h1>
    <section class="mt-5">
        <form method="POST" action="controllers/RegistrationController.php">
            <div class="col-md-6 mb-3">
                <label for="inputName" class="form-label">Username</label>
                <input type="text" class="form-control" id="inputName" name="username" required>
            </div>
            <div class="col-md-6 mb-3">
                <label for="inputPassword" class="form-label">Password</label>
                <input type="password" class="form-control" id="inputPassword" name="password" required>
            </div>
            <div class="col-md-6 mb-3">
                <label for="inputCPassword" class="form-label">Confirm Password</label>
                <input type="password" class="form-control" id="inputCPassword" name="cPassword" required>
            </div>
            <div class="col-md-6 mb-3">
                <label for="role" class="form-label">Role</label>
                <select class="form-control" id="role" name="role">
                    <option value="user">User</option>
                    <option value="admin">Admin</option>
                </select>
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-primary" name="submit">Register</button>
            </div>
        </form>

        <?php
        if (isset($msg)) {
            echo "<p class='mt-3'>$msg</p>";
        }
        ?>
    </section>
</main>
<script src="../bootstrap.js"></script>
</body>
</html>