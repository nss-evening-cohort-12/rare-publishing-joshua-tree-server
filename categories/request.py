import sqlite3
import json

from models.category import Category

CATEGORIES = []

def get_all_categories():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.category_name
        FROM categories c
        ORDER BY category_name ASC
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            category = Category(row['id'], row['category_name'])

            categories.append(category.__dict__)

    return json.dumps(categories)


def create_category(new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            ( category_name )
        VALUES
            ( ? );
        """, (new_category['category_name'], ))

        id = db_cursor.lastrowid

        new_category['id'] = id


    return json.dumps(new_category)
