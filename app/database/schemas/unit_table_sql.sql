DROP TABLE IF EXISTS unit;

CREATE TABLE unit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_start_assembly INTEGER,
    time_end_assembly INTEGER,
    unit_pattern_id INTEGER,
    FOREIGN KEY (unit_pattern_id) REFERENCES unit_pattern(id)
);