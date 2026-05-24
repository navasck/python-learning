from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Python API Working"
    }


@app.get("/hello")
def hello():
    return {
        "message": "Hello Abdul"
    }