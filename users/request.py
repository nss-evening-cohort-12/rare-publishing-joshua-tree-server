import sqlite3
import json
from models.user import User


def get_users_by_email(email, password):

    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
          select
              u.id,
              u.first_name,
              u.last_name,
              u.display_name,
              u.email,
              u.password
          from Users u
          where u.email = ? AND u.password = ?
        """, ( email, password))

        #users = []
        user = {}
        row = db_cursor.fetchone()
        if row == None:
            user['valid'] = False
            #user = user.__dict__
        else:
            user = User(row['id'], row['first_name'], row['last_name'],row['display_name'], row['email'] , row['password'])
            user = user.__dict__
            user['valid'] = True

        #user = User(row['id'], row['first_name'], row['last_name'],row['display_name'], row['email'] , row['password'])
        #users.append(user.__dict__)

        #print("getting email and pass")
    return json.dumps(user)

def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Users
            ( first_name, last_name, display_name, email, password )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_user['first_name'], new_user['last_name'],
              new_user['display_name'], new_user['email'],
              new_user['password'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_user['id'] = id
        new_user['valid'] = True


    return json.dumps(new_user)    

def get_all_users():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.display_name,
            u.email,
            u.password
        FROM users u
        """)

        # Initialize an empty list to hold all animal representations
        users = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            user = User(row['id'], row['first_name'], row['last_name'], row['display_name'],
                            row['email'], row['password'])

            users.append(user.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(users)
