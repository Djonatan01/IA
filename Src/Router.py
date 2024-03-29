from flask import Blueprint, render_template, request
from Src.Resources.Amplitude import Amplitude
from Src.Resources.Profundidade import Profundidade
from Src.Resources.ProfLimitada import ProfLimitada
from Src.Resources.AprofInterativo import AprofInterativo
from Src.Resources.Bidirecional  import Bidirecional
from Src.Util.functions import gerar_mapa


Router = Blueprint('router', __name__)

@Router.route("/")
@Router.route("/home")
def home():
    return render_template('index.html')

@Router.route("/amplitude")
def amplitude():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]

    search = Amplitude(inicio, fim, mapa)

    return search.make()

@Router.route("/profundidade")
def profundidade():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]

    search = Profundidade(inicio, fim, mapa)

    return search.make()

@Router.route("/profLimitada")
def profLimitada():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    limite = int(request.args.get('limite'))

    search = ProfLimitada(inicio, fim, mapa, limite)

    return search.make()

@Router.route("/aprofInterativo")
def aprofInterativo():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]

    search = AprofInterativo(inicio, fim, mapa)

    return search.make()

@Router.route("/bidirecional")
def bidirecional():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]

    search = Bidirecional(inicio, fim, mapa)

    return search.make()
