# importando o Blueprint
from flask import Blueprint
from ..extensions import db
from ..models.uc import Uc

# Instanciar o blueprint
ucBp = Blueprint('ucBP', __name__)

@ucBp.route('/uc')
def uc_list():
    #return "Teste"
    #nova adição
    db.create_all()