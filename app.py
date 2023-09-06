from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Frete
from logger import logger
from schemas import *
from flask_cors import CORS

from schemas.frete import FreteDelSchema

info = Info(title="Frete", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
frete_tag = Tag(name="Frete", description="CRUD de Frete")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/frete', tags=[frete_tag],
          responses={"200": FreteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: FreteSchema):
    """Adiciona um frete 

    Retorna uma representação de frete.
    {
        "nome": "TIAGO10",
        "valor": 0.9
    }

    """
    frete = Frete(
        nome = request.json['nome'],
        valor = request.json['valor'])
    logger.debug(f"Adicionando produto de nome: '{frete.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando um frete
        session.add(frete)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado frete de nome: '{frete.nome}'")
        return apresenta_produto(frete), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "frete de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar frete '{frete.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar frete '{frete.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/frete', tags=[frete_tag],
         responses={"200": ListagemFretesSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todas os frete cadastradas

    Retorna uma representação da listagem de fretes.
    """
    logger.debug(f"Coletando fretes")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    fretes = session.query(Frete).all()

    if not fretes:
        # se não há fretes cadastrados
        return {"fretes": []}, 200
    else:
        logger.debug(f"%d fretes econtradas" % len(fretes))
        # retorna a representação de produto
        print(fretes)
        return apresenta_produtos(fretes), 200


@app.get('/frete', tags=[frete_tag],
         responses={"200": FreteViewSchema, "404": ErrorSchema})
def get_produto(query: FreteBuscaSchema):
    """Faz a busca por um frete a partir do id de um frete

    Retorna uma representação das frete e lances associados.
    """
    frete_id = query.nome
    logger.debug(f"Coletando dados sobre produto #{frete_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    frete = session.query(Frete).filter(Frete.nome == frete_id).first()

    if not frete:
        # se o frete não foi encontrado
        error_msg = "frete não encontrada na base :/"
        logger.warning(f"Erro ao buscar produto '{frete_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{frete.nome}'")
        # retorna a representação da frete
        return apresenta_produto(frete), 200


@app.delete('/frete', tags=[frete_tag],
            responses={"200": FreteDelSchema, "404": ErrorSchema})
def del_produto(query: FreteBuscaSchema):
    """Deleta um frete a partir do nome de frete

    Retorna uma mensagem de confirmação da remoção.
    """
    frete_nome = unquote(unquote(query.nome))
    logger.debug(f"Deletando dados sobre produto #{frete_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Frete).filter(Frete.nome == frete_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{frete_nome}")
        return {"message": "Produto removido", "id": frete_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{frete_nome}', {error_msg}")
        return {"message": error_msg}, 404

