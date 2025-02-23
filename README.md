# Microservices-Based Application Using Docker

## Introduction
This project demonstrates a **microservices-based architecture** using **Docker and Docker Compose**. It includes a:

1. **Web Service (Flask/Express.js/Spring Boot)** – Provides an API for task management.
2. **Worker Service (Celery/RabbitMQ/Redis)** – Handles asynchronous task processing.
3. **Database Service (PostgreSQL/MySQL/MongoDB)** – Stores task details.

## Features
- Containerized services using **Docker**.
- Service orchestration with **Docker Compose**.
- Communication between web, worker, and database services.
- Data persistence for task management.

## Setup and Execution

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/microservices-docker.git
cd microservices-docker
```

### 2. Build and Start the Containers
```bash
docker-compose up --build -d
```

### 3. Verify Running Containers
```bash
docker ps
```

### 4. Test API Endpoints
#### Check Web Service
```bash
curl http://localhost:5000/
```
Expected Output:
```json
{"message": "Microservices App Running!"}
```

#### Add a Task
```bash
curl http://localhost:5000/add_task
```
Expected Output:
```json
{"task_id": "some-task-id", "status": "Task Added"}
```

### 5. Verify Worker Service Logs
```bash
docker logs worker_service
```

### 6. Connect to the Database and Verify Tables
```bash
sudo docker exec -it devopsass2_mongodb_1 mongosh
use taskdb
show collections
db.tasks.find()
```
## Stopping and Cleaning Up Containers
```bash
docker-compose down -v
```

## Repository Structure
```
task-manager/
├── docker-compose.yml
├── .env
├── web/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   └── templates/
│       └── index.html
├── worker/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── worker.py
└── mongodb/
    └── init-mongo.js
```
---
This project showcases a **fully containerized microservices application**, demonstrating **service orchestration, asynchronous task processing, and data persistence** using Docker. 🚀
