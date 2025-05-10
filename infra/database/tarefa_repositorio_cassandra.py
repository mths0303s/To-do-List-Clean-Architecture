from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from domain.entities.tarefa import Tarefa
from domain.repositories.tarefa_repositorio_interface import ITarefaRepositorio
from typing import List


class TarefaRepositorioCassandra(ITarefaRepositorio):
    def __init__(self, keyspace: str = "todo", table: str = "tarefas"):
        self.keyspace = keyspace
        self.table = table
        self.cluster = Cluster(["127.0.0.1"])  # ou IP do Cassandra
        self.session = self.cluster.connect()
        self._criar_schema()

    def _criar_schema(self):
        self.session.execute(f"""
            CREATE KEYSPACE IF NOT EXISTS {self.keyspace}
            WITH replication = {{ 'class': 'SimpleStrategy', 'replication_factor': '1' }}
        """)
        self.session.set_keyspace(self.keyspace)

        self.session.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id TEXT PRIMARY KEY,
                titulo TEXT,
                concluida BOOLEAN
            )
        """)

    def salvar(self, tarefa: Tarefa) -> None:
        self.session.execute(f"""
            INSERT INTO {self.table} (id, titulo, concluida)
            VALUES (%s, %s, %s)
        """, (tarefa.id, tarefa.titulo, tarefa.concluida))

    def listar(self) -> List[Tarefa]:
        rows = self.session.execute(f"SELECT * FROM {self.table}")
        return [Tarefa(id=row.id, titulo=row.titulo, concluida=row.concluida) for row in rows]

    def remover(self, id: str) -> None:
        self.session.execute(f"DELETE FROM {self.table} WHERE id = %s", (id,))

    def atualizar(self, tarefa: Tarefa) -> None:
        self.session.execute(f"""
            UPDATE {self.table}
            SET titulo = %s, concluida = %s
            WHERE id = %s
        """, (tarefa.titulo, tarefa.concluida, tarefa.id))

    def buscar_por_id(self, id: str) -> Tarefa:
        row = self.session.execute(f"SELECT * FROM {self.table} WHERE id = %s", (id,)).one()
        if row:
            return Tarefa(id=row.id, titulo=row.titulo, concluida=row.concluida)
        else:
            raise ValueError(f"Tarefa com id {id} não encontrada.")
        

    def atualizar_titulo(self, id: str, novo_titulo: str) -> None:
        self.session.execute(f"""
            UPDATE {self.table}
            SET titulo = %s
            WHERE id = %s
        """, (novo_titulo, id))
