    DROP TABLE IF EXISTS movimentacoes CASCADE;
    DROP TABLE IF EXISTS bens CASCADE;
    DROP TABLE IF EXISTS setores CASCADE;
    DROP TABLE IF EXISTS responsaveis CASCADE;
    DROP TABLE IF EXISTS categorias CASCADE;
    DROP TABLE IF EXISTS usuarios CASCADE;





    CREATE TABLE bens (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        codigo_tombamento VARCHAR(50) UNIQUE NOT NULL,
        valor DECIMAL(10, 2) NOT NULL,
        status VARCHAR(50) NOT NULL,
        ativo BOOLEAN NOT NULL DEFAULT TRUE,
        data_cadastro TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
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

    CREATE TABLE usuarios (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        senha VARCHAR(255) NOT NULL,
        tipo VARCHAR(20) NOT NULL, -- admin ou comum
        ativo BOOLEAN DEFAULT TRUE
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
    INSERT INTO bens (nome, codigo_tombamento, valor, status, ativo, data_cadastro) VALUES
    ('Notebook Dell Latitude', 'TMB-001', 4500.00, 'Em Uso', TRUE, '2024-01-15 09:30:00-03'),
    ('Monitor LG 29 Pol', 'TMB-002', 1200.00, 'Em Uso', TRUE, '2024-02-10 14:00:00-03'),
    ('Cadeira Ergonômica', 'TMB-003', 850.50, 'Disponível', TRUE, '2024-03-05 10:15:00-03'),
    ('Teclado Mecânico Logitech', 'TMB-004', 350.00, 'Em Uso', TRUE, '2024-05-20 16:45:00-03'),
    ('Mouse Gamer Razer', 'TMB-005', 280.00, 'Manutenção', TRUE, '2024-06-12 11:00:00-03'),
    ('Projetor Epson 4K', 'TMB-006', 3200.00, 'Em Uso', TRUE, '2024-08-01 08:00:00-03'),
    ('Servidor HP ProLiant', 'TMB-007', 15000.00, 'Em Uso', TRUE, '2024-09-15 13:20:00-03'),
    ('Switch Cisco 24 Portas', 'TMB-008', 2100.00, 'Disponível', TRUE, '2024-11-30 09:00:00-03'),
    ('Nobreak APC 1500VA', 'TMB-009', 1100.00, 'Em Uso', TRUE, '2025-01-05 15:30:00-03'),
    ('Tablet Samsung S9', 'TMB-010', 3800.00, 'Em Uso', TRUE, '2025-02-14 10:00:00-03'),
    ('Webcam Logitech C920', 'TMB-011', 450.00, 'Disponível', TRUE, '2025-03-22 17:10:00-03'),
    ('Impressora HP LaserJet', 'TMB-012', 1800.00, 'Manutenção', TRUE, '2025-05-10 14:40:00-03'),
    ('Ar Condicionado Split', 'TMB-013', 2500.00, 'Em Uso', TRUE, '2025-07-08 09:20:00-03'),
    ('Mesa de Reunião', 'TMB-014', 1300.00, 'Disponível', TRUE, '2025-09-12 11:50:00-03'),
    ('Roteador Wi-Fi 6', 'TMB-015', 750.00, 'Em Uso', TRUE, '2025-11-02 08:30:00-03'),
    ('Headset HyperX Cloud', 'TMB-016', 500.00, 'Em Uso', TRUE, '2026-01-20 13:00:00-03'),
    ('Estabilizador SMS', 'TMB-017', 150.00, 'Disponível', TRUE, '2026-02-15 10:45:00-03'),
    ('MacBook Air M2', 'TMB-018', 8500.00, 'Em Uso', TRUE, '2026-03-01 09:00:00-03'),
    ('Smartphone iPhone 15', 'TMB-019', 6200.00, 'Em Uso', TRUE, '2026-04-10 15:00:00-03'),
    ('Drone DJI Mini 4', 'TMB-020', 5400.00, 'Disponível', TRUE, '2026-04-20 11:20:00-03');

    INSERT INTO usuarios (username, senha, tipo)
    VALUES ('admin', '123', 'admin'),
    ('joao','123', 'comum');




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
