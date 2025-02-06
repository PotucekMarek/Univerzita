const db = require('../config/db');

const User = {
  getAllUsers: () => {
    return new Promise((resolve, reject) => {
      db.query('SELECT * FROM users_table', (error, results) => {
        if (error) {
          return reject(error);
        }
        resolve(results);
      });
    });
  }
};

module.exports = User;