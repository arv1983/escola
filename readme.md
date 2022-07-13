# API ESCOLA

### RODAR APLICAÇÂO:

docker-compose build
docker-compose up -d --build

## Usuarios

#### Criar aluno:

**URL** : `http://0.0.0.0:5010/`

**Method** : `POST`

```json
{
  "name": "nome teste",
  "cpf": 15554870090,
  "email": "meu@email.com",
  "phone_number": "51985862273"
}
```

## Resposta sucesso

**Code** : `201 CREATED`

**Content example**

```json
{
  "id": 1,
  "name": "nome teste",
  "cpf": "155.548.700-90",
  "email": "meu@email.com",
  "phone": "(51) 98586-2273",
  "created_at": "13/07/2022 - 23:14"
}
```

## Erros

**Condição** : Estudante já tem cadastro

**Code** : `401`

**Content** :

```json
{
  "erro": "Estudante já cadastrado"
}
```

##

**Condition** : CPF Inválido

**Code** : `409 CONFLICT`

**Content** :

```json
{
  "erro": "CPF inválido"
}
```

##

**Condition** : EMAIL Inválido

**Code** : `409 CONFLICT`

**Content** :

```json
{
  "erro": "Email inválido."
}
```

##

#### Listar todos os usuários:

**URL** : `http://0.0.0.0:5010`

**Method** : `GET`

```json
[
  {
    "id": 1,
    "name": "nome teste",
    "cpf": "155.548.700-90",
    "email": "meu@email.com",
    "phone": "(51) 98586-2273",
    "created_at": "13/07/2022 - 23:14"
  }
]
```

##

#### Buscar usuário por ID

**URL** : `http://0.0.0.0:5010/id/1`

**Method** : `GET`

```json
{
  "id": 1,
  "name": "teste name",
  "cpf": "317.676.510-07",
  "email": "meui@email.com",
  "phone": "51985862273",
  "created_at": "13/07/2022 - 17:58"
}
```

##

#### Buscar usuário por nome

**URL** : `http://0.0.0.0:5010/student`

**Method** : `GET`

```json
{
  "name": "Nome Teste"
}
```

## Resposta sucesso

**Code** : `200`

```json
[
  {
    "id": 2,
    "name": "teste 22",
    "cpf": "015.554.870-09",
    "email": "meui@email.com",
    "phone": "51985862273",
    "created_at": "13/07/2022 - 17:59"
  }
]
```

##

### Editar usuário:

**URL** : `http://0.0.0.0:5010/cpf/01555487009`

**Method** : `PATCH`

```json
{
  "name": "nome teste editado",
  "cpf": "01555487009",
  "email": "meue@mail_editado.com",
  "phone_number": "51985862273"
}
```

#### Resposta sucesso

**Code** : `200 OK`

```json
{
  "id": 1,
  "name": "nome teste editado",
  "cpf": "015.554.870-09",
  "email": "meue@mail_editado.com",
  "phone": "(51) 98586-2273",
  "created_at": "13/07/2022 - 23:14"
}
```

#### Erro

**Condição** : Id não encontrado

**Code** : `404` no content

##

### Deletar usuário:

**URL** : `http://0.0.0.0:5010/id/1`

**Method** : `DELETE`

#### Resposta sucesso

**Code** : `200 OK`

#### Resposta Erro

**Condição** : Usuário não encontrado

**Code** : `404 NOT FOUND`

---
