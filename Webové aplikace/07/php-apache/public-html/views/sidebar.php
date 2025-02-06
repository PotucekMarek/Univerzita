<style>
/* some hacks for responsive sidebar */
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
  padding: 48px 0 0; /* height of navbar */
}

.sidebar-sticky {
  height: calc(100vh - 48px);
  overflow-x: hidden;
  overflow-y: auto;
}
</style>

<nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
  <div class="position-sticky pt-3 sidebar-sticky">
    <ul class="nav flex-column">
      <li class="nav-item">
        <a href="/dashboard" class="nav-link <?= basename($_SERVER['PHP_SELF']) == 'dashboard.php' ? 'active' : 'link-dark' ?>" aria-current="page">
          <span class="icon">
            <i class="bi bi-easel"></i>
          </span>
          Dashboard
        </a>
      </li>
      <li class="nav-item">
        <a href="/items" class="nav-link <?= basename($_SERVER['PHP_SELF']) == 'items.php' ? 'active' : 'link-dark' ?>">
          <span class="icon">
            <i class="bi bi-card-list"></i>
          </span>
          Items
        </a>
      </li>
      <li class="nav-item">
        <a href="/others" class="nav-link <?= basename($_SERVER['PHP_SELF']) == 'others.php' ? 'active' : 'link-dark' ?>">
          <span class="icon">
            <i class="bi bi-box"></i>
          </span>
          Others
        </a>
      </li>
      <li class="nav-item">
        <a href="/users" class="nav-link <?= basename($_SERVER['PHP_SELF']) == 'users.php' ? 'active' : 'link-dark' ?>">
          <span class="icon">
            <i class="bi bi-person-circle"></i>
          </span>
          Users
        </a>
      </li>
    </ul>
  </div>
</nav>
<script src="../bootstrap.js"></script>