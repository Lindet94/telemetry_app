# Lesson 011: Creating Kubernetes Manifests

## Objective
Learn how to create Kubernetes manifests to deploy our application and database.

## Prerequisites
- Completed Lesson 010 (Kubernetes Introduction)
- Minikube running locally
- `kubectl` installed and configured

## Exercise 1: Project Structure

Let's start by creating a directory structure for our Kubernetes manifests:

```bash
mkdir -p k8s/{base,overlays} k8s/base/{app,db}
```

## Exercise 2: Database Deployment

Create a file at `k8s/base/db/deployment.yaml` with the following content:

```yaml
# k8s/base/db/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        env:
        - name: POSTGRES_USER
          value: telemetryapp_user
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secrets
              key: password
        - name: POSTGRES_DB
          value: telemetry
        ports:
        - containerPort: 5432
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
      volumes:
      - name: postgres-storage
        persistentVolumeClaim:
          claimName: postgres-pv-claim
```

## Exercise 3: Database Persistent Volume

Create a file at `k8s/base/db/volume.yaml`:

```yaml
# k8s/base/db/volume.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-pv-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

## Exercise 4: Database Secrets

Create a file at `k8s/base/db/secrets.yaml`:

```yaml
# k8s/base/db/secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: postgres-secrets
type: Opaque
data:
  password: cG9zdGdyZXM=  # base64 encoded "postgres"
```

## Exercise 5: Application Deployment

Create a file at `k8s/base/app/deployment.yaml`:

```yaml
# k8s/base/app/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: telemetry-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: telemetry-app
  template:
    metadata:
      labels:
        app: telemetry-app
    spec:
      containers:
      - name: telemetry-app
        image: telemetry-app:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          value: "postgresql://telemetryapp_user:$(POSTGRES_PASSWORD)@postgres:5432/telemetry"
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secrets
              key: password
```

## Exercise 6: Application Service

Create a file at `k8s/base/app/service.yaml`:

```yaml
# k8s/base/app/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: telemetry-app
spec:
  selector:
    app: telemetry-app
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
  type: NodePort
```

## Exercise 7: Database Service

Create a file at `k8s/base/db/service.yaml`:

```yaml
# k8s/base/db/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  selector:
    app: postgres
  ports:
    - protocol: TCP
      port: 5432
      targetPort: 5432
  type: ClusterIP
```

## Exercise 8: Apply the Manifests

1. Apply the database resources:
   ```bash
   kubectl apply -f k8s/base/db/
   ```

2. Apply the application resources:
   ```bash
   kubectl apply -f k8s/base/app/
   ```

3. Check the status of your pods:
   ```bash
   kubectl get pods --watch
   ```

## Knowledge Check

1. Why do we need a separate Service for the database?
2. What's the purpose of the `persistentVolumeClaim` in the database deployment?
3. How would you scale the application to 3 replicas?

## Next Steps
In the next lesson, we'll learn how to:
- Set up environment-specific configurations
- Use Kustomize for managing different environments
- Set up Ingress for external access

## Additional Resources
- [Kubernetes Documentation: Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes Documentation: Services](https://kubernetes.io/docs/concepts/services-networking/service/)
