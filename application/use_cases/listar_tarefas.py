from domain.repositories.tarefa_repositorio_interface import ITarefaRepositorio


class ListarTarefas:
    def __init__(self, repositorio: ITarefaRepositorio):
        self.repositorio = repositorio

    def executar(self):
        return self.repositorio.listar()