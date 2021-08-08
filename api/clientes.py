import fastapi
from fastapi import Depends
from modelos.validar import ValidarAtualizar, ValidarCriar, ValidarRemover, ValidarVisualizar
from servicos import cliente

router = fastapi.APIRouter()


@router.post('/clientes/criar', tags=['criar'])
async def post(loc: ValidarCriar = Depends()):
    dados = await cliente.criar_cliente(loc.nome, loc.email)
    return dados


@router.put('/clientes/atualizar', tags=['atualizar'])
async def put(loc: ValidarAtualizar = Depends()):
    dados = await cliente.atualizar_cliente(loc.nome, loc.email)
    return dados


@router.get('/clientes/visualizar', tags=['visualizar'])
async def get(loc: ValidarVisualizar = Depends()):
    dados = await cliente.visualizar_cliente(loc.email)
    return dados


@router.delete('/clientes/remover', tags=['remover'])
async def delete(loc: ValidarRemover = Depends()):
    dados = await cliente.remover_cliente(loc.nome, loc.email)
    return dados
