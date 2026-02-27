from fastapi import FastAPI

app = FastAPI()

# Example from FastAPI documentation.
# this is just a placeholder for a api to be exposed via tor hidden service.

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}