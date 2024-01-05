"""
    Main
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

try:
    from settings import settings
except ImportError:
    from .settings import settings

app = FastAPI()


class Status(BaseModel):
    """ Status class """
    status: str = "ok"


@app.get(settings.main_url)
async def status():
    """ Status endpoint """
    return Status()


def main():
    """
    Точка входа в приложение
    """
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == '__main__':
    main()
