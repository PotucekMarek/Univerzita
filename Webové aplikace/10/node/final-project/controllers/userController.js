

const User = require('../models/userModel');

// Function to get all users
const getUsers = async (req, res) => {
  try {
    const users = await User.getAllUsers();
    console.log('Fetched users from database:', users); // Log fetched users
    res.json(users);
  } catch (error) {
    console.error('Error fetching users:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
};

module.exports = {
  getUsers
};