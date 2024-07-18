DROP TABLE IF EXISTS work;

CREATE TABLE work (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    work_start INTEGER,
    work_end INTEGER,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);