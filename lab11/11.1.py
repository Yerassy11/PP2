import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5434,
    dbname="phonebook",
    user="postgres",
    password="Vinsmoke_00"
)
cur = conn.cursor()

# Создаём функцию
function_in_sql = """
CREATE OR REPLACE FUNCTION search_records(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.name, phonebook.phone
    FROM phonebook
    WHERE phonebook.name ILIKE '%' || pattern || '%' 
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
"""
cur.execute(function_in_sql)
conn.commit()

# Ввод и вызов функции
pattern = input("Enter search pattern: ")
cur.execute("SELECT * FROM search_records(%s);", (pattern,))
rows = cur.fetchall()

if rows:
    print("Found entries:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
else:
    print("No results found.")

cur.close()
conn.close()
