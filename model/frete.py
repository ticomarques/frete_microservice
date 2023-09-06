from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Frete(Base):
    __tablename__ = 'frete'

    id = Column("pk_frete", Integer, primary_key=True)
    nome = Column(String(140))
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, valor:float, data_insercao:Union[DateTime, None] = None):
        """
        Cria um frete

        Arguments:
            nome: nome do produto para entrar no frete.
            valor: valor do frete.
            data_insercao: data de quando o frete foi inserida no sistema

            exemplo de corpo de requisição (JSON):
            {
                nome: "Sedex",
                valor: 10.00
            }

        """
        self.nome = nome
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

