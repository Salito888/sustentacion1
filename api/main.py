from fastapi import FastAPI
from.controller.flor_controller import router as flor_router

app = FastAPI()

app.include_router(flor_router, prefix="/api")
