DROP TABLE IF EXISTS time_point;

CREATE TABLE time_point (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status INTEGER,
    time INTEGER,
    task_id INTEGER NOT NULL,
    works_id INTEGER NOT NULL,
    FOREIGN KEY (task_id) REFERENCES task(id),
    FOREIGN KEY (works_id) REFERENCES works(id)
);