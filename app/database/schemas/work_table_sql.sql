DROP TABLE IF EXISTS works;

CREATE TABLE works (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time INTEGER NOT NULL,
    end_time INTEGER,
    worker_id INTEGER NOT NULL,
    taskmaster_id INTEGER NOT NULL,
    FOREIGN KEY (worker_id) REFERENCES worker(id),
    FOREIGN KEY (taskmaster_id) REFERENCES worker(id)
);