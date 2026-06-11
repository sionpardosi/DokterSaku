# TODO Step 6: FastAPI main
from fastapi import FastAPI
app = FastAPI(title="Dokter Saku")
@app.get("/health")
def health(): return {"status": "ok"}
