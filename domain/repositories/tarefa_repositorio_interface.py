from abc import ABC, abstractmethod
from typing import List
from domain.entities.tarefa import Tarefa
from typing import Optional


class ITarefaRepositorio(ABC):
    @abstractmethod
    def salvar(self, tarefa: Tarefa) -> None:
        pass

    @abstractmethod
    def listar(self) -> List[Tarefa]:
        pass

    @abstractmethod
    def buscar_por_id(self, id: str) -> Optional[Tarefa]:
        pass


    @abstractmethod
    def remover(self, id: str) -> None:
        pass

    @abstractmethod
    def atualizar(self, tarefa: Tarefa) -> None:
        pass
    