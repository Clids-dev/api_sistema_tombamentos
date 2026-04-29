# Sistema de Tombamento - Project Context

This project is a **Sistema de Tombamento** (Asset Tracking System) developed to manage corporate assets, their locations, and movements. It provides a web interface and a REST API for CRUD operations on assets, categories, sectors, and personnel.

## Technology Stack
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Runtime:** Python 3.x
- **Database:** PostgreSQL (using `psycopg2-binary`)
- **Frontend:** HTML templates with [Jinja2](https://jinja.palletsprojects.com/)
- **Validation:** [Pydantic](https://docs.pydantic.dev/)
- **Configuration:** `python-dotenv`

## Project Architecture
The project follows a modular structure, where each domain entity resides in the `modules/` directory.

### Directory Structure
- `api/routes/`: FastAPI router definitions (controllers).
- `core/`:
  - `db.py`: Custom `DataBase` class for connection management and raw SQL execution.
  - `settings.py`: Application configurations (DB credentials, etc.).
- `modules/<module_name>/`:
  - `repository.py`: Data access layer (SQL execution).
  - `service.py`: Business logic layer.
  - `schemas.py`: Pydantic models for validation.
  - `querys.py`: Raw SQL query definitions.
- `static/`: Static assets (CSS, images).
- `templates/`: Jinja2 HTML templates.
- `main.py`: Application entry point.

## Building and Running

### Prerequisites
- Python 3.x
- PostgreSQL database

### Installation
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup
1. Create a database named `sistema_tombamento` in PostgreSQL.
2. Update `core/settings.py` with your database credentials.
3. Run the initialization script:
   ```bash
   psql -U <your_user> -d sistema_tombamento -f tabelasDados.sql
   ```

### Execution
Run the development server:
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.
Interactive docs: `http://127.0.0.1:8000/docs`.

## Development Conventions

### Data Layer
- **Raw SQL:** The project avoids ORMs. All database interactions are done via raw SQL stored in `querys.py` files within each module.
- **Soft Deletes:** Deletion is typically handled as a soft delete by setting the `ativo` column to `FALSE`.
- **Database Helper:** Always use the `DataBase` class from `core/db.py` to ensure connections are properly opened and closed.

### API & Routing
- Route files in `api/routes/` should ideally only handle request/response logic and delegate business logic to the corresponding `Service` class.
- Frontend routes (rendering templates) are separated from pure API routes (e.g., `bensView_route.py` vs `bem_route.py`).

### Authentication & Authorization
- Basic session management is implemented using cookies (`username`, `tipo`).
- Users are categorized as `admin` or `comum`.

## Core Entities
- **Bem (Asset):** The main entity representing an item being tracked.
- **Categoria (Category):** Classification for assets.
- **Setor (Sector):** Locations where assets are placed.
- **Responsável (Personnel):** People responsible for assets or sectors.
- **Movimentação (Movement):** Records of asset transfers between sectors.
- **Usuário (User):** System users for authentication.
