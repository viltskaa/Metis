DROP TABLE IF EXISTS tables;

CREATE TABLE tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article TEXT UNIQUE,
    time_start_assembly INTEGER,
    time_end_assembly INTEGER,
    qr_code TEXT,
    table_top_id INTEGER,
    marketplace_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (table_top_id) REFERENCES table_top(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);