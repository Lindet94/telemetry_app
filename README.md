# Telemetry App

A FastAPI-based telemetry application with PostgreSQL backend, deployed on Kubernetes with monitoring and CI/CD pipeline.

## Features

- RESTful API for telemetry data management
- PostgreSQL database with connection pooling
- Prometheus metrics collection
- Grafana dashboards for monitoring
- Kubernetes deployment with Helm-style structure
- GitHub Actions CI/CD pipeline
- Docker containerization

## Prerequisites

- Docker
- Minikube (for local Kubernetes)
- kubectl
- Python 3.10+
- Node.js (for some tools)

## Quick Start

### 1. Start Minikube

```bash
minikube start --driver=docker
eval $(minikube docker-env)
```

### 2. Build and Deploy

```bash
# Build the application image
docker build -t telemetry-app:dev .

# Load image into Minikube
minikube image load telemetry-app:dev

# Deploy database resources
kubectl apply -f k8s/base/db/

# Deploy the application
kubectl apply -f k8s/base/app/

# Access the application
kubectl port-forward svc/telemetry-app 8000:8000
```

### 3. Set Up Monitoring

```bash
# Create monitoring namespace
kubectl apply -f k8s/base/monitoring/namespace.yaml

# Deploy Prometheus
kubectl apply -f k8s/base/monitoring/prometheus/

# Deploy Grafana
kubectl apply -f k8s/base/monitoring/grafana/

# Access Grafana
minikube service -n monitoring grafana
```

## Local Development

### Setup Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=app --cov-report=html

# Run linting
black .
flake8 .
```

### Local Docker Compose

```bash
# Start with Docker Compose
docker-compose up -d

# Stop services
docker-compose down
```

## API Documentation

Once the application is running:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Health Check: http://localhost:8000/health
- Metrics: http://localhost:8000/metrics

## Kubernetes Structure

```
k8s/
├── base/
│   ├── app/          # Application deployment
│   ├── db/           # PostgreSQL database
│   └── monitoring/   # Prometheus & Grafana
└── overlays/         # Environment-specific configs
```

### Key Components

- **Deployment**: Application pods with health checks
- **Service**: Load balancer for application access
- **ConfigMap**: Application configuration
- **Secret**: Database credentials
- **PersistentVolume**: Database storage

## Monitoring Stack

### Prometheus

- Collects metrics from the application
- Exposed at port 9090
- Scrapes `/metrics` endpoint every 15 seconds

### Grafana

- Visualization dashboard
- Default credentials: admin/admin
- Pre-configured dashboards for application metrics

### Metrics Available

- `http_requests_total`: Total HTTP requests by method, endpoint, and status
- `http_request_duration_seconds`: Request latency histogram

## CI/CD Pipeline

The GitHub Actions workflow includes:

1. **Test Job**:

   - Python linting (Black, Flake8)
   - Unit tests with coverage
   - Coverage reporting to Codecov

2. **Build Job**:

   - Docker image build
   - Image caching for faster builds

3. **Deploy Job** (main branch only):
   - Kubernetes deployment
   - Rollout status monitoring
   - Automatic rollback on failure

### Required GitHub Secrets

- `DOCKERHUB_USERNAME`: Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub access token
- `KUBE_CONFIG`: Base64-encoded kubeconfig file

## Database

### Schema

- PostgreSQL with asyncpg driver
- Connection pooling for performance
- Automatic migration support

### Management

```bash
# Connect to database
kubectl exec -it <postgres-pod> -- psql -U telemetryapp_user -d telemetry

# View logs
kubectl logs -f -l app=postgres

# Restart database
kubectl delete pod -l app=postgres
```

## Troubleshooting

### Common Issues

1. **Docker networking on Manjaro**:

   ```bash
   # Use host networking mode
   network_mode: host
   # Stop conflicting PostgreSQL
   sudo systemctl stop postgresql
   ```

2. **Minikube image loading**:

   ```bash
   eval $(minikube docker-env)
   docker build -t telemetry-app:dev .
   minikube image load telemetry-app:dev
   ```

3. **Pod not starting**:
   ```bash
   kubectl describe pod -l app=telemetry-app
   kubectl logs -f -l app=telemetry-app
   ```

### Useful Commands

```bash
# View all resources
kubectl get all

# Watch pods
kubectl get pods -w

# Port forwarding
kubectl port-forward svc/telemetry-app 8000:8000
kubectl port-forward -n monitoring svc/grafana 3000:3000

# Cleanup
cleanup() {
  kubectl delete -f k8s/base/db/
  kubectl delete -f k8s/base/app/
  kubectl delete -f k8s/base/monitoring/
  kubectl delete pvc --all
}
```

## Production Considerations

- Use Kubernetes secrets for sensitive data
- Implement proper authentication and authorization
- Set up resource limits and requests
- Configure persistent storage with proper backup strategy
- Use HTTPS with proper certificates
- Set up monitoring alerts
- Implement proper logging strategy

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is licensed under the MIT License.

---

**Note**: This project uses development-friendly configurations with default passwords. For production deployments, use proper Kubernetes secrets and environment-specific configurations.
