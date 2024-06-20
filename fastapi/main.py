from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # Union - str or None으로 Optional[str]과 동일하다.
    return {"item_id": item_id, "q": str(item_id)}

@app.get("/items/")
# 타입은 명시를 할 수도 있고 하지 않을 수도 있다.
# 명시하지 않으면 다른 프레임워크와 동일하게 문자로 취급된다.
def read_items(item_id: int, q: str):
    return {"item_id": item_id, "q": q}
