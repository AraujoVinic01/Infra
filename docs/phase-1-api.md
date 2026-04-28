# Phase 1 — Python API with FastAPI

## 🎯 Goal
Build the foundational REST API that will be the core of the entire DevOps pipeline. Keep it simple but production-ready (typed, tested, with health checks).

## 🧠 Concepts learned
- REST API basics (HTTP methods, status codes, JSON responses)
- FastAPI framework: decorators, type hints, automatic OpenAPI docs
- Python virtual environments (`.venv`) for dependency isolation
- `requirements.txt` for reproducible installs
- Unit testing with `pytest` and FastAPI's `TestClient`
- The role of a `/health` endpoint (used by orchestrators like Kubernetes)
- Conventional Commits (`feat:`, `chore:`, etc.)
- Git branches and Pull Request workflow

## 🛠️ What was built
- `app/main.py` — FastAPI application instance with two endpoints
- `GET /` — welcome message
- `GET /health` — health check returning `{"status": "healthy"}`
- Auto-generated docs at `/docs` (Swagger UI) and `/redoc`
- `tests/test_main.py` — two tests covering both endpoints
- `requirements.txt` — pinned dependencies (FastAPI, uvicorn, pytest, httpx)

## 📁 Files
```text
.
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── requirements.txt
```

## ⚙️ Workflow
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run the API locally
uvicorn app.main:app --reload

# Run tests
pytest -v
```

## 🧗 Challenges faced
- **Understanding why a virtualenv matters** — at first it seemed like extra work. Realized it isolates per-project dependencies and matches how Docker/CI environments behave.
- **Confusion between FastAPI and Postman** — FastAPI is the framework that *builds* the API; Postman is a client that *consumes* APIs. They are complements, not alternatives. The auto-generated `/docs` page replaces Postman for most testing during development.
- **Encoding issues on Windows** — `Out-File` in PowerShell was creating files with BOM that broke YAML/Python parsing. Solved by using Git Bash with `cat > file << 'EOF'`.

## 📚 References
- FastAPI official tutorial: https://fastapi.tiangolo.com/tutorial/
- Pytest documentation: https://docs.pytest.org/
- HTTP status codes overview: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
