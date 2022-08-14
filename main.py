from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/home")
def hello(name=None):
    if name is not None:
        return f"Hello {name}"
    else:
        return "Hello stranger"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)