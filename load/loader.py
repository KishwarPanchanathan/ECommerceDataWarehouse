from io import StringIO
from database.olap_connection import get_olap_conn


def copy_dataframe(df, table_name):
    conn = get_olap_conn()
    buffer = StringIO()
    df.to_csv(buffer, index = False, header = False)
    buffer.seek(0)

    cols = ",".join(df.columns)

    with conn.cursor() as cur:
        cur.execute(f"TRUNCATE TABLE {table_name} RESTART IDENTITY")
        cur.copy_expert(f"COPY {table_name} ({cols}) FROM STDIN WITH CSV", buffer)

    conn.commit()
    conn.close()