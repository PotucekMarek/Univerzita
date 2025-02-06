<!doctype html>
<html lang="en">
  <head>
    <title>Simple Dashboard</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../css/custom.css" rel="stylesheet"> <!-- compiled sass -->
    <link rel="stylesheet" href="../bootstrap-icons.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  </head>
  <body>
    <?php
    include 'header.php';
    include 'sidebar.php';
    ?>

    <div class="container-fluid">
      <div class="row">
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
          <h1 class="pb-3 border-bottom">Dashboard</h1>

          <section class="mt-5">
            <h2>Last 10 Users</h2>
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Username</th>
                </tr>
              </thead>

              <tbody>
                <?php
                $sql = "SELECT id, username FROM login_table ORDER BY id DESC LIMIT 10"; // draw out 10 users
                if ($result = $conn->query($sql)) {
                  $count = 1;
                  while ($row = $result->fetch_assoc()) {
                    echo "<tr>";
                    echo "<th scope=\"row\">" . $count . "</th>";
                    echo "<td>" . htmlspecialchars($row['username']) . "</td>";
                    echo "</tr>";
                    $count++;
                  }
                  $result->free();
                }
                ?>
              </tbody>
            </table>
          </section>

          <div class="mt-5">
            <nav aria-label="Page navigation example">
              <ul class="pagination justify-content-center">
                <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
              </ul>
            </nav>
          </div>
        </main>
      </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <script src="./bootstrap.js"></script>
  </body>
</html>