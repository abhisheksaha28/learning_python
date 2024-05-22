import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="abhi_postgressDB",
    user="Abhishek",
    password="abhishek@28",
    host="localhost",
    port="5432"
)

# Open cursor to perform database operation
cur = conn.cursor()

# Query the database 
cur.execute("SELECT * FROM second")
rows = cur.fetchall()

if not len(rows):
    print("Empty")

else:   
    for row in rows:
     print(row)


# Creating table as per requirement
sql = '''CREATE TABLE PUBLISHER(
                publisher_id SERIAL PRIMARY KEY,
                publisher_name VARCHAR(255) NOT NULL,
                publisher_estd INT,
                publsiher_location VARCHAR(255),
                publsiher_type VARCHAR(255)
)'''
cur.execute(sql)
print("Table created successfully........")
conn.commit()

# Close communications with database
cur.close()
conn.close()