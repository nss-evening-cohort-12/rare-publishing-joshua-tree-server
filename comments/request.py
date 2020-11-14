import sqlite3
import json
from datetime import datetime
from sqlite3.dbapi2 import connect

from models.comment import Comment
from models.post import Post

def get_all_comments_post(id):
  with sqlite3.connect('./rare.db') as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
        c.id,
        c.user_id,
        c.post_id,
        c.subject,
        c.content,
        c.creation_date,
        u.first_name || ' ' || u.last_name AS full_name,
        p.title
    FROM Comments as c
    JOIN Users as u ON c.user_id = u.id
    JOIN Posts as p ON c.post_id = p.id
    WHERE c.post_id = ?
    ORDER BY c.creation_date DESC
    """, (id, ))
    
    comments = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      comment = Comment(row['id'], row['user_id'], row['post_id'],
                        row['subject'], row['content'], row['creation_date'], )
      comment = comment.__dict__
      comment['author'] = row['full_name']
      comment['title'] = row['title']
      comments.append(comment)
    
  return json.dumps(comments)


def create_comment(new_comment):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()
        date_now = datetime.now().strftime("%m/%d/%Y")

        db_cursor.execute(f"""
        INSERT INTO Comments
            ( user_id, post_id, subject, content, creation_date )
        VALUES
            ( ?, ?, ?, ?, ? );
        """, (new_comment['user_id'], new_comment['post_id'], new_comment['subject'], new_comment['content'], date_now, ))

    return json.dumps(new_comment)    

def delete_comment(id):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id ,))
