from flask import Blueprint, render_template, request
from Src.Resources.Amplitude import Amplitude
from Src.Resources.Profundidade import Profundidade
from Src.Resources.ProfLimitada import ProfLimitada
from Src.Resources.AprofInterativo import AprofInterativo
from Src.Resources.Bidirecional import Bidirecional
from Src.Resources.CustoUniforme import CustoUniforme
from Src.Resources.Greedy import Greedy
from Src.Resources.Aestrela import Aestrela
from Src.Resources.AIAestrela import AIAestrela
from Src.Util.functions import gerar_mapa, posicoes_possiveis, gera_H


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
    portalMap = gerar_mapa(request.args.get('portalMap'))

    search = Amplitude(inicio, fim, mapa, portalMap)

    return search.make()


@Router.route("/profundidade")
def profundidade():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    portalMap = gerar_mapa(request.args.get('portalMap'))

    search = Profundidade(inicio, fim, mapa, portalMap)

    return search.make()


@Router.route("/profLimitada")
def profLimitada():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    limite = int(request.args.get('limite'))
    portalMap = gerar_mapa(request.args.get('portalMap'))

    search = ProfLimitada(inicio, fim, mapa, limite, portalMap)

    return search.make()


@Router.route("/aprofInterativo")
def aprofInterativo():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    portalMap = gerar_mapa(request.args.get('portalMap'))

    search = AprofInterativo(inicio, fim, mapa, portalMap)

    return search.make()


@Router.route("/bidirecional")
def bidirecional():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    portalMap = gerar_mapa(request.args.get('portalMap'))

    search = Bidirecional(inicio, fim, mapa, portalMap)

    return search.make()

@Router.route("/custoUniforme")
def custoUniforme():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    portalMap = gerar_mapa(request.args.get('portalMap'))
    weightMap = gerar_mapa(request.args.get('weightMap'))

    search = CustoUniforme(inicio, fim, mapa, portalMap, weightMap)

    return search.make(inicio, fim) 

@Router.route("/greedy")
def greedy():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    portalMap = gerar_mapa(request.args.get('portalMap'))
    weightMap = gerar_mapa(request.args.get('weightMap'))

    search = Greedy(inicio, fim, mapa, portalMap, weightMap, posicoes_possiveis(mapa))

    return search.make(inicio, fim, gera_H(posicoes_possiveis(mapa))) 


@Router.route("/aestrela")
def aestrela():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    portalMap = gerar_mapa(request.args.get('portalMap'))
    weightMap = gerar_mapa(request.args.get('weightMap'))

    search = Aestrela(inicio, fim, mapa, portalMap, weightMap, posicoes_possiveis(mapa))

    return search.make(inicio, fim, gera_H(posicoes_possiveis(mapa))) 


@Router.route("/aiaestrela")
def aiaestrela():
    mapa = gerar_mapa(request.args.get('mapa'))
    inicio = [int(i) for i in request.args.get('inicio').split(',')][::-1]
    fim = [int(i) for i in request.args.get('fim').split(',')][::-1]
    portalMap = gerar_mapa(request.args.get('portalMap'))
    weightMap = gerar_mapa(request.args.get('weightMap'))

    search = AIAestrela(inicio, fim, mapa, portalMap, weightMap, posicoes_possiveis(mapa))

    return search.make(inicio, fim, gera_H(posicoes_possiveis(mapa))) 