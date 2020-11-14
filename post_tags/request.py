import sqlite3
import json

def create_post_tag(new_post_tag):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Post_Tags
            ( post_id, tag_id )
        VALUES ( ?, ? )
        """, (new_post_tag['post_id'], new_post_tag['tag_id']))
    return json.dumps(new_post_tag)

def delete_post_tags(id):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Post_Tags
        WHERE post_id = ?
        """, (id, ))
