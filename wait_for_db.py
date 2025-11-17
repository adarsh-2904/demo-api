# wait_for_db.py
import os
import time
import pymysql

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "fastapi_db")

MAX_RETRIES = 30
RETRY_DELAY = 2  # seconds

for attempt in range(1, MAX_RETRIES + 1):
    try:
        conn = pymysql.connect(host=DB_HOST, port=DB_PORT,
                               user=DB_USER, password=DB_PASSWORD,
                               database=DB_NAME, connect_timeout=5)
        conn.close()
        print("✅ Database is reachable")
        break
    except Exception as e:
        print(f"Waiting for DB (attempt {attempt}/{MAX_RETRIES})... {e}")
        time.sleep(RETRY_DELAY)
else:
    print("❌ Could not connect to the database after retries. Exiting.")
    raise SystemExit(1)
