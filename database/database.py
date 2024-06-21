import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
                conv_id STRING NOT NULL UNIQUE,
                user_id INTEGER NOT NULL,
                title STRING NOT NULL
            );
            """
        )
    except Error as e:
        print(e)


def create_conversation(conn, conversation):
    """
    Create a new conversation into the conversations table
    :param conn:
    :param conversation:
    :return: conversation id
    """
    sql = """ INSERT OR IGNORE INTO conversations(conv_id,user_id,title)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, conversation)
    conn.commit()
    return cur.lastrowid


def get_user_conversation_count(conn, user_id):
    """
    Query count of all conversations for each user
    :param conn: the Connection object
    :param user_id:
    :return count of conversations
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM conversations WHERE user_id=?;",
        (user_id,),
    )

    conv_count = cur.fetchone()
    if conv_count:
        return conv_count[0]

    return 0


def select_conversations_by_user(conn, conversation_page):
    """
    Query conversations for each user by limit and offset
    :param conn: the Connection object
    :param user_id:
    :return list of conversations
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM conversations WHERE user_id=? ORDER BY id DESC LIMIT 10 OFFSET ?;",
        conversation_page,
    )

    results = cur.fetchall()

    return [
        {
            "id": item[0],
            "conversation_id": item[1],
            "user_id": item[2],
            "title": item[3],
        }
        for item in results
    ]


def select_conversation_by_id(conn, conversation):
    """
    Query conversation by conv_id
    :param conn: the Connection object
    :param conversation: (user_id, conv_id):
    :return list of conversations
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT conv_id, title FROM conversations WHERE user_id=? AND conv_id=?;",
        conversation,
    )

    item = cur.fetchone()

    return {"conversation_id": item[0], "title": item[1]}


def delete_conversation_by_id(conn, conversation):
    """
    Delete conversation by conv_id
    :param conn: the Connection object
    :param conversation: (user_id, conv_id):
    :return:
    """
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM conversations WHERE user_id=? AND conv_id=?;", conversation
    )
    conn.commit()

    return
