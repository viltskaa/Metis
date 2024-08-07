DROP TABLE IF EXISTS task;

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL,
    created_date INTEGER NOT NULL,
    update_date INTEGER,
    exist_table_id INTEGER NOT NULL,
    user_id INTEGER,
    work_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (work_id) REFERENCES works(id),
    FOREIGN KEY (exist_table_id) REFERENCES exist_table(id)
);