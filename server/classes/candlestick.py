class Candlestick:
    def __init__(self):
        self.abertura = None
        self.maximo = None
        self.minimo = None
        self.fechamento = None

    def inicializa_candle(self, valor_inicial_candle):
        self.minimo = valor_inicial_candle
        self.maximo = valor_inicial_candle
        self.abertura = valor_inicial_candle

    def atualiza_valor_minimo_maximo(self, novo_valor_minimo_maximo):
        if novo_valor_minimo_maximo < self.minimo:
            self.minimo = novo_valor_minimo_maximo
        elif novo_valor_minimo_maximo > self.maximo:
            self.maximo = novo_valor_minimo_maximo

    def realiza_fechamento_candle(self, valor_fechamento):
        self.fechamento = valor_fechamento
