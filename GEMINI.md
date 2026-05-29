# Sistema de Tombamento - Project Context

This project is a **Sistema de Tombamento** (Asset Tracking System) developed to manage corporate assets, their locations, and movements. It provides a web interface and a REST API for CRUD operations on assets, categories, sectors, and personnel.

## Technology Stack
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.x)
- **Database:** PostgreSQL (using `psycopg2-binary`)
- **Frontend:** HTML5, Jinja2 Templates, Bootstrap 5
- **JavaScript:** ES6+ Modules (Modular and Decoupled)
- **Validation:** [Pydantic](https://docs.pydantic.dev/)

## Project Architecture
The project follows a modular structure where each domain entity resides in the `modules/` directory.

### Directory Structure
- `api/v1/`: FastAPI router definitions (JSON API).
- `web/`: FastAPI routes for rendering Jinja2 templates (UI).
- `core/`:
  - `database.py`: Custom `DataBase` class for connection pooling and raw SQL execution.
  - `config.py`: Application configurations (DB credentials, etc.).
- `modules/<module_name>/`:
  - `repository.py`: Data access layer (SQL execution).
  - `service.py`: Business logic layer.
  - `schemas.py`: Pydantic models for validation.
  - `queries.py`: Raw SQL query definitions.
- `static/`:
  - `css/`: Global styles (`style.css`).
  - `js/`: Modular JavaScript logic (`utils.js`, `bens.js`, etc.).
- `templates/`:
  - `base.html`: Master template (Navbar, Sidebar, shared structure).
  - `<page>.html`: Page-specific content inheriting from `base.html`.
- `main.py`: Application entry point.

## Development Conventions

### Frontend & UI
- **Template Inheritance:** All pages must extend `base.html` using `{% extends "base.html" %}`.
- **JavaScript Modules:** Use `<script type="module">` to keep logic isolated and reusable.
- **DOM Access:** Use the `$` helper from `utils.js` for selectors (e.g., `$('#id')`).
- **API Calls:** Always use the `api` helper from `utils.js` (e.g., `await api.get('/url')`) to ensure consistent error handling and JSON parsing.
- **Efficient Rendering:** Prefer `.map().join('')` over `innerHTML +=` in loops for better performance.

### Data Layer
- **Raw SQL:** No ORM used. All database interactions are via raw SQL in `queries.py`.
- **Soft Deletes:** Deletion is handled by setting the `ativo` column to `FALSE`.
- **Naming Conventions:** Assets (Bens) have automatic tracking codes generated as `SIGLA-00X`, where `SIGLA` is a normalized, non-accented 3-letter code from the Category.

### Authentication & Authorization
- Session management via cookies (`username`, `tipo`).
- Access levels: `admin` and `comum`.

## Core Entities
- **Bem (Asset):** Linked to a Category and a Sector (via movement).
- **Categoria (Category):** Defines the asset type and prefix for its tracking code (sigla).
- **Setor (Sector):** Physical or logical location of an asset.
- **Responsável (Personnel):** Person in charge of a sector or asset.
- **Movimentação (Movement):** Auditable log of asset transfers between sectors.
- **Usuário (User):** System credentials.

## Building and Running

### Prerequisites
- Python 3.x
- PostgreSQL

### Setup
1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Initialize DB with `tabelasDados.sql`.
5. Run: `uvicorn main:app --reload`
