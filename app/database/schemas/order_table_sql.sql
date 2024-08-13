DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tables_id INTEGER,
    table_pattern_id INTEGER NOT NULL,
    FOREIGN KEY (tables_id) REFERENCES tables(id),
    FOREIGN KEY (table_pattern_id) REFERENCES table_pattern(id)
);