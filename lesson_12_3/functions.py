import json
from json import JSONDecodeError


def save_picture(picture):
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ['png', 'jpg', 'bmp', 'svg']:
        return

    picture.save(f'./uploads/{filename}')
    return f'uploads/{filename}'


class PostHandler:
    def __init__(self, path):
        self.path = path

    def load_posts_data(self):
        posts = []
        try:
            with open(self.path, 'r', encoding="utf-8") as file:
                posts = json.load(file)
        except JSONDecodeError:
            return posts, 'Ошибка получения данных из файла JSON'

        return posts, None

    def search_posts(self, value):
        posts = []
        load_posts, error = self.load_posts_data()
        for post in load_posts:
            if value.lower() in post['content'].lower():
                posts.append(post)
        return posts, error

    def save_posts_to_json(self, posts):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

    def add_post(self, post):
        posts, error = self.load_posts_data()
        posts.append(post)
        self.save_posts_to_json(posts)
