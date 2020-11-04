class Post():

    def __init__(self, id, user_id, title, content, category_id, publication_date, image_url = ''):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.category_id = category_id
        self.publication_date = publication_date
        self.image_url = image_url