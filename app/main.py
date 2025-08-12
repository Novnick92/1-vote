from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routers import ballot

app = FastAPI(title="Novotny 1 Vote")

# Templates & static
app.state.templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Routers
app.include_router(ballot.router)
