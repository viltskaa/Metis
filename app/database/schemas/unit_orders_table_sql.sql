DROP TABLE IF EXISTS unit_orders;

CREATE TABLE unit_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    units_count INTEGER,
    unit_id INTEGER,
    orders_id INTEGER NOT NULL,
    unit_pattern_id INTEGER NOT NULL,
    FOREIGN KEY (unit_id) REFERENCES unit(id),
    FOREIGN KEY (orders_id) REFERENCES orders(id),
    FOREIGN KEY (unit_pattern_id) REFERENCES unit_pattern(id)
);