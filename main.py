from fastapi import FastAPI

app = FastAPI(title="Novotny 1 Vote")

@app.get("/")
def home():
    return {"message": "Welcome to Novotny 1 Vote!"}

@app.get("/test")
def test():
    return {"status": "App is running fine!"}

