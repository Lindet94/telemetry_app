# Lesson 010: Introduction to Kubernetes Deployment

## Objective
Understand the core concepts of Kubernetes and prepare your local environment for deployment.

## Prerequisites
- Docker and Docker Compose (already set up from previous lessons)
- Basic understanding of containerization

## Core Concepts

### 1. What is Kubernetes?
Kubernetes (K8s) is an open-source platform for automating deployment, scaling, and operations of application containers across clusters of hosts.

### 2. Key Components
- **Pods**: The smallest deployable units in Kubernetes
- **Deployments**: Manage the desired state of your application
- **Services**: Expose your application to the network
- **ConfigMaps & Secrets**: Manage configuration and sensitive data
- **PersistentVolumes**: Handle persistent storage

## Exercise 1: Install kubectl

1. Install `kubectl`, the Kubernetes command-line tool:
   - **Linux**:
     ```bash
     sudo apt-get update && sudo apt-get install -y kubectl
     ```
   - **macOS**:
     ```bash
     brew install kubectl
     ```
   - **Windows**:
     ```bash
     choco install kubernetes-cli
     ```

2. Verify the installation:
   ```bash
   kubectl version --client
   ```

## Exercise 2: Set Up Minikube (Local Kubernetes)

1. Install Minikube:
   - **Linux**:
     ```bash
     curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
     sudo install minikube-linux-amd64 /usr/local/bin/minikube
     ```
   - **macOS**:
     ```bash
     brew install minikube
     ```
   - **Windows**:
     ```bash
     choco install minikube
     ```

2. Start Minikube:
   ```bash
   minikube start --driver=docker
   ```

3. Verify your cluster is running:
   ```bash
   kubectl get nodes
   ```

## Exercise 3: Explore Kubernetes Dashboard

1. Start the Kubernetes dashboard:
   ```bash
   minikube dashboard
   ```

2. This will open the dashboard in your default web browser. Explore the different sections.

## Knowledge Check

1. What is the purpose of a Kubernetes Pod?
2. How does a Deployment differ from a Pod?
3. What command would you use to see all running pods in your cluster?

## Next Steps
In the next lesson, we'll create Kubernetes manifests for our application and deploy it to our local Minikube cluster.

## Additional Resources
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
