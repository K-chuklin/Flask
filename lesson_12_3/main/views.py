from flask import Blueprint, render_template, request
import logging
from skypro.lesson_12_3.functions import PostHandler


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_blueprint.route("/")
def main():
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    subst = request.args.get('s')
    logging.info(f'Поиск:{subst}')
    post_handler = PostHandler('posts.json')
    posts, error = post_handler.search_posts(subst)
    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка!'
    return render_template("post_list.html", posts=posts, subst=subst)
