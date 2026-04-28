# Phase 2 — Containerization with Docker

## 🎯 Goal
Package the API into a portable container so it runs identically on any machine, removing the classic "it works on my machine" problem.

## 🧠 Concepts learned
- Difference between **image** (recipe + frozen artifact) and **container** (running instance)
- Dockerfile instructions: `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`
- Layer caching: ordering instructions so dependencies are cached separately from source code
- Why containers are isolated filesystems (the "bag for the trip" analogy)
- `.dockerignore` for keeping secrets and build artifacts out of images
- Difference between `127.0.0.1` and `0.0.0.0` (binding interfaces)
- `docker-compose.yml` for declarative multi-service setups
- Image tagging and versioning (`devops-api:0.2.0`)

## 🛠️ What was built
- `docker/Dockerfile` — based on `python:3.12-slim`, installs deps, copies app, runs uvicorn
- `.dockerignore` — excludes `.git`, `.venv`, `__pycache__`, secrets
- `docker-compose.yml` — single-service definition with port mapping and restart policy
- Final image `devops-api:0.2.0` — ~250MB total, ~60MB compressed

## 📁 Files
```text
.
├── docker/
│   └── Dockerfile
├── .dockerignore
└── docker-compose.yml
```

## ⚙️ Workflow
```bash
# Build the image
docker build -f docker/Dockerfile -t devops-api:0.2.0 .

# Run with docker run (manual)
docker run -d --name devops-api -p 8000:8000 devops-api:0.2.0

# Or with docker compose (recommended)
docker compose up -d

# Inspect
docker ps
docker logs devops-api
docker exec -it devops-api bash

# Tear down
docker compose down
```

## 🧗 Challenges faced
- **Why copy `requirements.txt` BEFORE the source code?** — to take advantage of layer caching: deps change rarely, source code changes constantly. Putting source last means rebuilds skip the slow `pip install` step.
- **`EXPOSE` does not actually open a port** — it's only documentation. The port is opened with `-p` on `docker run` (or `ports:` in compose).
- **PowerShell prompt leaking into YAML files** — copying multi-line YAML while `(.venv)` was active inserted the prompt text into the file. Fix: `deactivate` before pasting, or use Git Bash.

## 📚 References
- Dockerfile reference: https://docs.docker.com/reference/dockerfile/
- Docker layer caching best practices: https://docs.docker.com/build/cache/
- Compose file reference: https://docs.docker.com/compose/compose-file/
