# MVP 2 - FRETE MICROSERVICE (Backend) - Engenharia de Software PUC-Rio (2023.3)

Microsserviço para gerenciamento de cupom, um CRUD de cupom.

---


# Backend tecnologias

O backend deste projeto foi desenvolido em Python com SQL Alchemy. Todas as dependencias podem ser consultadas no arquivo requirements.



## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Como ativar um virtal env:
```
source env/bin/activate 
```

Como desativar um virtal env:
```
deactivate 
```

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 8001
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 8001 --reload
```

Abra o [http://localhost:8001/#/](http://localhost:8001/#/) no navegador para verificar o status da API em execução.

## Docker
