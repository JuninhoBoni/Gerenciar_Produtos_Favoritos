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
    dados = {"nome": nome,
             "email": email,
             }
    return dados


async def visualizar_cliente(nome: str, email: str) -> dict:
    dados = {"nome": nome,
             "email": email,
             }
    return dados


async def remover_cliente(nome: str, email: str) -> dict:
    dados = {"nome": nome,
             "email": email,
             }
    return dados
