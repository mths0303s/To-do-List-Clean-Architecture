from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from application.use_cases.listar_tarefas import ListarTarefas
from application.use_cases.criar_tarefa import CriarTarefa
from application.use_cases.concluir_tarefa import ConcluirTarefa
from application.use_cases.remover_tarefa import RemoverTarefa
from infra.database.tarefa_repositorio_sqlite import TarefaRepositorioSQLite
from infra.database.tarefa_repositorio_cassandra import TarefaRepositorioCassandra


router = APIRouter()
templates = Jinja2Templates(directory="interface/templates")

# Instanciando os casos de uso com o repositório real

#repositorio = TarefaRepositorioSQLite() 
repositorio = TarefaRepositorioCassandra()
listar_tarefas = ListarTarefas(repositorio)
criar_tarefa = CriarTarefa(repositorio)
concluir_tarefa = ConcluirTarefa(repositorio)
remover_tarefa = RemoverTarefa(repositorio)


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    tarefas = listar_tarefas.executar()
    return templates.TemplateResponse("index.html", {"request": request, "tarefas": tarefas})


@router.post("/add", response_class=HTMLResponse)
async def criar(request: Request, titulo: str = Form(...)):
    criar_tarefa.executar(titulo)
    tarefas = listar_tarefas.executar()
    return templates.TemplateResponse("partials/list.html", {
        "request": request,
        "tarefas": tarefas
    })


@router.patch("/tarefas/{id}/concluir", response_class=HTMLResponse)
async def concluir(request: Request, id: str):
    concluir_tarefa.executar(id)
    tarefas = listar_tarefas.executar()
    return templates.TemplateResponse("partials/list.html", {
        "request": request,
        "tarefas": tarefas
    })

@router.delete("/tarefas/{id}/remover", response_class=HTMLResponse)
async def remover(request: Request, id: str):
    remover_tarefa.executar(id)
    tarefas = listar_tarefas.executar()
    return templates.TemplateResponse("partials/list.html", {
        "request": request,
        "tarefas": tarefas
    })
