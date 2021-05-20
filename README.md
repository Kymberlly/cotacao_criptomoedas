# Cotação de Criptomoedas

API desenvolvida em Python para realizar o processamento das cotações de uma determinada moeda, agregá-las em candlesticks e armazenar os candles em um banco de dados Mysql.

_____________________________________________________________

### Funcionamento:

Atualmente a API possui apenas uma endpoint **/monitoramento** que aceita os seguintes parâmetros:

**periodo (string)** - Tempo de processamento da cotação

**moeda (Método GET: string; Método POST: Lista de strings)** - Moeda na qual deseja realizar o monitoramento



### Métodos HTTP:

**GET:**

Através de parâmetros informados na URL: http://localhost:5000/monitoramento?periodo=1&moeda=BTC_XMR


**POST:** 

Através do envio de um objeto json para a URL: http://localhost:5000/monitoramento

```
{
    "moeda": ["BTC_XMR", "BTC_KNC", "BTC_ZEC"],
    "periodo": 1
}
```


Ao final do processamento os candles são salvos no banco de dados e a seguinte mensagem é retornada:
```
Processamento da cotação finalizado.
```

___________________________________________

## Pré-Requisitos:

Antes de começar, você vai precisar realizar as seguintes instalações:

* [Python 3.8](https://www.python.org/downloads/release/python-380/)
* [Mysql](https://www.mysql.com/downloads/)

Após realizada as instalações, clone o projeto:
```
git clone https://github.com/Kymberlly/criptomooedas.git
```

Acesse a pasta do projeto no terminal/cmd:
```
cd criptomooedas
```

Crie o ambiente virtual para realizar a instalação das dependências do nosso projeto:

*No caso abaixo estamos especificando que o ambiente virtual seja criado com a versão do Python 3.8, caso haja mais de uma versão instalada no computador.*
```
virtualenv venv -p=python3.8
```

Ative o ambiente virtual:
```
# No Linux:
. venv\bin\activate

# Windows
venv\Scripts\activate.bat
```

Instale as dependências do projeto:
```
pip install -r requirements.txt
pip install -r requirements-tests.txt
```

Após a realização dos passos acima, acesse a pasta server:
```
cd server
```

Crie o arquivo .env para armazenar nossas variáveis de ambiente, nele deverá conter as variáveis que estão presentes no arquivo .env.sample, porém preenchidas.

**Neste passo é importante que você já tenha realizado a instalação do Mysql e criado um banco de dados.**

### Estrutura do banco de dados para armazenamento dos Candles:

Atualmente o código está inserindo as informações no schema **criptomoedas** tabela **tb_candlestick**. Então será necessário criar em seu banco de dados um schema denominado criptomoedas e uma tabela tb_candlestick. Caso você precise que os dados sejam armazenados em outro schema/tabela basta modificar o código no arquivo bd/candlestick_crud.py

A tabela deverá conter as seguintes colunas:

* moeda
* periodicidade
* datetime
* open
* low
* high
* close


## Executando o projeto

Para executar o projeto é necessário ativar o ambiente virtual, estar dentro da pasta server e digitar no terminal o seguinte comando:
```
python aplicacao.py
```

O servidor iniciará na porta:5000 - acesse <http://localhost:5000/>
