from main import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from modelos.validar import ValidarAtualizar, ValidarCriar, ValidarRemover, ValidarVisualizar, ValidarFavoritos, ValidarFavoritosGet
from servicos import cliente, favorito


router = APIRouter(prefix="/clientes",
                   dependencies=[Depends(get_current_user)],
                   responses={404: {"description": "Not found"}},
                   )


@router.post('/favoritos/', tags=['clientes/favoritos'])
async def favoritos(loc: ValidarFavoritos = Depends()):
    dados = await favorito.favoritos_cliente_post(loc.id_cliente, loc.id_produto)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.delete('/{id_cliente}/favoritos/{id_produto}', tags=['clientes/favoritos'])
async def favoritos(loc: ValidarFavoritos = Depends()):
    dados = await favorito.favoritos_cliente_delete(loc.id_cliente, loc.id_produto)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.get('/{id_cliente}/favoritos/', tags=['clientes/favoritos'])
async def favoritos(loc: ValidarFavoritosGet = Depends()):
    dados = await favorito.favoritos_cliente_get(loc.id_cliente, loc.id_produto)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.post('/', tags=['clientes'])
async def criar(loc: ValidarCriar = Depends()):
    dados = await cliente.criar_cliente(loc.nome, loc.email)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.put('/{nome}/email/{email}', tags=['clientes'])
async def atualizar(loc: ValidarAtualizar = Depends()):
    dados = await cliente.atualizar_cliente(loc.nome, loc.email)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.get('/{email}', tags=['clientes'])
async def visualizar(loc: ValidarVisualizar = Depends()):
    dados = await cliente.visualizar_cliente(loc.email)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.delete('/{email}', tags=['clientes'])
async def remover(loc: ValidarRemover = Depends()):
    dados = await cliente.remover_cliente(loc.email)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados
