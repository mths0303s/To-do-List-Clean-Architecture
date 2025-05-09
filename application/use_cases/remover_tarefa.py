from domain.repositories.tarefa_repositorio_interface import ITarefaRepositorio


class RemoverTarefa:
    def __init__(self, repositorio: ITarefaRepositorio):
        self.repositorio = repositorio

    def executar(self, id: str):
        self.repositorio.remover(id)
