from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}