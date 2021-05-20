from mysql.connector import connect, Error
from decouple import config


def executa_query(sql, parametros):
    try:
        with connect(
                host=config('HOST'),
                user=config('USER'),
                password=config('PASSWORD'),
                database=config('DATABASE')
        ) as conexao:

            with conexao.cursor() as cursor:
                cursor.executemany(sql, parametros)
                conexao.commit()

    except Error as e:
        print(f'Erro ao conectar no Banco de Dados - {e}')
