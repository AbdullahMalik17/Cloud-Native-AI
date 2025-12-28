# FastAPI Hello World

A simple FastAPI application demonstrating the basics of building REST APIs with Python.

## Overview

This is a minimal FastAPI application that serves as an introduction to modern Python web development. It demonstrates:
- Basic FastAPI application structure
- Route definitions and path operations
- Async endpoint handlers
- Automatic API documentation
- Health check endpoint pattern

## Prerequisites

- Python 3.11 or higher
- `uv` package manager (recommended) or `pip`

## Project Structure

```
hello-fastapi/
├── main.py              # Main application file
├── pyproject.toml       # Project configuration
├── .python-version      # Python version specification
├── .gitignore          # Git ignore rules
├── .venv/              # Virtual environment (created after setup)
└── README.md           # This file
```

## Installation

### Option 1: Using UV (Recommended)

```bash
# Navigate to project directory
cd hello-fastapi

# Create virtual environment manually (if not exists)
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install "fastapi[standard]"
```

### Option 2: Using pip

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate

# Install FastAPI with all standard dependencies
pip install "fastapi[standard]"
```

## Running the Application

### Development Mode (with auto-reload)

```bash
# Make sure virtual environment is activated
uvicorn main:app --reload
```

The application will start on http://127.0.0.1:8000

**Note:** The `--reload` flag enables auto-reload, which automatically restarts the server when you make code changes. This is useful during development.

### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### Root Endpoint
- **URL:** `GET /`
- **Description:** Returns a Hello World message
- **Response:**
  ```json
  {
    "message": "Hello World"
  }
  ```

### Health Check Endpoint
- **URL:** `GET /health`
- **Description:** Returns the application health status
- **Response:**
  ```json
  {
    "status": "healthy"
  }
  ```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation:

### Swagger UI (OpenAPI)
Visit http://127.0.0.1:8000/docs

- Interactive interface to test endpoints
- Automatic request/response examples
- Built-in API testing capabilities

### ReDoc
Visit http://127.0.0.1:8000/redoc

- Alternative documentation interface
- Clean, three-panel design
- Better for reading and sharing

## Testing the API

### Using cURL

```bash
# Test root endpoint
curl http://127.0.0.1:8000/

# Test health endpoint
curl http://127.0.0.1:8000/health
```

### Using Browser

Simply open these URLs in your browser:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health

### Using HTTPie (if installed)

```bash
http GET http://127.0.0.1:8000/
http GET http://127.0.0.1:8000/health
```

## Code Explanation

### main.py Breakdown

```python
from fastapi import FastAPI

# Create FastAPI application instance
app = FastAPI()

# Define root endpoint with GET method
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Define health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

**Key Concepts:**

1. **FastAPI Instance:** `app = FastAPI()` creates the application
2. **Decorators:** `@app.get("/")` defines a route that responds to GET requests
3. **Async Functions:** `async def` allows asynchronous request handling
4. **Automatic JSON:** Return dictionaries are automatically converted to JSON
5. **Type Safety:** FastAPI uses Python type hints for validation and documentation

## Learning Path

### 1. Basic Concepts (Current)
- ✅ Creating a FastAPI application
- ✅ Defining routes and endpoints
- ✅ Returning JSON responses

### 2. Next Steps - Request Handling
Learn about:
- Path parameters: `/items/{item_id}`
- Query parameters: `/items?skip=0&limit=10`
- Request bodies with Pydantic models
- Request validation

**Example to try:**
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

### 3. Advanced Topics
- Database integration (SQLAlchemy)
- Authentication and authorization (JWT, OAuth2)
- Dependency injection
- Middleware and CORS
- Background tasks
- File uploads
- WebSockets

### 4. Production Deployment
- Docker containerization
- Environment configuration
- Logging and monitoring
- Testing with pytest
- CI/CD pipelines

## Common Issues and Solutions

### Issue: Module not found
**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
.venv\Scripts\activate
pip install "fastapi[standard]"
```

### Issue: Port already in use
**Solution:** Use a different port:
```bash
uvicorn main:app --reload --port 8001
```

### Issue: Import errors
**Solution:** Run uvicorn from the project root directory where `main.py` exists.

## Resources

### Official Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

### FastAPI-Mastery Skill References
This project uses the fastapi-mastery skill. For more advanced topics, refer to:
- `.claude/skills/fastapi-mastery/references/01-beginner.md` - Basic patterns
- `.claude/skills/fastapi-mastery/references/02-intermediate.md` - Auth, databases, middleware
- `.claude/skills/fastapi-mastery/references/03-advanced.md` - WebSockets, testing, deployment

### Video Tutorials
- [FastAPI Official Tutorial](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- [FastAPI Crash Course](https://www.youtube.com/results?search_query=fastapi+tutorial)

## Extending This Application

Try adding these features to practice:

1. **Add More Endpoints**
   ```python
   @app.get("/about")
   async def about():
       return {"app": "FastAPI Hello World", "version": "1.0"}
   ```

2. **Add Path Parameters**
   ```python
   @app.get("/greet/{name}")
   async def greet(name: str):
       return {"message": f"Hello, {name}!"}
   ```

3. **Add Query Parameters**
   ```python
   @app.get("/search")
   async def search(q: str, limit: int = 10):
       return {"query": q, "limit": limit}
   ```

4. **Use Pydantic Models**
   ```python
   from pydantic import BaseModel

   class Item(BaseModel):
       name: str
       price: float

   @app.post("/items")
   async def create_item(item: Item):
       return {"created": item}
   ```

## Contributing

This is a learning project. Feel free to experiment and modify the code to understand FastAPI better.

## License

This project is for educational purposes as part of the Panaversity AI 400 Course.

## Course Context

**Panaversity AI 400 - Cloud-Native AI Development**

This Hello World application is the first step in learning cloud-native AI development with:
- Docker
- Dapr
- Multi-Model Agents
- Kubernetes

---

**Happy Learning! 🚀**

For questions or issues, refer to the FastAPI documentation or the fastapi-mastery skill references.
