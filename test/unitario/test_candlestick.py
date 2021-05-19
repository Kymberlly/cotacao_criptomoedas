import unittest


class TestCandlestick(unittest.TestCase):
    def test_inicializa_candle(self):
        from server.classes.candlestick import Candlestick

        candle = Candlestick()
        candle.inicializa_candle(0.001)

    def test_atualiza_valor_minimo_maximo(self):
        from server.classes.candlestick import Candlestick

        candle = Candlestick()
        candle.atualiza_valor_minimo_maximo(0.001)

    def test_atualiza_valor_fechamento_candle(self):
        from server.classes.candlestick import Candlestick

        candle = Candlestick()
        candle.atualiza_valor_fechamento_candle(0.001)
