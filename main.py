import psycopg2
import psycopg2.extras

conn = None

try:
    with psycopg2.connect(
        host='localhost',
        dbname = 'ecommerceoltp',
        user='postgres',
        password = 'admin',
        port = 5432
    ) as conn:
        print("Connected to PostgreSQL database successfully!")

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('SELECT * FROM orders LIMIT 5')
            for row in cur.fetchall():
                print(row['customer_id'],row['store_id'])

except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
