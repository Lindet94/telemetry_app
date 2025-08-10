📄 Project Description – Expense Tracker API (Cloud-Native)

Overview:
This project is a personal Expense Tracker API designed to help me learn and practice cloud-native development, GitOps, and infrastructure-as-code using Terraform and Kubernetes. The API allows logging and retrieving personal expenses and will be deployed using a modern DevOps toolchain with full observability and CI/CD automation.

🎯 Purpose

Track personal expenses by amount, category, vendor, and timestamp
Build a practical backend app and deploy it in Kubernetes
Learn Terraform, GitHub Actions, ArgoCD, and Prometheus/Grafana
Practice real-world infrastructure setup with GitOps deployment workflows

🧱 Tech Stack

Layer	            Tech Used
Backend	            Python (FastAPI)
Database	        PostgreSQL
Infrastructure	    Kubernetes (Minikube → AKS or GKE)
IaC	                Terraform
GitOps	            ArgoCD
CI/CD	            GitHub Actions
Observability	    Prometheus + Grafana
Secrets (Optional)	Kubernetes Secrets / Azure Key Vault

🔧 Core Features

POST /expenses: Add a new expense (amount, vendor, category, timestamp)
GET /expenses: Retrieve expense history
Metrics exposed for Prometheus (e.g., request counts, errors, spending stats)
Grafana dashboard showing spending trends over time

📁 Project Structure

expense-tracker/
├── app/                      # Backend source code
├── infra/                    # Terraform configuration for cloud resources
├── manifests/                # K8s manifests (or ArgoCD-compatible GitOps repo)
├── .github/workflows/        # CI/CD pipelines
├── Dockerfile
└── README.md

🚀 Stretch Goals

- Add user authentication or API tokens
- Export data to CSV or cloud storage
- Setup automated alerts (e.g., budget threshold warnings)
- Add a minimal web frontend (optional)

