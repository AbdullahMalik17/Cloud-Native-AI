# FastAPI Middleware

## What is Middleware?

Middleware is a function that runs **before and after** every request-response cycle. It sits between the client and your route handlers, intercepting both the incoming request and the outgoing response.

```
Client  -->  Middleware (before)  -->  Route Handler
Client  <--  Middleware (after)   <--  Route Handler
```

A middleware function:

1. Receives the incoming `Request`.
2. Can modify the request or run any code before the route handler executes.
3. Calls `call_next(request)` to pass control to the next layer (another middleware or the route handler).
4. Receives the `Response` returned by the route handler.
5. Can modify the response or run any code after the route handler executes.
6. Returns the `Response`.

## Basic Example

```python
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

## How Multiple Middleware Works (The Stack)

When you register multiple middlewares, FastAPI wraps them around your application like layers of an onion. Each new middleware added becomes the **outermost layer**.

### Registration Order vs Execution Order

```python
app.add_middleware(MiddlewareA)   # Added first  -> innermost
app.add_middleware(MiddlewareB)   # Added second -> outermost
```

Or equivalently with decorators:

```python
@app.middleware("http")
async def middleware_a(request, call_next):  # Registered first -> innermost
    ...

@app.middleware("http")
async def middleware_b(request, call_next):  # Registered second -> outermost
    ...
```

### Execution Flow

The **last middleware added** runs **first** on the request path and **last** on the response path:

```
               REQUEST                          RESPONSE
              ─────────►                       ◄─────────

Client ──► MiddlewareB ──► MiddlewareA ──► Route ──► MiddlewareA ──► MiddlewareB ──► Client
           (outermost)     (innermost)               (innermost)     (outermost)
```

| Phase      | Execution Order                          |
|------------|------------------------------------------|
| **Request**  | MiddlewareB → MiddlewareA → Route Handler |
| **Response** | Route Handler → MiddlewareA → MiddlewareB |

### Concrete Example

```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def middleware_a(request: Request, call_next):
    print("A: before request")       # Step 2
    response = await call_next(request)
    print("A: after response")       # Step 4
    return response

@app.middleware("http")
async def middleware_b(request: Request, call_next):
    print("B: before request")       # Step 1
    response = await call_next(request)
    print("B: after response")       # Step 5
    return response

@app.get("/")
async def root():
    print("Route handler executed")   # Step 3
    return {"message": "Hello World"}
```

**Console output for a request to `/`:**

```
B: before request          # 1. Outermost middleware runs first
A: before request          # 2. Inner middleware runs next
Route handler executed     # 3. Route handler processes the request
A: after response          # 4. Inner middleware handles response first
B: after response          # 5. Outermost middleware handles response last
```

### Why Does This Matter?

The stack order is important when middlewares depend on each other. For example:

- An **authentication middleware** should run before a **logging middleware** that logs the authenticated user. Since the last-added middleware runs first on requests, you would add the logging middleware first and the auth middleware second.
- A **CORS middleware** typically needs to be the outermost layer to handle preflight requests before anything else.

### Key Takeaways

1. **Each middleware wraps the application**, forming a stack (like nested layers).
2. **Last added = outermost** — it runs first on requests, last on responses.
3. **First added = innermost** — it runs last on requests, first on responses.
4. The `call_next` function passes control to the next inner layer.
5. Every middleware sees **every request** — there is no route-based filtering at the middleware level.

## Running This Project

```bash
# Install dependencies
uv sync

# Start the development server
uvicorn main:app --reload
```

## References

- [FastAPI Middleware Documentation](https://fastapi.tiangolo.com/tutorial/middleware/)
- [Starlette Middleware](https://www.starlette.io/middleware/)
