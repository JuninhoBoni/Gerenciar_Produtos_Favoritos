from servicos import bd
import requests


async def criar_cliente(nome: str, email: str) -> dict:
    banco_dados = bd.MongoDB()

    dados_cliente = {'nome': nome, 'email': email, 'favoritos': []}
    banco_dados.dicionario = dados_cliente.copy()
    banco_dados.filtrar = {'email': email}
    banco_dados.criar_cliente()

    msg = {
        "id_cliente": banco_dados.id_cliente,
        "code": "sucesso"
    }

    if banco_dados.id_cliente == '':
        msg = {
            "error_message": f"Email {email} já cadastrado",
            "code": "erro"
        }

    return msg


async def atualizar_cliente(nome: str, email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email}
    banco_dados.novovalor = {'$set': {'nome': nome}}
    banco_dados.atualizar_cliente()
    msg = {
            "message": f"Email {email} cadastrado",
            "code": "sucesso"
        }

    if not (banco_dados.status['updatedExisting']):
        msg = {
            "error_message": f"Email {email} não cadastrado",
            "code": "erro"
        }

    return msg


async def visualizar_cliente(email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email, }
    banco_dados.visualizar_cliente()

    if not banco_dados.cliente:
        msg = {
            "error_message": f"Email {email} não encontrado",
            "code": "erro"
        }
    else:
        msg = {
            "id_cliente": str(banco_dados.cliente['_id']),
            "nome": banco_dados.cliente['nome'],
            "email": banco_dados.cliente['email'],
            "code": "sucesso",
        }

    return msg


async def remover_cliente(email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email}
    banco_dados.remover_cliente()

    if banco_dados.status['n'] == 0:
        msg = {
            "error_message": f"Email {email} não encontrado",
            "code": "erro"
        }
    else:
        msg = {
            "message": f"Email {email} removido com sucesso",
            "code": "erro"
        }

    return msg
