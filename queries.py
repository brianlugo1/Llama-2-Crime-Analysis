import psycopg2
import datetime



def create_connection():
    try:
        conn = psycopg2.connect("dbname=crime")

        cur = conn.cursor()

        return conn, cur
    except:
        return None, None


def create_table(conn, cur):
    cur.execute("CREATE TABLE IF NOT EXISTS crime (\
        id serial PRIMARY KEY, \
        day date NOT NULL, \
        messages JSONB NOT NULL \
    );")

    conn.commit()


def delete_table(conn, cur):
    cur.execute("DROP TABLE IF EXISTS crime;")

    conn.commit()


def clear_table(conn, cur):
    cur.execute("TRUNCATE crime;")

    conn.commit()

def insert_messages(conn, cur, messages):
    cur.execute(f"INSERT INTO crime (\
            day, messages \
        ) VALUES (\
            \'{datetime.datetime.now().date()}\',  \
            \'{messages}\' \
        );\
    ")

    conn.commit()

def select_messages_for_today(cur):
    cur.execute(
        f"select messages from crime where day = \'{datetime.datetime.now().date()}\';"
    )

    return cur.fetchall()