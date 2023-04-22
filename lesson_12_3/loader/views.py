import logging
from flask import Blueprint, render_template, request
from skypro.lesson_12_3.functions import PostHandler, save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/post")
def create_new_post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=['POST'])
def create_new_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        logging.info('Не все строки заполнены')
        return 'Не все строки заполнены'
    picture_path = save_picture(picture)
    if not picture_path:
        logging.info('Загружено не изображения')
        return 'Загружено не изображения'

    post_handler = PostHandler('posts.json')
    new_post = {"pic": picture_path, "content": content}
    post_handler.add_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
