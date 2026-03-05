"""
Módulo Paciente - Dev 1 Sprint 1
Classe que representa um paciente no totem hospitalar.
"""


class Paciente:
    """Representa um paciente com nome, idade e indicação de PCD."""

    def __init__(self, nome: str, idade: int, pcd: str):
        """
        Inicializa um paciente.

        Args:
            nome: Nome completo do paciente.
            idade: Idade em anos.
            pcd: "S" se for pessoa com deficiência, "N" caso contrário.
        """
        self.nome = nome
        self.idade = idade
        self.pcd = pcd.upper() if pcd else "N"

    def __str__(self) -> str:
        return f"Paciente(nome='{self.nome}', idade={self.idade}, pcd='{self.pcd}')"

    def __repr__(self) -> str:
        return self.__str__()


# Teste rápido: criar um paciente e ver se guarda os dados
if __name__ == "__main__":
    p = Paciente(nome="Maria Silva", idade=65, pcd="N")
    print("Teste Paciente:")
    print(f"  Nome: {p.nome}")
    print(f"  Idade: {p.idade}")
    print(f"  PCD: {p.pcd}")
    print(f"  __str__: {p}")
    assert p.nome == "Maria Silva" and p.idade == 65 and p.pcd == "N"
    print("  OK - dados guardados corretamente.")
