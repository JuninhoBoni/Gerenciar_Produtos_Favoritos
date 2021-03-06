<h1 align="center"> 
	Gerenciador de Produtos Favoritos de Cliente
</h1>

<p align="center">
 <a href="#sobre-o-projeto">Sobre</a> •
 <a href="#funcionalidades">Funcionalidades</a> •
 <a href="#configurações">Configurações</a> • 
 <a href="#como-executar-o-projeto">Como executar</a> • 
 <a href="#testes">Testes</a> • 
 <a href="#tecnologias">Tecnologias</a>
</p>

---

https://favoritos-clientes.herokuapp.com/docs/

---

## Sobre o projeto

- API REST desenvolvida com framework FastAPI para gerenciar os produtos favoritos dos clientes.
- Possui autenticação OAuth2 com Password (e hashing), Bearer com JWT tokens
- Documentação da autenticação está disponível:
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- A documentação da lista de produtos consumida está disponível:
https://gist.github.com/Bgouveia/9e043a3eba439489a35e70d1b5ea08ec 
- Acesse o link abaixo para acessar a documentação da API:
https://favoritos-clientes.herokuapp.com/docs/
---

## Funcionalidades

- [x] Criar, atualizar, visualizar e remover Clientes
  - Para gerenciamento do cliente, o projeto usa o e-mail como chave

- [x] Lista de produtos favoritos
  - Para gerenciamento dos produtos do cliente, o projeto usa o id do cliente como chave

---

## Configurações

- No arquivo dependencies.py está disponível as informações de autenticação.
- Foi criado o dicionário users_db com as informações do usuário para login.
- Para testes, a autenticação deste projeto está com os dados abaixo:
- username: teste
- password: secret
- Para acessar a documentação da API, acessar:
  127.0.0.1:8000/docs
- SECRET_KEY e MONGO_PASS são variáveis de ambiente.

---

## Como executar o projeto

Requisitos minimos
- [x] Python 3.9

```bash
# Montar ambiente virtual
$ python -m venv dist

# Acessar o ambiente virtual
$ ./dist/Scripts/activate

# Instalar as bibliotecas necessárias para este projeto, executando o comando abaixo.
$ pip install -r requirements.txt

# O comando abaixo executa o programa. 
$ ./main.py

```


## Testes

```bash
# Montar ambiente virtual
$ python -m venv dist

# Acessar o ambiente virtual
$ ./dist/Scripts/activate

# Instalar as bibliotecas necessárias para este projeto, executando o comando abaixo.
$ pip install -r requirements.txt

# Para testar a API, utilize o comando abaixo. 
$ pytest -rP

```

---

## Tecnologias

- Linguagem: python3.9
- Framework: FastAPI
- DB de Dados: MongoDB
