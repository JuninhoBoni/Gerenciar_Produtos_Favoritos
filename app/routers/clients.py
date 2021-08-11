from services.validate import ValidateUpdate, ValidateCreate, ValidateRemove, ValidateView, ValidateFavorites, ValidateFavoritesGet
#from main import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from services import client, favorite


router = APIRouter(prefix="/clients",
                   #dependencies=[Depends(get_current_user)],
                   responses={404: {"description": "Not found"}},
                   )


@router.post('/favorites/', tags=['clients/favorites'])
async def favorites(loc: ValidateFavorites = Depends()):
    data_return = await favorite.favorites_client_post(loc.id_client, loc.id_product)
    if data_return['code'] == 'erro':
        raise HTTPException(status_code=404, detail=data_return)
    return data_return


@router.delete('/{id_client}/favorites/{id_product}', tags=['clients/favorites'])
async def favorites(loc: ValidateFavorites = Depends()):
    data_return = await favorite.favorites_client_delete(loc.id_client, loc.id_product)
    if data_return['code'] == 'erro':
        raise HTTPException(status_code=404, detail=data_return)
    return data_return


@router.get('/{id_client}/favorites/', tags=['clients/favorites'])
async def favorites(loc: ValidateFavoritesGet = Depends()):
    data_return = await favorite.favorites_client_get(loc.id_client, loc.id_product)
    if data_return['code'] == 'erro':
        raise HTTPException(status_code=404, detail=data_return)
    return data_return


@router.post('/', tags=['clients'])
async def create(loc: ValidateCreate = Depends()):
    data_return = await client.create_client(loc.name, loc.email)
    if data_return['code'] == 'erro':
        raise HTTPException(status_code=404, detail=data_return)
    return data_return


@router.put('/{name}/email/{email}', tags=['clients'])
async def update(loc: ValidateUpdate = Depends()):
    data_return = await client.update_client(loc.name, loc.email)
    if data_return['code'] == 'erro':
        raise HTTPException(status_code=404, detail=data_return)
    return data_return


@router.get('/{email}', tags=['clients'])
async def view(loc: ValidateView = Depends()):
    data_return = await client.view_client(loc.email)
    if data_return['code'] == 'erro':
        raise HTTPException(status_code=404, detail=data_return)
    return data_return


@router.delete('/{email}', tags=['clients'])
async def remove(loc: ValidateRemove = Depends()):
    data_return = await client.remove_client(loc.email)
    if data_return['code'] == 'erro':
        raise HTTPException(status_code=404, detail=data_return)
    return data_return
