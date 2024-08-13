DROP TABLE IF EXISTS unit_tables;

CREATE TABLE unit_tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id INTEGER,
    tables_id INTEGER,
    FOREIGN KEY (unit_id) REFERENCES unit(id),
    FOREIGN KEY (tables_id) REFERENCES tables(id)
);