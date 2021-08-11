from services import database as bd
import requests


async def favorites_client_delete(id_client: str, id_product: str) -> dict:
    data_base = bd.MongoDB()
    data_base.filter = {'_id': id_client}
    data_base.view_client()

    if not data_base.client:
        msg = {
            "error_message": f"The client {id_client} not found",
            "code": "error"
        }
        return msg

    if id_product in data_base.client['favorites']:
        data_base.client['favorites'].remove(id_product)
        data_base.new_value = {
            '$set': {'favorites': data_base.client['favorites']}}
        data_base.update_client()
        msg = {
            "message": f"The product {id_product} deleted",
            "code": "success"
        }
    else:
        msg = {
            "error_message": f"The product {id_product} does not exist",
            "code": "error"
        }

    return msg


async def favorites_client_post(id_client: str, id_product: str) -> dict:
    data_base = bd.MongoDB()
    data_base.filter = {'_id': id_client}
    data_base.view_client()

    product = requests.get(
        f'http://challenge-api.luizalabs.com/api/product/{id_product}/').json()

    if 'id' not in product:
        msg = {
            "error_message": f"The product {id_product} does not exist",
            "code": "error"
        }
        return msg

    if not data_base.client:
        msg = {
            "error_message": f"The client {id_client} does not exist",
            "code": "error"
        }
        return msg

    if id_product in data_base.client['favorites']:
        msg = {
            "error_message": f"The product {id_product} already inserted",
            "code": "error"
        }
    else:
        data_base.client['favorites'].append(id_product)
        data_base.new_value = {
            '$set': {'favorites': data_base.client['favorites']}}
        data_base.update_client()
        msg = {
            "message": f"The product {id_product} successfully added",
            "code": "success"
        }

    return msg


async def favorites_client_get(id_client: str, id_product: str) -> dict:
    data_base = bd.MongoDB()
    data_base.filter = {'_id': id_client}
    data_base.view_client()
    if not data_base.client:
        msg = {
            "error_message": f"The client {id_client} does not exist",
            "code": "error"
        }
        return msg

    if id_product in data_base.client['favorites']:
        data_base.client['favorites'] = [id_product]
    elif id_product is not None:
        msg = {
            "error_message": f"The product {id_product} does not exist for the client {id_client}",
            "code": "error"
        }
        return msg

    msg = {}
    if data_base.client is not None:
        favorites = []
        for id_product in data_base.client['favorites']:
            product = requests.get(
                f'http://challenge-api.luizalabs.com/api/product/{id_product}/').json()

            if 'id' not in product:
                await favorites_client_delete(id_client, id_product)
                continue

            if 'reviewScore' in product:
                favorites.append({'id': product['id'], 'title': product['title'], 'image': product['image'],
                                 'price': product['price'], 'reviewScore': product['reviewScore']})
            else:
                favorites.append({'id': product['id'], 'title': product['title'],
                                 'image': product['image'], 'price': product['price']})

        msg = {
            "id_client": str(data_base.client['_id']),
            "favorites": favorites,
            "code": "success"
        }

    return msg
