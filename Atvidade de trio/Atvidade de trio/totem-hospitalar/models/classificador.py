"""
Módulo Classificador - Dev 1 Sprint 2
Classifica o paciente como PRIORITARIO ou GERAL.
"""

from models.paciente import Paciente


def classificar(paciente: Paciente) -> str:
    """
    Recebe um Paciente e retorna a classificação de atendimento.

    Regra:
        - PRIORITARIO: idade >= 60 OU pcd == "S"
        - GERAL: caso contrário

    Args:
        paciente: Instância de Paciente.

    Returns:
        "PRIORITARIO" ou "GERAL".
    """
    if paciente.idade >= 60 or paciente.pcd == "S":
        return "PRIORITARIO"
    return "GERAL"


# Teste rápido
if __name__ == "__main__":
    from models.paciente import Paciente

    p1 = Paciente("João", 25, "N")
    p2 = Paciente("Maria", 65, "N")
    p3 = Paciente("Pedro", 30, "S")
    print("Teste Classificador:")
    print(f"  João (25, N): {classificar(p1)}")   # GERAL
    print(f"  Maria (65, N): {classificar(p2)}")  # PRIORITARIO
    print(f"  Pedro (30, S): {classificar(p3)}")  # PRIORITARIO
    assert classificar(p1) == "GERAL"
    assert classificar(p2) == "PRIORITARIO"
    assert classificar(p3) == "PRIORITARIO"
    print("  OK.")
