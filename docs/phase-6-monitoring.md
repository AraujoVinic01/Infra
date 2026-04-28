# Phase 6 — Monitoring with Prometheus & Grafana

## 🎯 Goal
Add observability to the DevOps API: collect metrics from running pods, store them as time series, and visualize trends in dashboards.

## 🧠 Concepts learned
- **Three pillars of observability**: metrics, logs, traces (focus on metrics here)
- **Pull vs push**: Prometheus scrapes targets instead of receiving pushes
- **Metric types**: counter, gauge, histogram, summary
- **Service discovery**: Prometheus auto-finds pods via Kubernetes API + annotations
- **PromQL basics**: `rate()`, `sum() by ()`, label filtering
- **ConfigMap**: external configuration mounted into pods
- **RBAC**: ServiceAccount + ClusterRole + ClusterRoleBinding to grant API access
- **Dashboard as code mindset**: queries are declarative and reproducible

## 🛠️ What was built
- API instrumented with `prometheus-fastapi-instrumentator` (exposes `/metrics`)
- Docker image `devops-api:0.3.0` with monitoring support
- Kubernetes deployment annotated for Prometheus auto-discovery
- Prometheus deployed inside the cluster, scraping all annotated pods
- Grafana deployed alongside, connected to Prometheus as data source
- Custom dashboard with PromQL queries on real HTTP traffic

## 📁 Files
```text
.
├── app/main.py                          # API with Instrumentator()
├── docker/Dockerfile                    # rebuilt as 0.3.0
├── k8s/deployment.yaml                  # with prometheus.io/* annotations
└── monitoring/
    ├── prometheus-rbac.yaml             # ServiceAccount + Role + Binding
    ├── prometheus-config.yaml           # ConfigMap with scrape config
    ├── prometheus-deployment.yaml       # Prometheus pod + Service
    └── grafana-deployment.yaml          # Grafana pod + Service
```

## ⚙️ Workflow
```bash
# Apply monitoring stack
kubectl apply -f monitoring/

# Check Prometheus targets
kubectl port-forward service/prometheus 9090:9090
# open http://localhost:9090 → Status → Targets

# Open Grafana
kubectl port-forward service/grafana 3000:3000
# open http://localhost:3000 (admin/admin)
```

## 📊 Example PromQL queries
```promql
# Total requests across all pods
sum(http_requests_total)

# Requests per second by endpoint
sum(rate(http_requests_total[1m])) by (handler)

# Total requests per pod
sum(http_requests_total) by (pod)
```

## 🧗 Challenges faced
- **Backslash escapes in heredoc** — `cat > file << 'EOF'` preserved `\$1:\$2` literally instead of treating them as regex backreferences. The Prometheus config produced URLs like `http://\10.244.0.13:\8000`, all DOWN. Fixed by writing `$1:$2` directly and using `[0-9]+` instead of `\d+`.
- **ConfigMap doesn't auto-reload** — updating the ConfigMap doesn't restart pods that mount it. Fixed with `kubectl rollout restart deployment/prometheus`.
- **Slim images don't ship `curl`** — `kubectl exec ... curl` failed because the base image is minimal. Used `kubectl port-forward` instead, which is also closer to how a real human inspects a pod.
- **NodePort not reachable on Docker Desktop** — same issue as Phase 4. `port-forward` is the reliable way to access services from the host.

## 📚 References
- Prometheus documentation: https://prometheus.io/docs/
- PromQL basics: https://prometheus.io/docs/prometheus/latest/querying/basics/
- prometheus-fastapi-instrumentator: https://github.com/trallnag/prometheus-fastapi-instrumentator
- Grafana getting started: https://grafana.com/docs/grafana/latest/getting-started/
