<!doctype html>
<html lang="en">
    <head>
        <title>Dashboard</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link href="../css/custom.css" rel="stylesheet">  <!-- compiled sass -->
        <link rel="stylesheet" href="../bootstrap-icons.css">
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
                        <div id="root"></div>
                    </section>
                </main>
            </div>
        </div>

        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
        <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
        <script src="../bootstrap.js"></script>
        <script src="react/static/js/453.2a82e7ac.chunk.js"></script>
        <script src="react/static/js/main.7e269922.js"></script>
        <script>
            window.recentUsers = <?php echo json_encode($recentUsers); ?>;
        </script>
    </body>
</html>