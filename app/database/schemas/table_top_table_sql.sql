DROP TABLE IF EXISTS table_top;

CREATE TABLE table_top (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    width REAL,
    height REAL,
    perimeter REAL,
    depth REAL,
    color_main TEXT,
    color_edge TEXT,
    material TEXT,
    article TEXT UNIQUE,
    time_start_assembly INTEGER,
    time_end_assembly INTEGER,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);