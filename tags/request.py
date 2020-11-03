import sqlite3
import json

from models.tag import Tag

def get_all_tags():
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.name
        FROM Tags t
        """)

        tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            tag = Tag(row['id'], row['name'])
            tags.append(tag.__dict__)

    return json.dumps(tags)

def create_tag(new_tag):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( name )
        VALUES
            ( ? );
        """, (new_tag['name'], ))

        id = db_cursor.lastrowid
        new_tag['id'] = id

    return json.dumps(new_tag)