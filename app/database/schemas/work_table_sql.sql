DROP TABLE IF EXISTS works;

CREATE TABLE works (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    work_start INTEGER,
    work_end INTEGER,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);