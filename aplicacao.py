from flask import Flask

aplicacao = Flask(__name__)


@aplicacao.route('/monitoramento/<int:tempo_espera>', methods=['GET'])
def monitoramento(tempo_espera):
    import requests
    import time

    while True:
        resposta_api = requests.get('https://poloniex.com/public?command=returnTicker')

        if resposta_api.status_code != 200:
            raise ValueError('Erro ao realizar chamda da API Poloniex.')

        time.sleep(tempo_espera)

    return "<h1>Monitoramento</h1>"


aplicacao.config["DEBUG"] = True
aplicacao.run()
