# importando o Blueprint e adicionando render_template
from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.uc import Uc
from datetime import date, datetime

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

@ucBp.route('/uc/create')
def create_uc():
    return render_template('uc_create.html')

@ucBp.route('/uc/add', methods=["POST"])
def add_uc():

    sNome = request.form["nome"]
    sTipo = request.form["tipo"]
    dInicio = datetime.strptime(request.form["inicio"], '%Y-%m-%d')
    dFim = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc(nome=sNome, tipo=sTipo, inicio=dInicio, fim=dFim)
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for("ucBp.uc_list"))