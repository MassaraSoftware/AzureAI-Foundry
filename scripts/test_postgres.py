import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="Mass592322",  # replace with your real password
    port=5432
)

cur = conn.cursor()
cur.execute("SELECT version();")
print("✅ Connected to:", cur.fetchone())

cur.close()
conn.close()
