
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     test: float | None = None

# class ModelName(str, Enum):
#     onet = "1net"
#     tnet = "2net"
#     thnet = "3net"

# # fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}]
# app = FastAPI()

# @app.post("/sat/1")
# async def datahere(item: Item):
#     return item

# @app.get("/sat/1")
# def sat_test():
#     return {"message: ": "testest!"}

# @app.get("/")
# def read_root():
#     return {"message: ": "Hello, from satellite1!"}

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.onet:
#         return{"model_name": model_name, "message": "yeeters thats 1net"}
#     if model_name.value == "2net":
#         return{"model_name": model_name.value, "message": "dang dawg 2net"}

#     return {"model_name": model_name, "message: ": "threenizzle"}


# ## /items/123?q=pineapples&short=True
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if short:
#         item.update({"description": "weeee"})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# ## /items/123?q=hello
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return{"item_id": item_id}

# @app.get("/items/")
# async def read_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# def read_id(item_id: float):
#     return {"item id": item_id}


# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
