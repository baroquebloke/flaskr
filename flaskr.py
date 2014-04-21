from flask import (
    Flask,
    render_template
)
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route('/joke')
def joke():
    return "HHAHAHAHAHAHAHAHAHAHAHA"

@app.route('/', defaults={'path': 'about_me'})
@app.route('/<path:path>')
def show_page(path):
    templates = [t.format(path=path)
                 for t in 'pages/{path}.html', '{path}.html']
    try:
        return render_template(templates)
    except TemplateNotFound:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
