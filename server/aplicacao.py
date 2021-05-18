from flask import Flask

aplicacao = Flask(__name__)


@aplicacao.route('/monitoramento/<int:periodo>', methods=['GET'])
def monitoramento(periodo):
    from classes.candlestick import Candlestick
    import requests
    import time

    """
        O candle ele é formado com base em 4 valores:
        Abertura - É o valor quando no momento de montagem do candle
        Mínima - É o valor mínimo que aquela moeda atingiu em um determinado período
        Máxima - É o valor máximo que aquela moeda atingiu em um determinado período
        Fechamento - É o último valor de todos os ticks recebidos daquele período
        Ou seja, se eu estou em um candle de 5m na qual ele está sendo iniciado as 14:00, 
        meu valor de abertura será aquele primeiro candle, meu valor de fechamento será o último tick, 14:05, 
        e os de máxima e mínima, são inicialmente carregados com os de abertura, sofrendo alterações nos valores 
        de alta se o último tick for maior que o de máxima atual e nos valores de baixa se o último tick for 
        menor que o de mínima atual.
    """

    periodo_em_segundos = periodo * 60
    tempo_decorrido = 0
    tempo_espera = 5

    candlestick = Candlestick()
    valor_recente_candle = None

    while tempo_decorrido <= periodo_em_segundos:
        resposta_api = requests.get('https://poloniex.com/public?command=returnTicker')

        if resposta_api.status_code != 200:
            raise ValueError('Erro ao realizar chamada da API Poloniex.')

        # Todo: Adicionar monitoramento para demais moedas #
        valor_recente_candle = float(resposta_api.json()['BTC_XMR'].get('last'))

        if not tempo_decorrido:
            candlestick.inicializa_candle(valor_recente_candle)

        candlestick.atualiza_valor_minimo_maximo(valor_recente_candle)

        time.sleep(tempo_espera)
        tempo_decorrido += tempo_espera

    candlestick.realiza_fechamento_candle(valor_recente_candle)

    return candlestick.__dict__, 200


aplicacao.config["DEBUG"] = True
aplicacao.run()
