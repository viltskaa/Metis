DROP TABLE IF EXISTS table_top_pattern;

CREATE TABLE table_top_pattern (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    width REAL NOT NULL,
    height REAL NOT NULL,
    depth REAL NOT NULL,
    perimeter REAL NOT NULL,
    material TEXT NOT NULL,
    image_path TEXT NOT NULL
);