from services.validate import ValidateFavorites, ValidateFavoritesGet
from dependencies import get_current_user
from services import favorite

from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/clients",
                   tags=['clients/favorites'],
                   dependencies=[Depends(get_current_user)],
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
