from flask import Flask, Blueprint


route_yummy = Blueprint("yummy_page", __name__, url_prefix='/yummy')


@route_yummy.route("/")
def index():
    return "yummy index page"


@route_yummy.route("/hello")
def hello():
    return "yummy hello page"


app = Flask(__name__)
app.register_blueprint(route_yummy)


if __name__ == '__main__':
    app.run(port=8092)
