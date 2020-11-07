import sqlite3
import json
from datetime import datetime

from models.post import Post

def get_all_posts():
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.title,
            p.content,
            p.category_id,
            p.publication_date,
            p.image_url
        FROM Posts p
        """)

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['title'], row['content'], row['category_id'], row['publication_date'], row['image_url'])
            posts.append(post.__dict__)

    return json.dumps(posts)

def get_single_post(id):
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.title,
            p.content,
            p.category_id,
            p.publication_date,
            p.image_url
        FROM Posts p
        WHERE p.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        post = Post(data['id'], data['user_id'], data['title'], data['content'], data['category_id'], data['publication_date'], data['image_url'])

    return json.dumps(post.__dict__)

def create_post(new_post):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()
        date_now = datetime.now().strftime("%d/%m/%Y %H:%M")

        db_cursor.execute(f"""
        INSERT INTO Posts
            ( user_id, title, content, category_id, publication_date, image_url )
        VALUES
            ( ?, ?, ?, ?, ?, ? );
        """, (new_post['user_id'], new_post['title'], new_post['content'], new_post['category_id'], date_now, new_post['image_url'], ))

    return json.dumps(new_post)