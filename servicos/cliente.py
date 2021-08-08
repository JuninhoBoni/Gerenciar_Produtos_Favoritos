from servicos import bd
from modelos import emails
import uuid

async def criar_cliente(nome: str, email: str) -> dict:
    banco_dados = bd.PostgreSQL()
    chave = str(uuid.uuid4())
    dados_cliente = {
                    'nome' : nome,
                    'email' : email,
                    'status' : 'P',
                    'chave' : chave
                    }
    banco_dados.dados_cliente = dados_cliente
    
    conectar = banco_dados.conectar()
    retorno = "sucesso"
    if conectar:
        retorno = conectar
        dados_cliente = {}
        
    retorno_criar_cliente = banco_dados.criar_cliente()
    if retorno_criar_cliente:
        retorno = retorno_criar_cliente
        dados_cliente = {}
    
    if retorno == 'sucesso':
        enviar_email_ativacao = emails.Emails()
        enviar_email_ativacao.chave = chave
        enviar_email_ativacao.enviar_email_ativacao()

    dados = [{"retorno" : retorno},
                dados_cliente]

    return dados


async def atualizar_cliente(nome: str, email: str) -> dict:
    banco_dados = bd.PostgreSQL()
    dados_cliente = {
                    'nome' : nome,
                    'email' : email,
                    'status' : 'A',
                    }
    banco_dados.dados_cliente = dados_cliente

    conectar = banco_dados.conectar()
    retorno = "sucesso"
    if conectar:
        retorno = conectar
        dados_cliente = {}

    banco_dados.atualizar_cliente()
    
    if banco_dados.linhas == 0:
        # AO COMPLETAR O DESENVOLVIMENTO DO METODO visualizar_cliente 
        # REALIZAR CONSULTA PARA IDENTIFICAR SE O E-MAIL EXISTE
        retorno = {"status" : "E-mail não validado"}
        dados_cliente = {}
    
    dados = [{"retorno" : retorno},
                dados_cliente]
    return dados


async def visualizar_cliente(email: str) -> dict:
    banco_dados = bd.PostgreSQL()
    conectar = banco_dados.conectar()
    if conectar:
        retorno = conectar
        dados_cliente = {}
    else:
        retorno = "sucesso"
        banco_dados.colunas = ['nome', 'email', 'status', 'chave']
        banco_dados.valores = [email]
        retorno_visualizar_clientes = banco_dados.visualizar_cliente()
        dados_cliente = []
        for retorno_visualizar_cliente in retorno_visualizar_clientes:
            dados_cliente.append(retorno_visualizar_cliente)
        if not len(retorno_visualizar_clientes):
            retorno = 'sem dados'
    dados = [{"retorno" : retorno},
                dados_cliente]
    return dados


async def remover_cliente(nome: str, email: str) -> dict:
    dados = {"nome": nome,
             "email": email,
             }
    return dados
