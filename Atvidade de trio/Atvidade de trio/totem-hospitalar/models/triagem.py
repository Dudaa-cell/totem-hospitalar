"""
Módulo Triagem - Dev 1 Sprint 3
Verifica se o serviço escolhido é Emergência (não gera senha).
"""

# Códigos/opções de serviço (alinhado ao menu)
SERVICO_CONSULTA = "1"
SERVICO_EXAME = "2"
SERVICO_EMERGENCIA = "3"


def eh_emergencia(opcao: str) -> bool:
    """
    Verifica se a opção escolhida é Emergência.

    Args:
        opcao: Opção retornada pelo menu ("1", "2" ou "3").

    Returns:
        True se for Emergência, False caso contrário.
    """
    return opcao == SERVICO_EMERGENCIA


def nome_servico(opcao: str) -> str:
    """Retorna o nome legível do serviço para exibição no ticket."""
    if opcao == SERVICO_CONSULTA:
        return "Consulta"
    if opcao == SERVICO_EXAME:
        return "Exame"
    if opcao == SERVICO_EMERGENCIA:
        return "Emergência"
    return "Desconhecido"


# Teste rápido
if __name__ == "__main__":
    print("Teste Triagem:")
    print(f"  Opção 1 (Consulta): eh_emergencia = {eh_emergencia('1')}")
    print(f"  Opção 3 (Emergência): eh_emergencia = {eh_emergencia('3')}")
    assert eh_emergencia("1") is False
    assert eh_emergencia("3") is True
    print("  OK. Emergência não gera senha.")
