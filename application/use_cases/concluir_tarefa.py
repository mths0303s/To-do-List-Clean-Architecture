from domain.repositories.tarefa_repositorio_interface import ITarefaRepositorio


class ConcluirTarefa:
    def __init__(self, repositorio: ITarefaRepositorio):
        self.repositorio = repositorio

    def executar(self, id: str):
        tarefa = self.repositorio.buscar_por_id(id)
        tarefa.alternar_status_conclusao()
        self.repositorio.atualizar(tarefa)
