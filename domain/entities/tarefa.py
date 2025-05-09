""" 
1. Entidades (Entities) - camada mais interna define as entidades do domínio
Não tem dependências externas, fornecem as regras de negócio e são as classes mais puras do sistema.
    - São classes que representam os objetos do domínio, com seus atributos e comportamentos.
    - Não devem depender de frameworks ou bibliotecas externas.
    - Devem ser imutáveis (ou seja, não devem ter métodos que alterem seu estado).
    - Devem ter um construtor que receba todos os atributos obrigatórios.
    - Devem ter métodos que implementem as regras de negócio do domínio.
    - Devem ter métodos que implementem a lógica de comparação entre objetos (por exemplo, __eq__ e __hash__).
"""
from datetime import datetime
from uuid import uuid4


class Tarefa:
    def __init__(self, titulo: str, concluida: bool = False, criada_em: datetime = None, id: str = None):
        self.id = id or str(uuid4())  # gera um id único
        self.titulo = titulo
        self.concluida = concluida

    def alternar_status_conclusao(self):
        self.concluida = not self.concluida

    def atualizar_titulo(self, novo_titulo: str):
        if not novo_titulo.strip():
            raise ValueError("O título da tarefa não pode estar vazio.")
        self.titulo = novo_titulo
