# Production-Grade ML Inference Platform (CI/CD + Kubernetes)

This repository contains a production-style Machine Learning inference platform, built end-to-end using modern MLOps practices.
The project demonstrates how to take a trained ML model from local development → CI/CD → container registry → Kubernetes deployment.

## 🚀 Overview

The system exposes a REST API for real-time ML predictions and is designed with production readiness in mind:

- **Model training and serialization**
- **Stateless inference API**
- **Production-grade WSGI server**
- **Dockerized runtime**
- **Automated CI with testing**
- **Secure image publishing**
- **Kubernetes deployment and lifecycle management**

## 📊 Architecture

```mermaid
flowchart TD
    subgraph "Development Phase"
        A[ML Model<br/>scikit-learn + joblib]
        B[Flask REST API]
        C[Gunicorn WSGI Server]
        D[Docker Container]
    end
    
    subgraph "CI/CD Pipeline"
        E[GitHub Actions]
        F[Automated Tests<br/>pytest]
        G[Docker Image Build]
    end
    
    subgraph "Registry & Orchestration"
        H[Docker Hub Registry]
        I[Kubernetes Cluster]
        J[Deployment<br/>ReplicaSet + Pods]
        K[Service<br/>NodePort/LoadBalancer]
    end
    
    subgraph "Production"
        L[Live Inference API<br/>POST /predict]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style L fill:#9f9,stroke:#333,stroke-width:2px
    style E fill:#ff9,stroke:#333,stroke-width:2px
    style I fill:#9cf,stroke:#333,stroke-width:2px
🛠️ Tech Stack
Category	Technologies
Language	Python
ML	scikit-learn, joblib
API	Flask
Production Server	Gunicorn
Containerization	Docker
CI/CD	GitHub Actions
Registry	Docker Hub
Orchestration	Kubernetes (minikube)
📁 Project Structure
text
ml-model-ci-cd-kubernetes/
├── app/
│   └── app.py              # Flask inference API
├── model/
│   └── model.joblib        # Trained ML model
├── tests/
│   └── test_api.py         # API tests (pytest)
├── k8s/
│   ├── deployment.yaml     # Kubernetes Deployment
│   └── service.yaml        # Kubernetes Service
├── Dockerfile
├── requirements.txt
├── .github/workflows/ci.yml
└── README.md
🔮 Model & API
Model
Algorithm: Logistic Regression

Dataset: Iris dataset

Serialization: joblib

Best Practice: Model loaded once at startup

API Endpoints
Health Check
http
GET /
Response:

text
OK
Prediction
http
POST /predict
Content-Type: application/json
Request body:

json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
Response:

json
{
  "prediction": 0
}
🐳 Docker
The application is containerized using a slim Python base image and runs with Gunicorn for production-grade request handling.

Build locally:

bash
docker build -t ml-model .
Run locally:

bash
docker run -p 5000:5000 ml-model
🔁 CI/CD Pipeline
Implemented using GitHub Actions. On every push to main, the pipeline:

Installs dependencies

Builds the Docker image

Starts the container

Runs pytest API tests against the live service

Pushes the tested image to Docker Hub

This ensures only validated images are published.

📦 Docker Hub
The image is published automatically by CI:

bash
kiranrajsg/ml-model:latest
Publicly pullable and Kubernetes-ready.

☸️ Kubernetes Deployment (Local)
Deployed using minikube.

Apply manifests:

bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
Access service (local):

bash
kubectl port-forward svc/ml-model-service 5000:5000
Then call the API at:

text
http://localhost:5000
Clean teardown:

bash
kubectl delete deployment ml-model
kubectl delete service ml-model-service
✅ Key Engineering Practices Demonstrated
Production-safe model serving

Automated CI with runtime validation

API contract testing

Secure secret handling

Artifact lifecycle management

Kubernetes deployment fundamentals

Declarative infrastructure and clean teardown

🎯 Intended Audience
This project is intended for:

ML Engineers transitioning to MLOps

Backend engineers working with ML systems

Recruiters evaluating production readiness

Interview discussions on real-world ML deployment

📌 Future Enhancements (Optional)
Liveness & readiness probes

Resource limits and autoscaling

Versioned image rollouts (v1 → v2)

Monitoring (Prometheus metrics)

Authentication & authorization

👤 Author
Kiranraj S G
Machine Learning & ECE Graduate
📧 kiranrajganesan16@gmail.com
