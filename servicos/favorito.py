from servicos import bd
import requests


async def favoritos_cliente_delete(id_cliente: str, id_produto: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'_id': id_cliente}
    banco_dados.visualizar_cliente()
    
    if not banco_dados.cliente:
        msg = {
            "error_message": f"Não existe o cliente {id_cliente}",
            "code": "erro"
        }
        return msg

    if id_produto in banco_dados.cliente['favoritos']:
        banco_dados.cliente['favoritos'].remove(id_produto)
        banco_dados.novovalor = {
            '$set': {'favoritos': banco_dados.cliente['favoritos']}}
        banco_dados.atualizar_cliente()
        msg = {
            "message": f"Produto {id_produto} excluído",
            "code": "sucesso"
        }
    else:
        msg = {
            "error_message": f"Produto {id_produto} inexistente",
            "code": "erro"
        }

    return msg


async def favoritos_cliente_post(id_cliente: str, id_produto: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'_id': id_cliente}
    banco_dados.visualizar_cliente()
    
    produto = requests.get(
                f'http://challenge-api.luizalabs.com/api/product/{id_produto}/').json()
    
    if 'id' not in produto:
        msg = {
            "error_message": f"Não existe o produto {id_produto}",
            "code": "erro"
        }
        return msg


    if not banco_dados.cliente:
        msg = {
            "error_message": f"Não existe o cliente {id_cliente}",
            "code": "erro"
        }
        return msg

    if id_produto in banco_dados.cliente['favoritos']:
        msg = {
            "error_message": f"Produto {id_produto} já inserido",
            "code": "erro"
        }
    else:
        banco_dados.cliente['favoritos'].append(id_produto)
        banco_dados.novovalor = {
            '$set': {'favoritos': banco_dados.cliente['favoritos']}}
        banco_dados.atualizar_cliente()
        msg = {
            "message": f"Produto {id_produto} incluído com sucesso",
            "code": "sucesso"
        }

    return msg


async def favoritos_cliente_get(id_cliente: str, id_produto: str) -> dict:
    banco_dados = bd.MongoDB()
    banco_dados.filtrar = {'_id': id_cliente}
    banco_dados.visualizar_cliente()
    if not banco_dados.cliente:
        msg = {
            "error_message": f"Não existe o cliente {id_cliente}",
            "code": "erro"
        }
        return msg

    if id_produto in banco_dados.cliente['favoritos']:
        banco_dados.cliente['favoritos'] = [id_produto]
    elif id_produto is not None:
        msg = {
            "error_message": f"Não existe o produto {id_produto} para o cliente {id_cliente}",
            "code": "erro"
        }
        return msg

    msg = {}
    if banco_dados.cliente is not None:
        favoritos = []
        for id_produto in banco_dados.cliente['favoritos']:
            produto = requests.get(
                f'http://challenge-api.luizalabs.com/api/product/{id_produto}/').json()
            
            if 'id' not in produto:
                await favoritos_cliente_delete(id_cliente, id_produto)
                continue

            if 'reviewScore' in produto:
                favoritos.append({'id': produto['id'], 'title': produto['title'], 'image': produto['image'],
                                 'price': produto['price'], 'reviewScore': produto['reviewScore']})
            else:
                favoritos.append({'id': produto['id'], 'title': produto['title'],
                                 'image': produto['image'], 'price': produto['price']})
        
        msg = {
            "id_cliente": str(banco_dados.cliente['_id']),
            "favoritos": favoritos,
            "code": "sucesso"
        }

    return msg
