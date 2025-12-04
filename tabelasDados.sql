DROP TABLE responsaveis CASCADE;
DROP TABLE setores CASCADE;
DROP TABLE movimentacoes CASCADE;
DROP TABLE bens CASCADE;
DROP TABLE categorias CASCADE;






CREATE TABLE bens (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    codigo_tombamento VARCHAR(50) UNIQUE NOT NULL,
    valor DECIMAL NOT NULL,
    status VARCHAR(50) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE responsaveis(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE setores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    responsavel_id INTEGER REFERENCES responsaveis(id),
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE movimentacoes (
    id SERIAL PRIMARY KEY,
    bem_id INTEGER REFERENCES bens(id),
    setor_origem_id INTEGER REFERENCES setores(id),
    setor_destino_id INTEGER REFERENCES setores(id),
    data_movimentacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    justificativa VARCHAR(500),
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

BEGIN; -- Inicia transação para garantir integridade

-- 1. Inserir Categorias
INSERT INTO categorias (nome, ativo) VALUES
('Informática', TRUE),
('Mobiliário', TRUE),
('Veículos', TRUE),
('Eletrônicos', TRUE);

-- 2. Inserir Responsáveis (Necessário criar antes dos Setores)
INSERT INTO responsaveis (nome, cargo, ativo) VALUES
('Carlos Mendes', 'Gerente de TI', TRUE),
('Fernanda Costa', 'Diretora Financeira', TRUE),
('João Batista', 'Chefe de Almoxarifado', TRUE),
('Mariana Alves', 'Supervisora de RH', TRUE);

-- 3. Inserir Setores (Vinculando aos Responsáveis criados acima)
-- IDs esperados: 1=Carlos, 2=Fernanda, 3=João, 4=Mariana
INSERT INTO setores (nome, responsavel_id, ativo) VALUES
('Departamento de Tecnologia', 1, TRUE),
('Financeiro', 2, TRUE),
('Almoxarifado Central', 3, TRUE),
('Recursos Humanos', 4, TRUE);

-- 4. Inserir Bens
INSERT INTO bens (nome, codigo_tombamento, valor, status, ativo) VALUES
('Notebook Lenovo Thinkpad', 'PAT-2024-001', 4200.00, 'em_uso', TRUE),
('Monitor Samsung 27"', 'PAT-2024-002', 1200.50, 'em_uso', TRUE),
('Cadeira Presidente', 'PAT-2024-003', 850.00, 'em_estoque', TRUE),
('Mesa em L', 'PAT-2024-004', 600.00, 'em_uso', TRUE),
('Servidor Dell PowerEdge', 'PAT-2024-005', 25000.00, 'em_manutencao', TRUE);

-- 5. Inserir Movimentações
-- IDs de Setores esperados: 1=TI, 2=Financeiro, 3=Almoxarifado, 4=RH
-- IDs de Bens esperados: 1=Notebook, 2=Monitor, 3=Cadeira...

INSERT INTO movimentacoes (bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo) VALUES
-- Notebook saiu do Almoxarifado (3) para TI (1)
(1, 3, 1, '2024-01-10 09:00:00', TRUE),

-- Monitor saiu do Almoxarifado (3) para TI (1)
(2, 3, 1, '2024-01-10 09:05:00', TRUE),

-- Cadeira chegou direto no Almoxarifado (Origem NULL = Compra nova)
(3, NULL, 3, '2024-01-15 14:00:00', TRUE),

-- Mesa saiu do Almoxarifado (3) para o RH (4)
(4, 3, 4, '2024-01-20 10:30:00', TRUE),

-- Servidor saiu da TI (1) para Manutenção externa (destino pode ser NULL ou um setor específico de manutenção, aqui simulando volta para Almoxarifado)
(5, 1, 3, NOW(), TRUE);

COMMIT; -- Confirma a gravação