-- 1. Limpeza (Opcional: remove as tabelas se já existirem para recriar do zero)
DROP TABLE IF EXISTS movimentacoes;
DROP TABLE IF EXISTS bens;
DROP TABLE IF EXISTS setores;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS responsaveis;

-- 2. Criação da tabela Categoria
-- (Criada primeiro pois não depende de ninguém)
CREATE TABLE categorias (
    nome VARCHAR(100) NOT NULL UNIQUE,
    id SERIAL PRIMARY KEY,
    ativo BOOLEAN DEFAULT TRUE
);

-- 3. Criação da tabela Responsavel
-- (Conforme solicitado no item 1.5)
CREATE TABLE responsaveis (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cargo VARCHAR(100),
    ativo BOOLEAN DEFAULT TRUE
);

-- 4. Criação da tabela Setor
-- (O campo 'responsavel' aqui é texto livre conforme o item 1.3)
CREATE TABLE setores (
    nome VARCHAR(100) NOT NULL UNIQUE,
    id SERIAL PRIMARY KEY,
    responsavel VARCHAR(150),
    ativo BOOLEAN DEFAULT TRUE
);

-- 5. Criação da tabela Bem
-- (Inclui restrição CHECK para garantir que o status seja válido)
CREATE TABLE bens (
    nome VARCHAR(200) NOT NULL,
    codigo_tombamento VARCHAR(50) NOT NULL UNIQUE,
    id SERIAL PRIMARY KEY,
    valor NUMERIC(15, 2), -- Suporta valores monetários com 2 casas decimais
    status VARCHAR(30) CHECK (status IN ('em_uso', 'em_estoque', 'descartado', 'em_manutencao')),
    ativo BOOLEAN DEFAULT TRUE
    -- Nota: Se desejar vincular o Bem à Categoria, descomente a linha abaixo:
    -- , categoria_id INTEGER REFERENCES categoria(id)
);

-- 6. Criação da tabela Movimentacao
-- (Depende das tabelas Bem e Setor)
CREATE TABLE movimentacoes (
    id SERIAL PRIMARY KEY,
    bem_id INTEGER NOT NULL REFERENCES bens(id),
    setor_origem_id INTEGER REFERENCES setores(id), -- Pode ser nulo se for a primeira entrada
    setor_destino_id INTEGER NOT NULL REFERENCES setores(id),
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE
);
-- Inicia uma transação para garantir que tudo seja inserido ou nada seja (segurança)
BEGIN;

-- 1. Inserindo Categorias
INSERT INTO categorias (nome, ativo) VALUES
('Informática', TRUE),
('Mobiliário', TRUE),
('Veículos', TRUE),
('Eletrodomésticos', TRUE);

-- 2. Inserindo Responsáveis (Pessoas)
INSERT INTO responsaveis (nome, cargo, ativo) VALUES
('Ana Silva', 'Gerente de TI', TRUE),
('Carlos Souza', 'Analista de RH', TRUE),
('Roberto Dias', 'Almoxarife', TRUE),
('Mariana Lima', 'Diretora Financeira', TRUE);

-- 3. Inserindo Setores
-- O campo 'responsavel' aqui é texto, conforme sua estrutura original
INSERT INTO setores (nome, responsavel, ativo) VALUES
('Departamento de TI', 'Ana Silva', TRUE),
('Recursos Humanos', 'Carlos Souza', TRUE),
('Almoxarifado Central', 'Roberto Dias', TRUE),
('Manutenção Externa', 'Empresa Terceira', TRUE);

-- 4. Inserindo Bens (Patrimônio)
-- Note que os status devem respeitar a restrição CHECK criada anteriormente
INSERT INTO bens (nome, codigo_tombamento, valor, status, ativo) VALUES
('Notebook Dell Latitude', 'TB-00100', 4500.00, 'em_uso', TRUE),
('Monitor LG 24pol', 'TB-00101', 850.00, 'em_uso', TRUE),
('Cadeira Ergonômica', 'TB-00200', 600.00, 'em_estoque', TRUE),
('Mesa de Reunião', 'TB-00201', 1200.00, 'em_uso', TRUE),
('Projetor Epson', 'TB-00300', 2500.00, 'em_manutencao', TRUE),
('Carro Fiat Fiorino', 'TB-00400', 55000.00, 'em_uso', TRUE),
('Teclado Antigo', 'TB-99999', 50.00, 'descartado', FALSE);

-- 5. Inserindo Movimentações
-- Estamos assumindo os IDs gerados sequencialmente (1, 2, 3...) pelas inserções acima.
-- Exemplo: Bem ID 1 (Notebook) saiu do Setor 3 (Almoxarifado) para Setor 1 (TI)
INSERT INTO movimentacoes (bem_id, setor_origem_id, setor_destino_id, data, ativo) VALUES
(1, 3, 1, '2023-10-01 08:30:00', TRUE),  -- Notebook foi para TI
(2, 3, 1, '2023-10-01 08:35:00', TRUE),  -- Monitor foi para TI
(3, NULL, 3, '2023-09-15 10:00:00', TRUE), -- Cadeira chegou direto no Almoxarifado (Origem NULL)
(5, 1, 4, NOW(), TRUE);                  -- Projetor saiu da TI para Manutenção (Data de agora)

-- Confirma as alterações
COMMIT;