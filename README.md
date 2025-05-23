# FARM_STACK_TODOLIST

A modern full-stack To-Do List app designed to help you organize your tasks effortlessly. This project combines a powerful FastAPI backend with a sleek React frontend, backed by MongoDB for data persistence.

## 🚀 Project Highlights

- Complete CRUD functionality for managing to-do lists and individual tasks  
- Built with asynchronous Python and FastAPI for high performance  
- Responsive React UI for an intuitive user experience  
- Cloud-ready MongoDB Atlas database integration  
- Containerized using Docker for easy deployment and scalability  

## 🛠️ Tools Used

- FastAPI — Backend web framework for building APIs  
- React — Frontend library for building UI  
- MongoDB Atlas — Cloud-hosted NoSQL database to store user and task data  
- Motor — Async MongoDB driver for Python  
- Axios — HTTP client for frontend API requests  
- Docker & Docker Compose — Containerizing frontend, backend, and database  
- NGINX — Reverse proxy setup to route frontend and backend  
- Uvicorn — ASGI server to run FastAPI app  

## 🌐 Tech Stack

- Python  
- JavaScript (React)  
- MongoDB (NoSQL)  

## 💻 Local Setup Instructions

### Prerequisites

- Install Docker and Docker Compose  
- Set up a MongoDB Atlas cluster and obtain your connection URI  

### Steps

1. **Clone this repository:**

    ```bash
    git clone https://github.com/harisreet/FARM_STACK_TODOLIST.git
    cd FARM_STACK_TODOLIST
    ```

2. **Configure environment variables:**

    Create a `.env` file in the project root with your MongoDB connection string:

    ```ini
    MONGODB_URI="your-mongodb-atlas-connection-uri"
    ```

3. **Build and start the application:**

    ```bash
    docker-compose up --build
    ```

4. **Access the app:**

    - Frontend UI: [http://localhost:3000](http://localhost:3000)  
    - API docs: [http://localhost:3001/docs](http://localhost:3001/docs)  

5. **Stop and clean up:**

    ```bash
    docker-compose down --volumes --remove-orphans
    ```
