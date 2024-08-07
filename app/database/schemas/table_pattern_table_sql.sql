DROP TABLE IF EXISTS table_pattern;

CREATE TABLE table_pattern (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article TEXT UNIQUE,
    image_path TEXT NOT NULL,
    name TEXT NOT NULL,
    table_top_pattern_id INTEGER NOT NULL,
    FOREIGN KEY (table_top_pattern_id) REFERENCES table_top_pattern(id)
);