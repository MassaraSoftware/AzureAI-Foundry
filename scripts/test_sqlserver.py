import pyodbc

# Connection settings
server = "AI"
database = "TestDB"
username = "sa"
password = "Mass592322"

# Build connection string
conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    print("✅ Connected to SQL Server")
    print(f"Version: {row[0]}")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
