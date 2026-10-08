# Containerized Flask Application

## Project Objective

This project demonstrates how to containerize a Python Flask application using Docker and deploy it on Amazon ECS using Amazon ECR. The application is publicly accessible through an ECS endpoint.

---

## AWS Services Used

- Amazon ECS (Elastic Container Service)
- Amazon ECR (Elastic Container Registry)
- AWS IAM
- Amazon CloudWatch
- Docker

---

## Architecture / Workflow

Flask Application
↓
Docker Image
↓
Amazon ECR
↓
Amazon ECS Service
↓
Public Application URL

---

## Implementation Steps

### Step 1
Created a simple Flask web application using Python.

### Step 2
Created Dockerfile and requirements.txt.

### Step 3
Built Docker image.

```bash
docker build -t containerized-flask-app .
```

### Step 4
Created Amazon ECR repository.

### Step 5
Pushed Docker image to Amazon ECR.

### Step 6
Created ECS Express Service.

### Step 7
Deployed application successfully.

---

## Screenshots

- Docker Build
- ECR Repository
- ECS Service Overview
- Running Task
- Application URL Output

---

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:

http://127.0.0.1:5000

---

## Deployment

1. Build Docker image
2. Push image to Amazon ECR
3. Create ECS Service
4. Deploy container
5. Access public URL

---

## Key Learnings

- Docker Containerization
- Amazon ECR Image Management
- Amazon ECS Deployment
- CloudWatch Monitoring
- IAM Role Configuration
- Troubleshooting ECS Deployment Issues

---

## Project Author

Punam More

Bachelor of Computer Science

AWS Cloud Computing & Python Learner