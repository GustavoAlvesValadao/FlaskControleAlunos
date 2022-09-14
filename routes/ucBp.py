# importando o Blueprint
from flask import Blueprint

# Instanciar o blueprint
ucBp = Blueprint('ucBP', __name__)

@ucBp.route('/uc')
def uc_list():
    return "Teste"