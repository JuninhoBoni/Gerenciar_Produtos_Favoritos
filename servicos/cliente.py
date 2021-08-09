from servicos import bd
from modelos import emails
import uuid


async def ativar_cliente(chave: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'chave': chave,
                           'status': 'P'}
    banco_dados.novovalor = {"$set": {'status': 'A'}}
    banco_dados.atualizar_cliente()

    retorno = {"status": "E-mail ativo"}
    if not banco_dados.status['updatedExisting']:
        retorno = {"status": "Chave invalida"}

    dados = [{"retorno": retorno},
             {}]
    return dados


async def criar_cliente(nome: str, email: str) -> dict:
    banco_dados = bd.MongoDB()
    chave = str(uuid.uuid4())

    dados_cliente = {"nome": nome,
                     "email": email,
                     "status": "P",
                     "chave": chave,
                     "favoritos": [""],
                     }
    banco_dados.dicionario = dados_cliente.copy()
    banco_dados.filtrar = {'email': email}
    banco_dados.criar_cliente()

    if banco_dados.quantidade > 0:
        retorno = "email já está cadastrado"
        dados_cliente = {"nome": nome,
                         "email": email,
                         }
    else:
        retorno = "sucesso"
        enviar_email_ativacao = emails.Emails()
        enviar_email_ativacao.chave = chave
        enviar_email_ativacao.enviar_email_ativacao()

    dados = [{"retorno": retorno},
             dados_cliente]

    return dados


async def atualizar_cliente(nome: str, email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email,
                           'status': 'A'}
    banco_dados.novovalor = {"$set": {'nome': nome}}
    banco_dados.atualizar_cliente()

    if banco_dados.status['updatedExisting'] and banco_dados.status['nModified'] == 0:
        retorno = {"status": "Sem alteração de dados"}
        dados_cliente = {}
    elif banco_dados.status['updatedExisting'] and banco_dados.status['nModified'] == 1:
        retorno = {"status": "Sucesso"}
        dados_cliente = {}
    else:
        retorno = {"status": "E-mail não cadastrado"}
        dados_cliente = {}

    dados = [{"retorno": retorno},
             dados_cliente]

    return dados


async def visualizar_cliente(email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email, }
    banco_dados.visualizar_cliente()
    if banco_dados.cliente:
        retorno = 'sucesso'
        dados_cliente = {"nome": banco_dados.cliente['nome'],
                         "email": banco_dados.cliente['email'],
                         "status": banco_dados.cliente['status'],
                         "favoritos": banco_dados.cliente['favoritos'],
                         }
    else:
        retorno = 'email não encontrado'
        dados_cliente = {}

    dados = [{"retorno": retorno},
             dados_cliente]
    return dados


async def remover_cliente(email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email, }
    banco_dados.remover_cliente()

    dados_cliente = {"email": email}
    if banco_dados.status['n'] == 0:
        retorno = {"status": "E-mail não encontrado"}
    else:
        retorno = "sucesso"
    dados = [{"retorno": retorno},
             dados_cliente]
    return dados
