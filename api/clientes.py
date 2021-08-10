import fastapi
from fastapi import Depends
from modelos.validar import ValidarAtualizar, ValidarFavoritos, ValidarCriar, ValidarRemover, ValidarVisualizar
from servicos import cliente

router = fastapi.APIRouter()

@router.patch('/clientes/favoritos/alterar', tags=['favoritos/alterar'])
async def favoritos(loc: ValidarFavoritos = Depends()):
    dados = await cliente.favoritos_cliente(loc.id_cliente, loc.id_produto)
    return dados

@router.post('/clientes/criar', tags=['criar'])
async def criar(loc: ValidarCriar = Depends()):
    dados = await cliente.criar_cliente(loc.nome, loc.email)
    return dados


@router.put('/clientes/atualizar', tags=['atualizar'])
async def atualizar(loc: ValidarAtualizar = Depends()):
    dados = await cliente.atualizar_cliente(loc.nome, loc.email)
    return dados


@router.get('/clientes/visualizar', tags=['visualizar'])
async def visualizar(loc: ValidarVisualizar = Depends()):
    dados = await cliente.visualizar_cliente(loc.email)
    return dados


@router.delete('/clientes/remover', tags=['remover'])
async def remover(loc: ValidarRemover = Depends()):
    dados = await cliente.remover_cliente(loc.email)
    return dados
