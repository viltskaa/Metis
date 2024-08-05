DROP TABLE IF EXISTS pallet;

CREATE TABLE pallet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tables_id INTEGER NOT NULL,
    surface_type INTEGER,
    hex_color TEXT,
    FOREIGN KEY (tables_id) REFERENCES tables(id)
);