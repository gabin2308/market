import sqlite3

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = BASE_DIR /"schema.sql"
DB_PATH = BASE_DIR / "database.db"

connection = sqlite3.connect(DB_PATH)

with open(SCHEMA_PATH, encoding="utf-8") as f:
    connection.executescript(f.read())  

connection.commit()
connection.close()

print("Database initialisée avec succès !")