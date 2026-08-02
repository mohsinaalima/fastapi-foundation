from fastapi
import FastAPI

app = FastAPI(
    title="Chai Point menu API",
    description="Read only menu API for kisko displays and mobile apps",
)

@app.get("/")
def root():
    return {"message": "Welcome to Chai Point menu API!"}