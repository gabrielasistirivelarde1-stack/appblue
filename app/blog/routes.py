from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, url_prefix='/blog', template_folder='templates')

ENTRADAS = {
    1: "Introduccion a Flask",
    2: "Que son los Blueprints",
    3: "Plantillas con Jinja2"
}

# /blog/entrada/1
@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    titulo = ENTRADAS.get(id, "Entrada no encontrada")
    return render_template('entrada.html', id=id, titulo=titulo)