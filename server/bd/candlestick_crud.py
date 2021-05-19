def insere_candlestick(candlesticks):
    from bd.conexao import executa_query

    sql = """
            insert into criptomoedas.tb_candlestick
            (moeda, open, low, high, close)
            values
            (%s, %s, %s, %s, %s);
        """

    parametros = []
    for moeda, candle in candlesticks.items():
        abertura, minimo, maximo, fechamento = candle.__dict__.values()
        parametros.append((moeda, abertura, minimo, maximo, fechamento))

    executa_query(sql, parametros)
