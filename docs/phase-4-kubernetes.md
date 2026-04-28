# Phase 4 — Orchestration with Kubernetes

## 🎯 Goal
Run the containerized API on a Kubernetes cluster with multiple replicas, self-healing, and a stable network entry point — the same way real production systems run.

## 🧠 Concepts learned
- **Cluster** vs **Node** vs **Pod** vs **Container** hierarchy
- **Deployment** as a controller: declares desired state ("I want N pods always")
- **Service** as a stable network endpoint that load-balances across pods
- **Labels and selectors** — the glue that connects Deployments, Services, and Pods
- **livenessProbe** ("are you alive?") vs **readinessProbe** ("are you ready for traffic?")
- Self-healing: when a pod dies, the Deployment immediately spawns a replacement
- "Cattle, not pets" — pods are disposable; the system tolerates and expects failure
- `NodePort` for exposing a service in local dev (vs `LoadBalancer` in real cloud)
- `kubectl port-forward` as a reliable fallback for local access

## 🛠️ What was built
- `k8s/deployment.yaml` — declares 2 replicas of the API with health probes hitting `/health`
- `k8s/service.yaml` — `NodePort` service on port 30080 routing to pods on port 8000
- A live local cluster (Docker Desktop with `kind` provider) running both manifests

## 📁 Files
```text
.
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

## ⚙️ Workflow
```bash
# Apply manifests
kubectl apply -f k8s/

# Inspect cluster state
kubectl get pods
kubectl get services
kubectl describe deployment devops-api

# Watch self-healing in action
kubectl delete pod <pod-name>
kubectl get pods   # a new one appears within seconds

# View logs from all pods at once
kubectl logs -l app=devops-api -f

# Access the API locally
kubectl port-forward service/devops-api 8000:80
# then open http://localhost:8000/docs
```

## 🧗 Challenges faced
- **NodePort wasn't reachable on localhost** — Docker Desktop's `kind` provider does not always bind NodePorts directly to the host. Solved by using `kubectl port-forward`, which is also more reliable for local development.
- **Confusion about why I need a Service if pods already have IPs** — pod IPs change every time a pod is recreated. The Service provides a stable IP and DNS name regardless of pod churn.
- **Probe frequency anxiety** — worried that probing `/health` every few seconds would generate cost or noise. Realized that a simple endpoint costs microseconds, and the protection against bad pods is worth orders of magnitude more.
- **Image not visible to the cluster** — the `kind` cluster has its own image store, separate from the regular Docker daemon. With Docker Desktop's integration, `imagePullPolicy: IfNotPresent` plus a locally built image was enough.

## 📚 References
- Kubernetes concepts: https://kubernetes.io/docs/concepts/
- Configure Liveness, Readiness and Startup Probes: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
- Service resource overview: https://kubernetes.io/docs/concepts/services-networking/service/
