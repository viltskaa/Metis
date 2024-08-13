DROP TABLE IF EXISTS tables;

CREATE TABLE tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_start_assembly INTEGER,
    time_end_assembly INTEGER,
    table_pattern_id INTEGER,
    table_top_id INTEGER,
    FOREIGN KEY (table_top_id) REFERENCES table_top(id),
    FOREIGN KEY (table_pattern_id) REFERENCES table_pattern(id)
);