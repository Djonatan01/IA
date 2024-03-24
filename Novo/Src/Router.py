from flask import Blueprint, render_template, request
from Src.Resources.Amplitude import Amplitude
from Src.Util.functions import gerar_mapa


Router = Blueprint('router', __name__)

@Router.route("/")
@Router.route("/home")
def home():
    return render_template('index.html')

@Router.route("/amplitude")
def amplitude():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')]
    fim = [int(i) for i in request.args.get('fim').split(',')]

    search = Amplitude(inicio, fim, mapa)

    return search.make()