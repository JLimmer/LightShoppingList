from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Light Shopping List App!"}

@app.get("/items/")
def read_items():
    return {"items": []}

@app.post("/items/")
def add_item(item: str):
    return {"message": f"Item '{item}' added to the shopping list."}

@app.delete("/items/")
def delete_item(item: str):
    return {"message": f"Item '{item}' removed from the shopping list."}