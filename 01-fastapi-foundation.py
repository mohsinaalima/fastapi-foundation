from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Swiggy Order Service",
    description="This is a sample FastAPI application for Swiggy Order Service.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get("/")
def root():
    """Root endpoint - Health check"""
    return {
        "message": "Welcome to the Swiggy Order Service API!",
        "status": "Healthy"
    }


@app.get("/about")
def about():
    """About endpoint - Provides information about the API"""
    return {
        "name": "Swiggy Order Service",
        "version": "1.0.0",
        "description": "This is a sample FastAPI application for Swiggy Order Service.",
        "author": "Mohsina Alima",
        "contact": {
            "email": "mohsinaalima2006@gmail.com",
            "website": "https://github.com/mohsinaalima"
        }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)