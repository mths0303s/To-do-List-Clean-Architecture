from domain.repositories.tarefa_repositorio_interface import ITarefaRepositorio

class AtualizarTituloTarefa:
    def __init__(self, repositorio: ITarefaRepositorio):
        self.repositorio = repositorio

    def executar(self, id: str, novo_titulo: str):
        tarefa = self.repositorio.buscar_por_id(id)
        tarefa.atualizar_titulo(novo_titulo)
        self.repositorio.atualizar(tarefa)