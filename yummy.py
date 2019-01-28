from flask import Flask, Blueprint, url_for


app = Flask(__name__)


class UrlManager:
    @staticmethod
    def build_url(path):
        return path

    @staticmethod
    def build_static_url(path):
        path = path + '?version=' + "201901270953"
        return UrlManager.build_url(path)


route_yummy = Blueprint("yummy_page", __name__, url_prefix='/yummy')


@route_yummy.route("/")
def index():
    msg = "yummy index page"
    app.logger.info(msg)
    app.logger.debug(msg)
    app.logger.error(msg)
    return msg


@route_yummy.route("/hello")
def hello():
    url = url_for('yummy_page.index')
    url_1 = UrlManager.build_url('/yummy/')
    url_2 = UrlManager.build_static_url('/yummy/css/bootstrap.css')
    msg = "yummy hello page, %s, %s, %s" % (url, url_1, url_2)
    app.logger.info(msg)
    return msg


app.register_blueprint(route_yummy)


if __name__ == '__main__':
    app.run(port=8092, debug=True)
