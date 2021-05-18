def insere_candlestick(moeda, candlestick):
    from bd.conexao import executa_query

    sql = """
            insert into criptomoedas.tb_candlestick
            (moeda, open, low, high, close)
            values
            (%s, %s, %s, %s, %s);
        """

    parametros = [(moeda, candlestick['abertura'], candlestick['minimo'],
                   candlestick['maximo'], candlestick['fechamento'])]
    executa_query(sql, parametros)
