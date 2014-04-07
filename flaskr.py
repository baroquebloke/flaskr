

from flask import Flask

from jinja2 import TemplateNotFound



app = Flask(__name__)


@app.route('/', defaults={'path': 'index'})
@app.route('/<path:path>')
def show_page(path):
    templates = [t.format(path=path) for t \
                 in 'pages/{path}.html', '{path}.html']
    try:
        return render_template(templates, **site_variables())
    except TemplateNotFound:
        return render_template('404.html', **site_variables()), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
