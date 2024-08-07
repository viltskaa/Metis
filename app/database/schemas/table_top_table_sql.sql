DROP TABLE IF EXISTS table_top;

CREATE TABLE table_top (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    width REAL,
    height REAL,
    perimeter REAL,
    depth REAL,
    time_start_assembly INTEGER,
    time_end_assembly INTEGER,
    response INTEGER,
    image_path TEXT,
    table_top_pattern_id INTEGER,
    FOREIGN KEY (table_top_pattern_id) REFERENCES table_top_pattern(id)
);