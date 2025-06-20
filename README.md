# Task Management API

A production-ready FastAPI application for comprehensive task management with JWT authentication, PostgreSQL, Docker, and more.

## 1. Setup
```bash
# Clone or create project directory
mkdir task_management_api
cd task_management_api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your database credentials
```

## 2. Database Setup
```bash
# Using Docker Compose (recommended)
docker-compose up -d db

# Or install PostgreSQL locally and create database
createdb taskdb
```

## 3. Run the Application
```bash
# Development mode
uvicorn app.main:app --reload

# Or using Docker Compose
docker-compose up
```

## 4. API Endpoints

**Authentication:**
- `POST /api/v1/auth/login` - Login and get access token

**Users:**
- `POST /api/v1/users/` - Register new user
- `GET /api/v1/users/me` - Get current user info
- `PUT /api/v1/users/me` - Update current user

**Tasks:**
- `GET /api/v1/tasks/` - Get all tasks for current user
- `POST /api/v1/tasks/` - Create new task
- `GET /api/v1/tasks/{task_id}` - Get specific task
- `PUT /api/v1/tasks/{task_id}` - Update task
- `DELETE /api/v1/tasks/{task_id}` - Delete task

## 5. Access Swagger Documentation
Visit `http://localhost:8000/docs` for interactive API documentation.

## Features

✅ **Complete CRUD Operations** for tasks and users

✅ **JWT Authentication** with secure password hashing

✅ **PostgreSQL Integration** with SQLAlchemy ORM

✅ **Proper Project Structure** following FastAPI best practices

✅ **Automatic Swagger Documentation**

✅ **Docker Support** for easy deployment

✅ **Input Validation** with Pydantic models

✅ **Error Handling** and proper HTTP status codes

✅ **CORS Support** for frontend integration

✅ **Database Relationships** (User -> Tasks)

✅ **Query Parameters** for pagination

✅ **Security Dependencies** for protected routes

This is a production-ready FastAPI application with comprehensive features for task management!
