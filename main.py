from fastapi import FastAPI

app = FastAPI(
    title="pincode lookup API",
    description="Auto fill city and state from india pincode during checkout ",
)

@app.get("/")
def root():
    return {"message": "Welcome to the pincode lookup API!"}


