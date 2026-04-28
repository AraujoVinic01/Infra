# Phase 3 — CI with GitHub Actions

## 🎯 Goal
Automate quality checks so every push and pull request runs the test suite without manual effort, preventing broken code from reaching `main`.

## 🧠 Concepts learned
- Difference between **CI** (Continuous Integration) and **CD** (Continuous Delivery/Deployment)
- GitHub Actions workflow file structure (`name`, `on`, `jobs`, `steps`)
- Workflow triggers: `push` and `pull_request` filtered by branch
- GitHub-hosted runners (`ubuntu-latest`) — free disposable VMs
- Reusable actions from the marketplace (`actions/checkout`, `actions/setup-python`)
- How CI status checks integrate into Pull Requests (green/red checks)
- Importance of pinning action versions (`@v4`, `@v5`)

## 🛠️ What was built
- `.github/workflows/ci.yml` — workflow that:
  1. Checks out the repository
  2. Sets up Python 3.12
  3. Installs dependencies from `requirements.txt`
  4. Runs `pytest -v`
- Triggers on every push and PR targeting `main`

## 📁 Files
```text
.
└── .github/
    └── workflows/
        └── ci.yml
```

## ⚙️ Workflow
```bash
# Create branch and add the workflow file
git checkout -b phase-3-cicd
mkdir -p .github/workflows

# After editing ci.yml, commit and push
git add .github/workflows/ci.yml tests/
git commit -m "ci: add GitHub Actions workflow and pytest tests"
git push -u origin phase-3-cicd

# Open a PR — the workflow runs automatically
# Check status at: https://github.com/<user>/<repo>/actions
```

## 🧗 Challenges faced
- **First push didn't seem to trigger anything** — turned out the Actions tab was redirecting to `/actions/new` because the workflow only existed on the branch, not on `main` yet. Once the PR was opened, the workflow ran on the PR.
- **YAML indentation pain** — YAML is whitespace-sensitive. A single misaligned `steps:` broke the whole file silently. Lesson: always run `yamllint` mentally and trust the editor's indent guides.
- **Understanding what gets cached vs re-downloaded** — by default each run starts from a clean VM. Caching pip dependencies (with `actions/cache`) is a future optimization.

## 📚 References
- GitHub Actions documentation: https://docs.github.com/en/actions
- Workflow syntax reference: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions
- `actions/setup-python`: https://github.com/actions/setup-python
