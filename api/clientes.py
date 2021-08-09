import fastapi
from fastapi import Depends
from modelos.validar import ValidarAtualizar, ValidarChave, ValidarCriar, ValidarFavoritos, ValidarRemover, ValidarVisualizar
from servicos import cliente

router = fastapi.APIRouter()


@router.post('/clientes/favoritos', tags=['favoritos'])
async def post(loc: ValidarFavoritos = Depends()):
    dados = await cliente.favoritos_cliente(loc.id_cliente, loc.id_produto)
    return dados


@router.post('/clientes/ativar', tags=['ativar'])
async def post(loc: ValidarChave = Depends()):
    dados = await cliente.ativar_cliente(loc.chave)
    return dados


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
    dados = await cliente.remover_cliente(loc.email)
    return dados
