# Project Blank 🚀

A robust, feature-rich FastAPI boilerplate designed to kickstart your next pet project or enterprise service without wasting time on repetitive boilerplate code.

---

### 🏁 Quick Start

Before you start developing, follow these steps:

1.  **Sync dependencies:**
    ```bash
    uv sync
    ```
2.  **Setup environment:**
    Copy the `.env.template` to a new `.env` file:
    ```bash
    cp .env.template .env
    ```
3.  **Generate secret tokens:**
    Open the Python terminal and generate secrets for `access_token` and other fields:
    ```python
    import secrets
    print(secrets.token_urlsafe(32))
    ```
    Copy the resulting strings into the corresponding fields in your `.env` file.

4.  **Database:**
    ⚠️ **Don't forget** to change the database URLs (`DATABASE_URL`) in the `.env` file to match your local settings or Docker container.

---

### 💻 Tech Stack

The boilerplate includes a modern and high-performance stack:

*   🐍 **Python >= 3.13**
*   ⚡ **FastAPI** — modern web framework.
*   🛡️ **FastAPI-Users** — ready-made Auth implementation (JWT / Database tokens).
*   🗄️ **SQLAlchemy 2.0 (Asyncio)** — next-generation ORM.
*   🐘 **Asyncpg** — the fastest asynchronous PostgreSQL driver.
*   🔄 **Alembic** — migration management (already configured with **async** template).
*   ✅ **Pydantic v2 & Pydantic-Settings** — data validation and convenient configuration management.
*   🚀 **Uvicorn** — high-performance ASGI server.
*   📦 **uv** — lightning-fast package manager.

---

### 🏗 Implementation Details

Your boilerplate is more than just an empty project; it's a well-thought-out architecture:

*   **Clean Architecture:** Split into `core` (logic), `api` (endpoints), `models` (DB), and `schemas` (validation).
*   **Full Auth Cycle:** Registration, login, logout, and current user management (`/me`).
*   **Database Helper:** A convenient singleton for obtaining asynchronous sessions.
*   **Modular API:** API versioning (`/api/v1/...`) is pre-configured.
*   **Automation:** Automatic `snake_case` table name generation based on model class names.
*   **Logging:** Configured `logging` with structured and readable formatting.

---

### 🐳 Docker & Deployment

⚠️ **Important Warning:**
The boilerplate **does not include** ready-made `Dockerfile` and `docker-compose.yaml` (even if folders exist). The user must **manually** create the Docker configuration to suit their specific needs (image choice, networks, dependencies) if they plan to run the project via containers.

---

### 🎯 Why use this?
Stop rewriting the same helpers for every new repository. **Project Blank** provides a solid architectural foundation, allowing you to focus on business logic from minute one.
