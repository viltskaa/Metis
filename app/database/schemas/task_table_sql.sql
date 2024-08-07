DROP TABLE IF EXISTS task;

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_date INTEGER NOT NULL,
    status INTEGER NOT NULL,
    worker_type INTEGER,
    orders_id INTEGER NOT NULL,
    FOREIGN KEY (orders_id) REFERENCES orders(id)
);