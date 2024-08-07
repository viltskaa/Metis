DROP TABLE IF EXISTS color_pallet;

CREATE TABLE color_pallet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surface_type INTEGER,
    hex_color TEXT,
    table_top_id INTEGER,
    FOREIGN KEY (table_top_id) REFERENCES table_top(id)
);