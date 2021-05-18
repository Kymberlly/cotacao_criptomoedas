from flask import Flask

aplicacao = Flask(__name__)


@aplicacao.route('/monitoramento/<string:moeda>/<int:periodo>', methods=['GET'])
def monitoramento(moeda, periodo):
    from classes.candlestick import Candlestick
    import requests
    import time

    periodo_em_segundos = periodo * 60
    tempo_decorrido = 0
    tempo_espera = 5

    candlestick = Candlestick()
    valor_recente_candle = None

    while tempo_decorrido <= periodo_em_segundos:
        resposta_api = requests.get('https://poloniex.com/public?command=returnTicker')

        if resposta_api.status_code != 200:
            return 'Erro ao realizar chamada da API Poloniex.', 400

        dados_retorno_api = resposta_api.json()
        if not dados_retorno_api.get(moeda):
            return 'Moeda não encontrada nos dados retornados da API Poloniex.', 400

        valor_recente_candle = float(dados_retorno_api[moeda].get('last'))

        if not tempo_decorrido:
            candlestick.inicializa_candle(valor_recente_candle)

        candlestick.atualiza_valor_minimo_maximo(valor_recente_candle)

        time.sleep(tempo_espera)
        tempo_decorrido += tempo_espera

    candlestick.realiza_fechamento_candle(valor_recente_candle)

    return candlestick.__dict__, 200


aplicacao.config["DEBUG"] = True
aplicacao.run()
