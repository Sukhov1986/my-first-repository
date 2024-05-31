CREATE TABLE IF NOT EXISTS mainmenu(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL);

CREATE TABLE mobile_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    data_limit INTEGER,
    call_minutes INTEGER,
    validity_period INTEGER
    time INTEGER NOT NULL
);




