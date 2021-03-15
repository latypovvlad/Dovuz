import sqlite3

__connection__ = None

def get_connection():
    global __connection__
    if __connection__ is None:
        __connection__ = sqlite3.connect('basaPerson.db', check_same_thread=False)
    return __connection__

def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS webADMIN')
        c.execute('DROP TABLE IF EXISTS usersReads')

    c.execute('''
            CREATE TABLE IF NOT EXISTS webADMIN(
                text     TEXT NOT NULL
            )
        ''')
    c.execute('''
                CREATE TABLE IF NOT EXISTS usersReads(
                    user_alias     TEXT NOT NULL,
                    chat_ID        INTEGER NOT NULL
                )
            ''')
    conn.commit()

def add_sait_admin(texts: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO webADMIN VALUES (?)', (texts, ))
    conn.commit()

def add_users_reads(user_alias: str, chat_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO usersReads VALUES (?, ?)', (user_alias, chat_id))
    conn.commit()

def read_sait_admin():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM webADMIN', )
    rows = c.fetchall()
    if len(rows) == 0:
        return -1
    else:
        return [i[0] for i in rows]


if __name__ == '__main__':
    init_db(force=True)
    add_sait_admin(texts='www.wada.com')
    print("Reset basa: complit!")
else:
    init_db(force=False)