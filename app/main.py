from fastapi import FastAPI

app = FastAPI(
    title="AxiomCheck API",
    description="Backend API for checking technical integrity of research papers.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AxiomCheck API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "AxiomCheck API"
    }