from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello_world():
    return {"Hello": "World"}


@app.get('/query')
async def query_name(name: str):
    return {"name": name}
