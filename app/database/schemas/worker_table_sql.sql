DROP TABLE IF EXISTS worker;

CREATE TABLE worker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT NOT NULL,
    type INTEGER NOT NULL,
    password_hash TEXT NOT NULL
);