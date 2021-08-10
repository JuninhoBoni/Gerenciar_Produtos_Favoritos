import fastapi
from fastapi import Depends, HTTPException
from modelos.validar import ValidarFavoritos, ValidarFavoritosGet
from servicos import favorito

router = fastapi.APIRouter()


@router.post('/clientes/favoritos/', tags=['clientes/favoritos'])
async def favoritos(loc: ValidarFavoritos = Depends()):
    dados = await favorito.favoritos_cliente_post(loc.id_cliente, loc.id_produto)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.delete('/clientes/{id_cliente}/favoritos/{id_produto}', tags=['clientes/favoritos'])
async def favoritos(loc: ValidarFavoritos = Depends()):
    dados = await favorito.favoritos_cliente_delete(loc.id_cliente, loc.id_produto)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.get('/clientes/{id_cliente}/favoritos/', tags=['clientes/favoritos'])
async def favoritos(loc: ValidarFavoritosGet = Depends()):
    dados = await favorito.favoritos_cliente_get(loc.id_cliente, loc.id_produto)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados
