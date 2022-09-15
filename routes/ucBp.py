# importando o Blueprint e adicionando render_template
from flask import Blueprint, render_template
from ..extensions import db
from ..models.uc import Uc

# Instanciar o blueprint
ucBp = Blueprint('ucBP', __name__)

@ucBp.route('/uc')
def uc_list():
#    return "Teste"
    #nova adição
#    db.create_all()
# adiciona o acesso a banco e a chamada ao render_template
    ucs_query = Uc.query.all()
    return render_template('uc_list.html', ucs=ucs_query)