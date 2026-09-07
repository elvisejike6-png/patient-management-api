CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR,
    age VARCHAR,
    passport VARCHAR
);

CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR,
    specialization VARCHAR
);

CREATE TABLE IF NOT EXISTS "assign" (
    doctor_id INT,
    patient_id INTEGER
);