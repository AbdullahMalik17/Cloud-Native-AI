from fastapi import FastAPI, Depends

app = FastAPI(title="Dependency Injection Example")

def configure_database():
    return {"db_url": "sqlite:///:memory:"}

@app.get("/items/{item_id}")
def task(item_id: int,config: dict = Depends(configure_database)):
    # config=configure_database()
    return {"item_id": item_id,"db_url":config["db_url"]}