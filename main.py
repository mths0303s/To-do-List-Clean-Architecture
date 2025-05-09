from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from interface.controllers.tarefa_controller import router as tarefa_router

app = FastAPI()

# Monta a pasta de arquivos estáticos (Bulma, JS, imagens etc.)
app.mount("/static", StaticFiles(directory="interface/static"), name="static")
# Inclui as rotas de tarefa
app.include_router(tarefa_router)
