def processamento_candle(periodo_em_segundos, moedas):
    from bd.candlestick import insere_candlestick
    from classes.candlestick import Candlestick
    from flask import abort
    import requests
    import time

    tempo_decorrido = 0
    tempo_espera = 10

    objeto_moedas = {}
    for moeda in moedas:
        objeto_moedas[moeda] = Candlestick()

    while tempo_decorrido <= periodo_em_segundos:
        resposta_api = requests.get('https://poloniex.com/public?command=returnTicker')

        if resposta_api.status_code != 200:
            abort(400, description='Erro ao realizar chamada da API Poloniex.')

        dados_retorno_api = resposta_api.json()

        for moeda, candle in objeto_moedas.items():
            if not dados_retorno_api.get(moeda):
                abort(400, description=f'Moeda {moeda} não encontrada nos dados retornados da API Poloniex.')

            valor_recente_candle = float(dados_retorno_api[moeda].get('last'))

            if not tempo_decorrido:
                candle.inicializa_candle(valor_recente_candle)

            candle.atualiza_valor_minimo_maximo(valor_recente_candle)
            candle.atualiza_valor_fechamento_candle(valor_recente_candle)

        time.sleep(tempo_espera)
        tempo_decorrido += tempo_espera

    insere_candlestick(objeto_moedas)
