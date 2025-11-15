# Sistema de Tombamento — Modelo de Dados e API

Documento padrão para projetos FBD (2025.2). Este guia descreve **modelo de dados**, **endpoints CRUD (onde o D = desativar)** e **endpoints específicos**. Os exemplos são em JSON. **Todos os QueryParams em requisições GET são opcionais.** Removidos paginação e ordenação para simplificar.

---

# Requisitos para o projeto:
1.Criar e ativar o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Linux/Mac
   # ou
   venv\Scripts\activate  # No Windows
   ```
2.  Instalar as dependecias:
   Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Executar o projeto:
1. Certifique-se de que o ambiente virtual está ativado
2. Execute o servidor de desenvolvimento:
   ```bash
   uvicorn main:app --reload
   ```



## 1) Texto padrão (para reutilização em outros projetos)
1. **Coluna `ativo`**: todo recurso possui um campo booleano `ativo` (default: `true`). Operações de “exclusão” apenas marcam `ativo = false`.
2. **CRUD**:
   - **POST** cria um registro ativo.
   - **GET** lista/detalha; filtros via QueryParams **opcionais**.
   - **PUT/PATCH** atualiza campos do registro.
   - **DELETE** = **desativar** (soft delete: `ativo = false`).
3. **Respostas**: retornar objeto salvo/atualizado ou mensagem de confirmação.
4. **Erros comuns**: 400 (validação), 404 (não encontrado), 409 (conflito – ex.: `codigo_tombamento` já usado), 422 (semântica), 500 (erro interno).
5. **Datas**: usar ISO 8601 (`YYYY-MM-DD` ou `YYYY-MM-DDTHH:mm:ssZ`).
6. **IDs**: inteiros auto-incrementais.

> Este texto-padrão pode ser copiado para outros projetos mudando apenas as entidades e os endpoints específicos.

---

## 2) Modelo de Dados (Tabelas)

### 1.1) Bem
Campos: `id`, `nome`, `codigo_tombamento` (único), `valor` (decimal), `status` (ex.: `em_uso`, `em_estoque`, `descartado`, `em_manutencao`), `ativo` (bool).

### 1.2) Categoria
Campos: `id`, `nome` (único), `ativo` (bool).

### 1.3) Setor
Campos: `id`, `nome` (único), `responsavel` (texto livre), `ativo` (bool).

> Observação: existe também a tabela **Responsavel** (pessoa) abaixo; o campo texto `responsavel` no **Setor** é mantido para simplicidade, mas a associação formal a pessoas ocorre via tabela **Responsavel**.

### 1.4) Movimentacao
Campos: `id`, `bem_id`, `setor_origem_id`, `setor_destino_id`, `data` (data/hora), `ativo` (bool).

### 1.5) Responsavel
Campos: `id`, `nome`, `cargo`, `ativo` (bool).

---

## 3) Endpoints CRUD

### 2.1) Bens
**Base**: `/bens`

#### POST `/bens`
Cria um bem.
Body (JSON):
```json
{
  "nome": "Notebook Dell 15",
  "codigo_tombamento": "TMB-2025-0001",
  "valor": 5200.00,
  "status": "em_uso"
}
```
Resposta 201:
```json
{
  "id": 1,
  "nome": "Notebook Dell 15",
  "codigo_tombamento": "TMB-2025-0001",
  "valor": 5200.00,
  "status": "em_uso",
  "ativo": true
}
```

#### GET `/bens`
Lista bens com **QueryParams opcionais**: `nome`, `codigo_tombamento`, `status`, `ativo` (true/false), `valor_min`, `valor_max`.
Exemplo: `/bens?status=em_uso&valor_max=6000`
Resposta 200:
```json
[
  { "id": 1, "nome": "Notebook Dell 15", "codigo_tombamento": "TMB-2025-0001", "valor": 5200.00, "status": "em_uso", "ativo": true }
]
```

#### GET `/bens/{id}`
Detalha um bem.
Resposta 200:
```json
{ "id": 1, "nome": "Notebook Dell 15", "codigo_tombamento": "TMB-2025-0001", "valor": 5200.00, "status": "em_uso", "ativo": true }
```

#### PUT `/bens/{id}`
Atualiza campos do bem.
Body (JSON):
```json
{ "nome": "Notebook Dell 15 3520", "status": "em_manutencao" }
```
Resposta 200: objeto atualizado.

#### DELETE `/bens/{id}` (Desativar)
Marca `ativo = false`.
Resposta 200:
```json
{ "message": "Bem desativado com sucesso", "id": 1, "ativo": false }
```

---

### 2.2) Categorias
**Base**: `/categorias`

#### POST `/categorias`
Body:
```json
{ "nome": "Informática" }
```

#### GET `/categorias`
QueryParams (opcionais): `nome`, `ativo`.

#### GET `/categorias/{id}`

#### PUT `/categorias/{id}`
Body:
```json
{ "nome": "Informática e Periféricos" }
```

#### DELETE `/categorias/{id}` (Desativar)

---

### 2.3) Setores
**Base**: `/setores`

#### POST `/setores`
Body:
```json
{ "nome": "TI", "responsavel": "Coord. de TI" }
```

#### GET `/setores`
QueryParams: `nome`, `responsavel`, `ativo`.

#### GET `/setores/{id}`

#### PUT `/setores/{id}`
Body:
```json
{ "responsavel": "Gerência de TI" }
```

#### DELETE `/setores/{id}` (Desativar)

---

### 2.4) Responsáveis
**Base**: `/responsaveis`

#### POST `/responsaveis`
Body:
```json
{ "nome": "Ana Lima", "cargo": "Analista" }
```

#### GET `/responsaveis`
QueryParams: `nome`, `cargo`, `ativo`.

#### GET `/responsaveis/{id}`

#### PUT `/responsaveis/{id}`
Body:
```json
{ "cargo": "Coordenadora" }
```

#### DELETE `/responsaveis/{id}` (Desativar)

---

### 2.5) Movimentações
**Base**: `/movimentacoes`

#### POST `/movimentacoes`
Registra movimentação de um bem.
Body:
```json
{
  "bem_id": 1,
  "setor_origem_id": 2,
  "setor_destino_id": 5,
  "data": "2025-10-20T14:30:00Z"
}
```
Resposta 201: objeto criado.

#### GET `/movimentacoes`
QueryParams: `bem_id`, `setor_origem_id`, `setor_destino_id`, `data_inicio`, `data_fim`, `ativo`.

#### GET `/movimentacoes/{id}`

#### PUT `/movimentacoes/{id}`
> Uso raro (em geral movimentações são imutáveis). Permita apenas corrigir `data` ou `setor_destino_id` com justificativa.

Body:
```json
{ "data": "2025-10-20T16:00:00Z" }
```

#### DELETE `/movimentacoes/{id}` (Desativar)
> Não apaga o histórico; apenas invalida o registro.

---

## 4) Endpoints Específicos

### 3.1) Buscar bem por código de tombamento
`GET /bens/buscar?codigo_tombamento=TMB-2025-0001`
Resposta 200:
```json
{ "id": 1, "nome": "Notebook Dell 15", "codigo_tombamento": "TMB-2025-0001", "status": "em_uso", "ativo": true }
```

### 3.2) Histórico de movimentações de um bem
`GET /bens/{id}/historico-movimentacoes`
Resposta 200:
```json
[
  { "id": 10, "bem_id": 1, "setor_origem_id": 2, "setor_destino_id": 5, "data": "2025-10-20T14:30:00Z", "ativo": true }
]
```

### 3.3) Listar bens por setor atual
`GET /bens/por-setor?setor_id=5`
> O “setor atual” é inferido pela **última movimentação ativa** do bem.
Resposta 200:
```json
[
  { "id": 1, "nome": "Notebook Dell 15", "codigo_tombamento": "TMB-2025-0001", "status": "em_uso", "ativo": true }
]
```

### 3.4) Desativar/reativar bem
- `POST /bens/{id}/desativar`
- `POST /bens/{id}/reativar`

Respostas 200:
```json
{ "id": 1, "ativo": false, "message": "Bem desativado" }
```
```json
{ "id": 1, "ativo": true, "message": "Bem reativado" }
```

### 3.5) Transferência rápida de setor (atalho de movimentação)
`POST /bens/{id}/transferir`
Body:
```json
{ "setor_destino_id": 7, "data": "2025-11-03T12:00:00Z" }
```
Resposta 201: retorna a **movimentação** criada.

### 3.6) Relatório simples: bens ativos por status
`GET /relatorios/bens-ativos-por-status`
Resposta 200:
```json
[
  { "status": "em_uso", "quantidade": 12 },
  { "status": "em_manutencao", "quantidade": 3 },
  { "status": "em_estoque", "quantidade": 8 }
]
```

---

## 5) Exemplos de Fluxo

### 4.1) Cadastro e movimentação
1) Cadastrar bem (POST `/bens`).
2) Registrar movimentação (POST `/movimentacoes`).
3) Listar bens por setor (GET `/bens/por-setor?setor_id=...`).

### 4.2) Desativação
1) Desativar bem (DELETE `/bens/{id}` ou POST `/bens/{id}/desativar`).
2) Evitar retorno em listagens usando `ativo=true` em GET.

---

## 6) Validações sugeridas
- `codigo_tombamento` **único** e obrigatório.
- `valor >= 0`.
- `status` dentro do conjunto permitido.
- `bem_id` e setores existentes ao registrar movimentação.
- Ao transferir: `setor_destino_id` ≠ último setor atual.

---

## 7) Observações finais
- **GET: todos os QueryParams são opcionais.**
- “Excluir” = desativar (`ativo = false`).
- Histórico é preservado via **Movimentacao**.
- Este documento é um **template**: troque nomes e campos para outros projetos mantendo a mesma lógica.

