from services import database as bd


async def create_client(name: str, email: str) -> dict:
    data_base = bd.MongoDB()

    data_return_client = {'name': name, 'email': email, 'favorites': []}
    data_base.dictionary = data_return_client.copy()
    data_base.filter = {'email': email}
    data_base.create_client()

    msg = {
        "id_client": data_base.id_client,
        "code": "success"
    }

    if data_base.id_client == '':
        msg = {
            "error_message": f"Email {email} already registered",
            "code": "error"
        }
    
    return msg


async def update_client(name: str, email: str) -> dict:
    data_base = bd.MongoDB()
    data_base.filter = {'email': email}
    data_base.new_value = {'$set': {'name': name}}
    data_base.update_client()
    msg = {
        "message": f"Email {email} already registered",
        "code": "success"
    }

    if not (data_base.status['updatedExisting']):
        msg = {
            "error_message": f"Email {email} not found",
            "code": "error"
        }

    return msg


async def view_client(email: str) -> dict:
    data_base = bd.MongoDB()
    data_base.filter = {'email': email, }
    data_base.view_client()

    if not data_base.client:
        msg = {
            "error_message": f"Email {email} not found",
            "code": "error"
        }
    else:
        msg = {
            "id_client": str(data_base.client['_id']),
            "name": data_base.client['name'],
            "email": data_base.client['email'],
            "code": "success",
        }

    return msg


async def remove_client(email: str) -> dict:
    data_base = bd.MongoDB()
    data_base.filter = {'email': email}
    data_base.remove_client()

    if data_base.status['n'] == 0:
        msg = {
            "error_message": f"Email {email} not found",
            "code": "error"
        }
    else:
        msg = {
            "message": f"Email {email} successfully removed",
            "code": "success"
        }

    return msg
