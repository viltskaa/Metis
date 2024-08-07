DROP TABLE IF EXISTS unit_pattern;

CREATE TABLE unit_pattern (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    image_path TEXT NOT NULL,
    type INTEGER NOT NULL
);