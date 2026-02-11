import time
from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add processing time to every response."""
    start_time = time.perf_counter()
    print(f"Starting request processing for path: {request.url.path},{request.method}")

    response = await call_next(request)  # Pass to route
    
    print(f"Finished request processing {response.status_code}")
    process_time = time.perf_counter() - start_time
    print(f"Processing time: {process_time:.4f} seconds")
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}