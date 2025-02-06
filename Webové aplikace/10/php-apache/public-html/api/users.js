const express = require('express');
const router = express.Router();

// Middleware to ensure session exists
router.use((req, res, next) => {
  if (!req.session.users) {
    req.session.users = [];
  }
  next();
});

// GET /api/users - Get all users
router.get('/', (req, res) => {
  res.json(req.session.users);
});

// GET /api/users/:id - Get user by ID
router.get('/:id', (req, res) => {
  const user = req.session.users.find(u => u.id == req.params.id);
  if (user) {
    res.json(user);
  } else {
    res.status(404).json({ message: 'User not found' });
  }
});

// POST /api/users - Create a new user
router.post('/', (req, res) => {
  const { id, name, surname } = req.body;
  req.session.users.push({ id, name, surname });
  res.status(201).json({ message: 'User created' });
});

// PUT /api/users/:id - Update user by ID
router.put('/:id', (req, res) => {
  const { name, surname } = req.body;
  const user = req.session.users.find(u => u.id == req.params.id);
  if (user) {
    user.name = name;
    user.surname = surname;
    res.json({ message: 'User updated' });
  } else {
    res.status(404).json({ message: 'User not found' });
  }
});
// DELETE /api/users/:id - Delete user by ID
router.delete('/:id', (req, res) => {
    const userIndex = req.session.users.findIndex(u => u.id == req.params.id);
    if (userIndex !== -1) {
      req.session.users.splice(userIndex, 1);
      res.json({ message: 'User deleted' });
    } else {
      res.status(404).json({ message: 'User not found' });
    }
  });
  
  module.exports = router;