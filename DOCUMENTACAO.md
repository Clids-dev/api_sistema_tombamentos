# 📚 Documentação do Projeto: PatriFlow (Sistema de Tombamento)

Este documento serve como um guia de estudos e registro de evolução do projeto **PatriFlow**. Aqui você encontrará o objetivo do sistema, a arquitetura utilizada, o porquê das decisões técnicas e o roteiro (roadmap) do que já foi feito e o que virá a seguir.

---

## 🎯 Objetivo do Projeto
O **PatriFlow** é um sistema de gestão de patrimônio (tombamento) focado em simplicidade e eficiência. O objetivo é permitir que organizações controlem seus ativos (notebooks, móveis, veículos), saibam onde estão localizados (setores), quem são os responsáveis e todo o histórico de movimentação entre departamentos.

---

## 🏗️ Arquitetura e Decisões Técnicas

O projeto foi construído utilizando **FastAPI** (Python) no backend e **Bootstrap 5** com **Vanilla JS** no frontend.

### Por que estas escolhas?

1.  **FastAPI vs Django/Flask:**
    *   Escolhemos o FastAPI por ser moderno, extremamente rápido e possuir validação de dados nativa com Pydantic. Ele facilita a criação de APIs que o Frontend consome via JavaScript (\`fetch\`).
2.  **Raw SQL (psycopg2) vs ORM (SQLAlchemy):**
    *   **Decisão:** Estamos usando SQL puro em arquivos \`querys.py\`.
    *   **Por quê?** Para um estudante, entender como o SQL funciona "por baixo dos panos" é fundamental. Isso evita a "caixa preta" dos ORMs e garante performance total em consultas complexas.
3.  **Arquitetura Modular:**
    *   O projeto é dividido em \`modules/\` (bem, setor, usuario, etc.). Cada módulo tem seu próprio \`repository\` (acesso a dados), \`service\` (regra de negócio) e \`schemas\` (validação). Isso mantém o código organizado e fácil de escalar.
4.  **Soft Delete (Ativo/Inativo):**
    *   Em sistemas de auditoria, **nunca deletamos um registro do banco**. Usamos uma coluna \`ativo\` (BOOLEAN). Se o item for "excluído", apenas marcamos como \`FALSE\`. Isso preserva o histórico de movimentações.

---

## ✅ O que já foi feito (Log de Atividades)

### 1. Estrutura Backend
- [x] Configuração da conexão com banco de dados PostgreSQL (\`core/db.py\`).
- [x] Criação dos módulos base: \`Bem\`, \`Categoria\`, \`Setor\`, \`Responsavel\`, \`Movimentacao\` e \`Usuario\`.
- [x] Implementação de Services e Repositories para operações CRUD.
- [x] **Nova Funcionalidade:** Endpoint de detalhes do bem (\`/bem/{id}/detalhes\`) que retorna o setor atual e a última movimentação.

### 2. Interface Frontend (UI/UX)
- [x] **Dashboard:** Página principal com cards de estatísticas dinâmicos e lista de categorias ativas.
- [x] **Gestão de Bens:** 
    *   Sidebar padronizada e harmônica com o tema Nubank.
    *   **Paginação:** Listagem limitada a 10 itens por página com navegação fluida.
    *   **Visualização Detalhada:** Componente de "olho" que abre um modal com informações completas do bem.
    *   **Filtros Avançados:** Novo componente para filtrar a listagem por **Status** de forma combinada com a busca por nome/código.
- [x] **Redesign do Login:** Paleta Nubank e layout estilo Facebook.

---

## 🗺️ Roadmap de Desenvolvimento (Padrão de Estudo)

Este roadmap segue a ordem lógica de complexidade de um sistema corporativo.

### Fase 1: Fundação (Concluída)
- [x] Modelagem do Banco de Dados.
- [x] Login e Autenticação básica.
- [x] CRUD de Bens (Equipamentos) com Paginação, Detalhes e Filtros.

### Fase 2: Gestão de Estrutura (Em Andamento)
- [ ] **Módulo de Setores:** Criar interface para gerenciar os departamentos da empresa.
- [ ] **Módulo de Responsáveis:** Cadastro das pessoas que respondem pelos bens.
- [ ] **Módulo de Categorias:** Organização dos bens por tipo.

---

## 💡 Dica de Estudo
O novo sistema de **Filtros Combinados** utiliza lógica booleana no JavaScript (\`matchesBusca && matchesStatus\`). Isso permite que o usuário refine a busca de forma muito precisa, por exemplo: "Procure apenas Notebooks que estejam em Manutenção".
