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
