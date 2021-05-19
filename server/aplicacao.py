from flask import Flask, request, jsonify, abort

aplicacao = Flask(__name__)


"""
    Dificuldades:
        Aplicação e testes não utilizam mesma hierarquia de pastas.
    Para rodar os testes é necessário adicionar server.
    
        Problema em configurar de testes.
"""


@aplicacao.errorhandler(400)
def tratamento_erro(e):
    return jsonify(Erro=str(e)), 400


@aplicacao.route('/monitoramento', methods=['GET', 'POST'])
def monitoramento():
    from funcoes.processa_candle import processamento_candle

    if request.method == 'GET':
        moedas = request.args.get('moeda')
        periodo = request.args.get('periodo')

        moedas = [moedas]

    else:
        moedas = request.json.get('moeda', [])
        periodo = request.json.get('periodo')

        if not isinstance(moedas, list):
            moedas = [moedas]

    if not moedas:
        abort(400, description='Necessário informar uma moeda.')

    if not periodo:
        abort(400, 'Necessário informar um período para o processamento das cotações.')

    if not isinstance(periodo, int):
        periodo = int(periodo)

    periodo_em_segundos = periodo * 60
    processamento_candle(periodo_em_segundos, moedas)

    return jsonify('Processamento da cotação finalizado.'), 200


aplicacao.config["DEBUG"] = True
aplicacao.run()
