from typing import Annotated

from fastapi import Body, FastAPI, Field
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str = Field(examples = "")
    description: str | None = Field(default="null")
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, )


@app.put("/items/{item_id}")
async def update_item(
    
):
    results = {"item_id": item_id, "item": item}
    return results