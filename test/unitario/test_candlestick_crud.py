import unittest
from mockito import when, args


class TestCandlestickCrud(unittest.TestCase):
    def test_insere_candlestick(self):
        from server.bd.candlestick_crud import insere_candlestick
        from server.bd import conexao

        when(conexao).executa_query(*args).thenReturn()

        candle_moeda_finalizado = mock_candle_moeda_finalizado()
        insere_candlestick(candle_moeda_finalizado)


def mock_candle_moeda_finalizado():
    from server.classes.candlestick import Candlestick

    candle = Candlestick()
    return {'BTC_XMR': candle}
