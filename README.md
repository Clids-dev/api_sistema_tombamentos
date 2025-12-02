
# Sistema de Tombamento – API e Modelo de Dados

Este documento descreve o projeto **Sistema de Tombamento**, desenvolvido em FastAPI, incluindo **modelo de dados**, **endpoints CRUD**, **endpoints específicos**, **requisitos**, **instalação**, **execução** e **fluxo geral do sistema**.

---

# 1. Requisitos para o projeto

## 1. Criar e ativar o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate     # Linux/Mac
# ou
venv\Scripts\activate        # Windows
```

## 2. Instalar as dependências:

```bash
pip install -r requirements.txt
```

## 3. Executar o projeto:

1. Certifique-se de que o ambiente virtual está ativo.
2. Execute o servidor de desenvolvimento:

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

Documentação automática:

```
/docs
/redoc
```

---

# 2. Modelo de Dados (Tabelas)

## 2.1 Bem

* id
* nome
* codigo_tombamento (único)
* valor
* status
* ativo

## 2.2 Categoria

* id
* nome
* ativo

## 2.3 Setor

* id
* nome
* responsavel
* ativo

## 2.4 Responsável

* id
* nome
* cargo
* ativo

## 2.5 Movimentação

* id
* bem_id
* setor_origem_id
* setor_destino_id
* data
* ativo

---

# 3. Endpoints CRUD

## 3.1 Bens

Base: `/bens`

### POST /bens

```json
{
  "nome": "Notebook Dell 15",
  "codigo_tombamento": "TMB-2025-0001",
  "valor": 5200,
  "status": "em_uso"
}
```

### GET /bens

QueryParams opcionais: nome, codigo_tombamento, status, ativo, valor_min, valor_max.

### GET /bens/{id}

### PUT /bens/{id}

### DELETE /bens/{id}

Soft delete (ativo = false)

---

## 3.2 Categorias

Base: `/categorias`

### POST /categorias

```json
{ "nome": "Informática" }
```

### GET /categorias

### GET /categorias/{id}

### PUT /categorias/{id}

### DELETE /categorias/{id}

---

## 3.3 Setores

Base: `/setores`

### POST /setores

```json
{ "nome": "TI", "responsavel": "Coord. de TI" }
```

### GET /setores

### GET /setores/{id}

### PUT /setores/{id}

### DELETE /setores/{id}

---

## 3.4 Responsáveis

Base: `/responsaveis`

### POST /responsaveis

### GET /responsaveis

### GET /responsaveis/{id}

### PUT /responsaveis/{id}

### DELETE /responsaveis/{id}

---

## 3.5 Movimentações

Base: `/movimentacoes`

### POST /movimentacoes

```json
{
  "bem_id": 1,
  "setor_origem_id": 2,
  "setor_destino_id": 5,
  "data": "2025-10-20T14:30:00Z"
}
```

### GET /movimentacoes

### GET /movimentacoes/{id}

### PUT /movimentacoes/{id}

### DELETE /movimentacoes/{id}

---

# 4. Endpoints Específicos

## 4.1 Buscar bem por código de tombamento

```
GET /bens/buscar?codigo_tombamento=XXXX
```

## 4.2 Histórico de movimentações

```
GET /bens/{id}/historico-movimentacoes
```

## 4.3 Listar bens por setor atual

```
GET /bens/por-setor?setor_id=5
```

## 4.4 Transferência rápida

```
POST /bens/{id}/transferir
```

## 4.5 Relatório: bens ativos por status

```
GET /relatorios/bens-ativos-por-status
```

---

# 5. Fluxo Geral do Sistema

## Cadastro + Movimentação

1. Criar bem
2. Registrar movimentação
3. Consultar setor atual

## Desativação

1. Desativar bem (DELETE ou endpoint específico)
2. Filtrar listagens com `ativo=true`


## Equipe

**José Euclides H Barros**

**Pedro Henrique do Santos**

**Guilherme Henrique M. G. Santana**

Desenvolvedores do projeto *Sistema de Tombamento*.


