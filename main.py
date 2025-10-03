from fastapi import FastAPI
from .routers import router
from .db import Base, engine


def create_app() -> FastAPI:
    app = FastAPI(title="Simple API App")
    app.include_router(router)

    @app.on_event("startup")
    def startup_event() -> None:
        Base.metadata.create_all(bind=engine)

    @app.get("/health")
    async def health_check() -> dict:
        return {"status": "ok"}

    return app


app = create_app()

