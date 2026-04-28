# 🚀 DevOps from Scratch — Infra

A portfolio project documenting my hands-on journey learning DevOps — from code to infrastructure, from CI/CD to monitoring.

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/k8s-ready-326CE5?logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?logo=terraform&logoColor=white)

---

## 📖 About this project

This repository documents, **phase by phase**, the construction of a complete application surrounded by a modern DevOps lifecycle. The goal is not just to have working code, but to **demonstrate the learning process** and the technical decisions taken at each step.

> 💡 Each phase has its own dedicated documentation in [`docs/`](docs/), with concepts learned, challenges faced, and references used.

## 🎯 What is built here

A simple **Python REST API (FastAPI)** wrapped with all the infrastructure, automation, and observability expected in a real production environment:

Code → Container → CI/CD → Cluster → Cloud → Metrics

## 🛠️ Tech stack

| Layer            | Technology                  | Phase |
|------------------|----------------------------|-------|
| Application      | Python · FastAPI · Pytest  | 1     |
| Containerization | Docker · Docker Compose    | 2     |
| CI/CD            | GitHub Actions             | 3     |
| Orchestration    | Kubernetes · Helm          | 4     |
| Infrastructure   | Terraform · AWS            | 5     |
| Observability    | Prometheus · Grafana       | 6     |

## 🗺️ Roadmap

- [x] **Phase 1** — Python API (FastAPI) with endpoints, tests, and clean structure
- [x] **Phase 2** — Docker containerization & multi-stage builds
- [x] **Phase 3** — CI/CD pipeline with GitHub Actions
- [x] **Phase 4** — Kubernetes deployments, services, and ingress
- [x] **Phase 5** — Cloud infrastructure provisioning with Terraform
- [ ] **Phase 6** — Monitoring with Prometheus and Grafana dashboards

## 📁 Repository structure

```text
.
├── app/             # API source code (FastAPI)
├── docker/          # Dockerfiles & docker-compose
├── .github/         # GitHub Actions workflows
├── k8s/             # Kubernetes manifests
├── terraform/       # Infrastructure as Code
├── monitoring/      # Prometheus & Grafana configs
└── docs/            # Phase-by-phase documentation
```

## 🚀 Getting started

> ⚠️ Commands will be expanded as each phase is completed.

```bash
# Clone the repository
git clone https://github.com/AraujoVinic01/Infra.git
cd Infra
```

## 📚 Documentation

Detailed write-ups for each phase live under [`docs/`](docs/):

- [`docs/phase-1-api.md`](docs/phase-1-api.md) — Python API foundations
- [`docs/phase-2-docker.md`](docs/phase-2-docker.md) — Containerization with Docker
- [`docs/phase-3-cicd.md`](docs/phase-3-cicd.md) — CI with GitHub Actions
- [`docs/phase-4-kubernetes.md`](docs/phase-4-kubernetes.md) — Orchestration with Kubernetes
- [`docs/phase-5-terraform.md`](docs/phase-5-terraform.md) — Infrastructure as Code with Terraform
- `docs/phase-6-monitoring.md` — _coming soon_

## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

Built with ☕ and curiosity by [AraujoVinic01](https://github.com/AraujoVinic01)