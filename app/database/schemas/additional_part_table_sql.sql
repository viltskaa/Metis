DROP TABLE IF EXISTS additional_part;

CREATE TABLE additional_part (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_start_assembly INTEGER,
    time_end_assembly INTEGER,
    time_end_scanning INTEGER,
    article TEXT,
    user_id INTEGER NOT NULL,
    table_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (table_id) REFERENCES tables(id)
);