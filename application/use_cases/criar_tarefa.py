from domain.entities.tarefa import Tarefa
from domain.repositories.tarefa_repositorio_interface import ITarefaRepositorio


class CriarTarefa:
    def __init__(self, repositorio: ITarefaRepositorio):
        self.repositorio = repositorio

    def executar(self, titulo: str):
        nova_tarefa = Tarefa(titulo=titulo)
        self.repositorio.salvar(nova_tarefa)
        return nova_tarefa
