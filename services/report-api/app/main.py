from fastapi import FastAPI

app = FastAPI(title="MediReport report-api")


@app.get("/health")
def health():
    return {"status": "ok"}
