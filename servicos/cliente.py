from servicos import bd
import requests


async def favoritos_cliente(id_cliente: str, id_produto: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'_id': id_cliente}
    banco_dados.visualizar_cliente()

    if id_produto in banco_dados.cliente['favoritos']:
        banco_dados.cliente['favoritos'].remove(id_produto)
    else:
        produto = requests.get(f'http://challenge-api.luizalabs.com/api/product/{id_produto}/')
        if produto.status_code == 200:
            banco_dados.cliente['favoritos'].append(id_produto)
        else:
            msg = {
                "error_message" : f"Produto {id_produto} inexistente",
                "code": "erro"
                }
            return msg

    banco_dados.novovalor = {'$set': {'favoritos': banco_dados.cliente['favoritos']}}
    banco_dados.atualizar_cliente()
    msg = mensagem(banco_dados.cliente)

    return msg


async def criar_cliente(nome: str, email: str) -> dict:
    banco_dados = bd.MongoDB()

    dados_cliente = {'nome': nome,
                     'email': email,
                     'favoritos': [],
                     }
    banco_dados.dicionario = dados_cliente.copy()
    banco_dados.filtrar = {'email': email}
    banco_dados.criar_cliente()
    msg = mensagem(banco_dados.cliente)

    if banco_dados.quantidade > 0:
        msg = {
            "error_message" : f"Email {email} já cadastrado",
            "code": "erro"
            }
    
    return msg


async def atualizar_cliente(nome: str, email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email}
    banco_dados.novovalor = {'$set': {'nome': nome}}
    banco_dados.atualizar_cliente()
    msg = mensagem(banco_dados.cliente)

    if not (banco_dados.status['updatedExisting']):
        msg = {
                "error_message" : f"Email {email} não cadastrado",
                "code": "erro"
            }

    return msg


async def visualizar_cliente(email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email, }
    banco_dados.visualizar_cliente()
    msg = mensagem(banco_dados.cliente)

    if not banco_dados.cliente:
        msg = {
                "error_message" : f"Email {email} não encontrado",
                "code": "erro"
            }

    return msg

async def remover_cliente(email: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'email': email, }
    banco_dados.remover_cliente()
    msg = mensagem(banco_dados.cliente)

    if banco_dados.status['n'] == 0:
        msg = {
                "error_message" : f"Email {email} não encontrado",
                "code": "erro"
            }
    else:
        msg = {
                "message" : f"Email {email} removido com sucesso",
                "code": "erro"
            }

    return msg

def mensagem(cliente):
    msg = None
    if cliente is not None:
        favoritos = []
        for id_produto in cliente['favoritos']:
            produto = requests.get(f'http://challenge-api.luizalabs.com/api/product/{id_produto}/').json()
            if 'reviewScore' in produto:
                favoritos.append({ 'id': produto['id'], 'title' : produto['title'], 'image' : produto['image'], 'price': produto['price'], 'reviewScore': produto['reviewScore']})
            else:
                favoritos.append({ 'id': produto['id'], 'title' : produto['title'], 'image' : produto['image'], 'price': produto['price']})
        msg = {
            "_id": str(cliente['_id']),
            "nome": cliente['nome'],
            "email": cliente['email'],
            "favoritos": favoritos,
            "code": "sucesso",
            }
        
    return msg