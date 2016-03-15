from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware

from timetable.web import user


app = Flask(__name__, template_folder='web/templates',
            static_folder='web/static')


app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'timetable.web': ('static/sass', 'static/css', '/static/css')
})


def import_python(module_name: str):
    modules = module_name.split(':')
    if len(modules) != 2:
        return None
    try:
        return getattr(__import__(modules[0]), modules[1])
    except (ImportError, AttributeError):
        return None


app.add_template_global(import_python, 'import_python')
app.add_template_global(isinstance, 'isinstance')


app.register_blueprint(user.bp)


@app.route('/', methods=['GET'])
def hello():
    return render_template('hello.html')
