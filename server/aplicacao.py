from flask import Flask, request

aplicacao = Flask(__name__)


@aplicacao.route('/monitoramento', methods=['GET', 'POST'])
def monitoramento():
    from bd.candlestick import insere_candlestick
    from classes.candlestick import Candlestick
    import requests
    import time

    if request.method == 'GET':
        moedas = request.args.get('moeda')
        periodo = request.args.get('periodo')
    else:
        moedas = request.json.get('moeda', [])
        periodo = request.json.get('periodo')

    if not moedas:
        return 'Necessário informar uma moeda.', 400

    if not periodo:
        return 'Necessário informar um período para o processamento das cotações.', 400

    if not isinstance(periodo, int):
        periodo = int(periodo)

    if not isinstance(moedas, list):
        moedas = [moedas]

    periodo_em_segundos = periodo * 60
    tempo_decorrido = 0
    tempo_espera = 10

    objeto_moedas = {}
    for moeda in moedas:
        objeto_moedas[moeda] = Candlestick()

    while tempo_decorrido <= periodo_em_segundos:
        resposta_api = requests.get('https://poloniex.com/public?command=returnTicker')

        if resposta_api.status_code != 200:
            return 'Erro ao realizar chamada da API Poloniex.', 400

        dados_retorno_api = resposta_api.json()

        for moeda, candle in objeto_moedas.items():
            if not dados_retorno_api.get(moeda):
                return f'Moeda {moeda} não encontrada nos dados retornados da API Poloniex.', 400

            valor_recente_candle = float(dados_retorno_api[moeda].get('last'))

            if not tempo_decorrido:
                candle.inicializa_candle(valor_recente_candle)

            candle.atualiza_valor_minimo_maximo(valor_recente_candle)
            candle.atualiza_valor_fechamento_candle(valor_recente_candle)

        time.sleep(tempo_espera)
        tempo_decorrido += tempo_espera

    insere_candlestick(objeto_moedas)

    return 'Processamento da cotação finalizado.', 200


aplicacao.config["DEBUG"] = True
aplicacao.run()
