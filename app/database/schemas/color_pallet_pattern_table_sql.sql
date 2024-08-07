DROP TABLE IF EXISTS color_pallet_pattern;

CREATE TABLE color_pallet_pattern (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surface_type INTEGER NOT NULL,
    hex_color TEXT NOT NULL,
    table_top_pattern_id INTEGER NOT NULL,
    FOREIGN KEY (table_top_pattern_id) REFERENCES table_top_pattern(id)
);