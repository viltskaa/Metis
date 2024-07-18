DROP TABLE IF EXISTS additional_part;

CREATE TABLE additional_part (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_assembly INTEGER,
    article TEXT,
    user_id INTEGER,
    table_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (table_id) REFERENCES tables(id)
);