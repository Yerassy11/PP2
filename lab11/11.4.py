import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5434,
    dbname="phonebook",
    user="postgres",
    password="Vinsmoke_00"
)
cur = conn.cursor()

pagination_function_sql = """CREATE OR REPLACE FUNCTION get_paginated_users(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;

"""

cur.execute(pagination_function_sql)
conn.commit()
print("Pagination function created successfully.\n")

limit = int(input("Enter how many records to display per page (LIMIT): "))
offset = int(input("Enter how many records to skip (OFFSET): "))

cur.execute("SELECT * FROM get_paginated_users(%s, %s);", (limit, offset))
rows = cur.fetchall()

print("\nPaginated Results:")
if rows:
    for row in rows:
        print("ID: ", row[0]," Name:", row[1]," Phone: ", row[2])
else:
    print("No data found!")

cur.close()
conn.close()