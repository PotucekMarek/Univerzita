// routes/dataRoute.js
const express = require('express');
const path = require('path'); // Add this line to require the path module
const router = express.Router();

router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../views/data.php'));
});

module.exports = router;