import sqlite3
from typing import List, Optional
from domain.entities.tarefa import Tarefa
from domain.repositories.tarefa_repositorio_interface import ITarefaRepositorio


class TarefaRepositorioSQLite(ITarefaRepositorio):
    def __init__(self, db_path: str = "tarefas.db"):
        self.conn = sqlite3.connect(db_path)
        self._criar_tabela()

    def _criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                concluida INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def salvar(self, tarefa: Tarefa) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tarefas (id, titulo, concluida) VALUES (?, ?, ?)",
            (tarefa.id, tarefa.titulo, int(tarefa.concluida))
        )
        self.conn.commit()

    def listar(self) -> List[Tarefa]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, titulo, concluida FROM tarefas")
        linhas = cursor.fetchall()
        return [Tarefa(id=id_, titulo=titulo, concluida=bool(concluida)) for id_, titulo, concluida in linhas]

    def remover(self, id: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
        self.conn.commit()

    def atualizar(self, tarefa: Tarefa) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE tarefas SET titulo = ?, concluida = ? WHERE id = ?",
            (tarefa.titulo, int(tarefa.concluida), tarefa.id)
        )
        self.conn.commit()

    def buscar_por_id(self, id: str) -> Optional[Tarefa]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, titulo, concluida FROM tarefas WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Tarefa(id=linha[0], titulo=linha[1], concluida=bool(linha[2]))
        return None
