DROP TABLE IF EXISTS unit_pattern_table_pattern;

CREATE TABLE unit_pattern_table_pattern (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_pattern_id INTEGER NOT NULL,
    unit_pattern_id INTEGER NOT NULL,
    units_count INTEGER NOT NULL,
    FOREIGN KEY (table_pattern_id) REFERENCES table_pattern(id),
    FOREIGN KEY (unit_pattern_id) REFERENCES unit_pattern(id)
);