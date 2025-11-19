import sqlite3

def connect():
    try:
        con = sqlite3.connect("payroll.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees(
                emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                designation TEXT NOT NULL,
                department TEXT,
                salary REAL,
                status TEXT
            )
        """)
        con.commit()
        return con
    except Exception as e:
        print("Database connection error:", e)
        return None
