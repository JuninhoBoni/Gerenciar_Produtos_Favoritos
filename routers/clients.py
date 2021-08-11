from services.validate import ValidateUpdate, ValidateCreate, ValidateRemove, ValidateView
from dependencies import get_current_user
from services import client

from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/clients",
                   tags=['clients'],
                   dependencies=[Depends(get_current_user)],
                   responses={404: {"description": "Not found"}},
                   )


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
