DROP TABLE IF EXISTS table_top_pattern;

CREATE TABLE table_top_pattern (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article TEXT UNIQUE,
    name TEXT,
    width REAL NOT NULL,
    height REAL NOT NULL,
    depth REAL,
    perimeter REAL NOT NULL,
    material TEXT,
    image_path TEXT NOT NULL
);