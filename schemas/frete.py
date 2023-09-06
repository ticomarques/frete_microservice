from pydantic import BaseModel
from typing import Optional, List
from model.frete import Frete



class FreteSchema(BaseModel):
    """ Define como um novo Frete a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "Sedex"
    valor: float = 12.50


class FreteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do frete.
    """
    nome: str = "Sedex"


class ListagemFretesSchema(BaseModel):
    """ Define como uma listagem de fretes será retornada.
    """
    fretes:List[FreteSchema]


def apresenta_produtos(fretes: List[Frete]):
    """ Retorna uma representação do frete seguindo o schema definido em
        FreteViewSchema.
    """
    result = []
    for frete in fretes:
        result.append({
            "id": frete.id,
            "nome": frete.nome,
            "valor": frete.valor,
        })

    return {"fretes": result}


class FreteViewSchema(BaseModel):
    """ Define como uma frete será retornada: frete.
    """
    id: int = 1
    nome: str = "Banana Prata"
    valor: float = 12.50



class FreteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_produto(frete: Frete):
    """ Retorna uma representação do frete seguindo o schema definido em
        FreteViewSchema.
    """
    return {
        "id": frete.id,
        "nome": frete.nome,
        "valor": frete.valor
    }
