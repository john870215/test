from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers import vhs_short_v1
from sql_app.database import create_table


@asynccontextmanager
async def register_init(app: FastAPI):
    """
    :return:
    """

    await create_table()

    yield


app = FastAPI(
    lifespan=register_init,
)

app.include_router(vhs_short_v1.router, prefix="/api/v1.0")

@app.get("/")
async def index():
    return {"message": "success"}
