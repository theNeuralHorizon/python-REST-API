from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{userid}")
async def root():
    return {"message": "Hello World"}