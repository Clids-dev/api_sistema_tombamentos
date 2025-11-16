-- ============================================
-- Remover tabelas existentes (se houver)
-- ============================================
DROP TABLE IF EXISTS bem CASCADE;
DROP TABLE IF EXISTS categoria CASCADE;
DROP TABLE IF EXISTS setor CASCADE;
DROP TABLE IF EXISTS movimentacao CASCADE;
DROP TABLE IF EXISTS responsavel CASCADE;

-- ============================================
-- Criação das Tabelas
-- ============================================
-- Tabela Bem
CREATE TABLE bens (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    codigo_tombamento VARCHAR(50) UNIQUE,
    valor NUMERIC(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (
        status IN ('em_uso','em_estoque','descartado','em_manutencao')
    ),
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);