DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_top_id INTEGER,
    table_top_pattern_id INTEGER NOT NULL,
    table_pattern_id INTEGER NOT NULL,
    FOREIGN KEY (table_top_id) REFERENCES table_top(id),
    FOREIGN KEY (table_top_pattern_id) REFERENCES table_top_pattern(id),
    FOREIGN KEY (table_pattern_id) REFERENCES table_pattern(id)
);