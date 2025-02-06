<?php

?>
<!doctype html>
<html lang="en">
  <head>
    <title>Others</title>
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

    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
      <h1 class="pb-3 border-bottom">Others</h1>
      <section class="mt-5">
        <h2>Notifications examples</h2>
        <div class="alert alert-success" role="alert">
          A simple success alert—check it out!
        </div>

        <div class="alert alert-danger" role="alert">
          A simple danger alert—check it out!
        </div>

        <div class="alert alert-info" role="alert">
          A simple info alert—check it out!
        </div>
      </section>

      <section class="mt-5">
        <h2>Badge examples</h2>
        <span class="badge text-bg-primary">Primary</span>
        <span class="badge text-bg-secondary">Secondary</span>
        <span class="badge text-bg-success">Success</span>
        <span class="badge text-bg-danger">Danger</span>
        <span class="badge text-bg-warning">Warning</span>
        <span class="badge text-bg-info">Info</span>
        <span class="badge text-bg-light">Light</span>
        <span class="badge text-bg-dark">Dark</span>
      </section>

      <section class="mt-5">
        <h2>Button examples</h2>
        <button type="button" class="btn btn-primary">Primary</button>
        <button type="button" class="btn btn-secondary">Secondary</button>
        <button type="button" class="btn btn-success">Success</button>
        <button type="button" class="btn btn-danger">Danger</button>
        <button type="button" class="btn btn-warning">Warning</button>
        <button type="button" class="btn btn-info">Info</button>
        <button type="button" class="btn btn-light">Light</button>
        <button type="button" class="btn btn-dark">Dark</button>
      </section>

      <section class="mt-5">
        <h2>Others</h2>
        <button type="button" class="btn btn-primary position-relative">
          Inbox
          <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
            99+
            <span class="visually-hidden">unread messages</span>
          </span>
        </button>
      </section>
    </main>
  </body>
  <script src="./bootstrap.js"></script>
</html>