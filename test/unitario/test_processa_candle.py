import unittest
from mockito import when, args


class TestProcessaCandle(unittest.TestCase):

    # Dificuldade: Realizar mock do request #
    def test_processamento_candle(self):
        from server.funcoes.processa_candle import processamento_candle
        from server.classes.candlestick import Candlestick
        from server.bd import candlestick_crud

        when(Candlestick).inicializa_candle(*args).thenReturn()
        when(Candlestick).atualiza_valor_minimo_maximo(*args).thenReturn()
        when(Candlestick).atualiza_valor_fechamento_candle(*args).thenReturn()
        when(candlestick_crud).insere_candlestick(*args).thenReturn()

        processamento_candle(10, ['BTC_XMR'])
