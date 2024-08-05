DROP TABLE IF EXISTS tables;

CREATE TABLE tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article TEXT UNIQUE,
    time_start_assembly INTEGER,
    time_end_assembly INTEGER,
    time_end_scanning INTEGER,
    qr_code TEXT,
    table_top_id INTEGER NOT NULL,
    marketplace_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (table_top_id) REFERENCES table_top(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);