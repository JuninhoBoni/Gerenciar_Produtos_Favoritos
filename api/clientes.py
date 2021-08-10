import fastapi
from fastapi import Depends, HTTPException
from modelos.validar import ValidarAtualizar, ValidarCriar, ValidarRemover, ValidarVisualizar
from servicos import cliente

router = fastapi.APIRouter()


@router.post('/clientes', tags=['clientes'])
async def criar(loc: ValidarCriar = Depends()):
    dados = await cliente.criar_cliente(loc.nome, loc.email)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.put('/clientes/{nome}/email/{email}', tags=['clientes'])
async def atualizar(loc: ValidarAtualizar = Depends()):
    dados = await cliente.atualizar_cliente(loc.nome, loc.email)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.get('/clientes/{email}', tags=['clientes'])
async def visualizar(loc: ValidarVisualizar = Depends()):
    dados = await cliente.visualizar_cliente(loc.email)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados


@router.delete('/clientes/{email}', tags=['clientes'])
async def remover(loc: ValidarRemover = Depends()):
    dados = await cliente.remover_cliente(loc.email)
    if dados['code'] == 'erro':
        raise HTTPException(status_code=404, detail=dados)
    return dados
