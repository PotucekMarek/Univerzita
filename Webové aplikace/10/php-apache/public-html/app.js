const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// MySQL připojení
const connection = mysql.createConnection({
    host: 'localhost',
    port: '3306',
    user: 'root',
    password: '',
    database: 'user_database'
});

connection.connect((err) => {
    if (err) {
        console.error('Error connecting to the database:', err);
        return;
    }
    console.log('Connected to the MySQL server.');
});

// Middleware pro logování
const log = function(req, res, next) {
  console.log(`${req.method} ${req.url}`);
  next(); // předání řízení
}

// Middleware pro obsluhu všech požadavků
const handler = function(req, res, next) {
  const { controler, method, params } = req.params;

  // vypsání POST
  console.log(JSON.stringify(req.body));

  res.send(`controler: ${controler}, method: ${method}, params: ${params}`);
  next();
}

app.all('/:controler/:method/:params(*)', [log, handler]);

// get all users
app.get('/api/users', (req, res) => {
    connection.query('SELECT * FROM user_table', (err, rows) => {
        if (err) {
            res.status(500).send(err);
        } else {
            res.json(rows);
        }
    });
});

// get user by ID
app.get('/api/users/:id', (req, res) => {
    const { id } = req.params;
    connection.query('SELECT * FROM user_table WHERE id = ?', [id], (err, rows) => {
        if (err) {
            res.status(500).send(err);
        } else if (rows.length === 0) {
            res.status(404).send({ message: 'User not found' });
        } else {
            res.json(rows[0]);
        }
    });
});

// create a new user
app.post('/api/users', (req, res) => {
    const { name, lastName, email, phoneNumber, workRoom } = req.body;
    connection.query(
        'INSERT INTO user_table (name, lastName, email, phoneNumber, workRoom) VALUES (?, ?, ?, ?, ?)', 
        [name, lastName, email, phoneNumber, workRoom], 
        (err, result) => {
            if (err) {
                res.status(500).send(err);
            } else {
                res.status(201).send({ message: 'User created', id: result.insertId });
            }
        }
    );
});

// update user
app.put('/api/users/:id', (req, res) => {
    const { id } = req.params;
    const { name, lastName, email, phoneNumber, workRoom } = req.body;
    connection.query(
        'UPDATE user_table SET name = ?, lastName = ?, email = ?, phoneNumber = ?, workRoom = ? WHERE id = ?', 
        [name, lastName, email, phoneNumber, workRoom, id], 
        (err) => {
            if (err) {
                res.status(500).send(err);
            } else {
                res.send({ message: 'User updated' });
            }
        }
    );
});

// delete user
app.delete('/api/users/:id', (req, res) => {
    const { id } = req.params;
    connection.query('DELETE FROM user_table WHERE id = ?', [id], (err) => {
        if (err) {
            res.status(500).send(err);
        } else {
            res.send({ message: 'User deleted' });
        }
    });
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});