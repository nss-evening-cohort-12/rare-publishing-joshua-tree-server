import sqlite3
import json
from datetime import datetime

from models.post import Post
from models.user import User
from models.category import Category

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
            p.image_url,
            c.category_name,
            u.first_name || ' ' || u.last_name AS full_name
        FROM Posts as p
        JOIN Users as u ON p.user_id = u.id
        JOIN Categories as c ON p.category_id = c.id
        """)

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['title'], row['content'], row['category_id'], row['publication_date'], row['image_url'])
            post = post.__dict__
            post['full_name'] = row['full_name']
            post['category_name'] = row['category_name']
            posts.append(post)

    return json.dumps(posts)

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
