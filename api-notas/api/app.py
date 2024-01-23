from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.database import create_tables
from api.public import api as nota_api


def create_app():
    app = FastAPI(
        title="Notas de Usuario",
        version="1.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    def on_starup():
        create_tables()

    app.include_router(nota_api)

    return app