"""
Módulo Impressora - Dev 2 Sprint 3
Imprime ticket no console e alerta de emergência.
"""

from datetime import datetime
from typing import Optional


def imprimir_ticket(
    nome: str,
    servico: str,
    senha: str,
    data_hora: Optional[datetime] = None,
) -> None:
    """
    Imprime um ticket bonito no console com data e serviço.

    Args:
        nome: Nome do paciente.
        servico: Nome do serviço (ex: "Consulta", "Exame").
        senha: Senha gerada (ex: "G-001", "P-001").
        data_hora: Data/hora do atendimento; se None, usa agora.
    """
    if data_hora is None:
        data_hora = datetime.now()
    data_str = data_hora.strftime("%d/%m/%Y")
    hora_str = data_hora.strftime("%H:%M")

    print()
    print("╔" + "═" * 38 + "╗")
    print("║" + " TICKET DE ATENDIMENTO ".center(38) + "║")
    print("╠" + "═" * 38 + "╣")
    print("║" + f" Paciente: {nome[:26]:<26} " + "║")
    print("║" + f" Serviço:  {servico[:26]:<26} " + "║")
    print("║" + f" Senha:    {senha:<26} " + "║")
    print("║" + f" Data:     {data_str:<26} " + "║")
    print("║" + f" Hora:     {hora_str:<26} " + "║")
    print("╚" + "═" * 38 + "╝")
    print()


def imprimir_alerta_emergencia() -> None:
    """Imprime alerta de emergência no console (quando serviço é Emergência)."""
    print()
    print("!" * 42)
    print("!!  ATENÇÃO: EMERGÊNCIA - SEM GERAÇÃO DE SENHA  !!")
    print("!!  Dirija-se imediatamente à recepção.        !!")
    print("!" * 42)
    print()


# Teste rápido
if __name__ == "__main__":
    print("Teste Impressora - Ticket:")
    imprimir_ticket("Maria Silva", "Consulta", "G-001")
    print("Teste Impressora - Alerta Emergência:")
    imprimir_alerta_emergencia()
    print("  OK.")
