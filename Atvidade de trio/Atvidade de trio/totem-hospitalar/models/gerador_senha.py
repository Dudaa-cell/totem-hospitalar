"""
Módulo Gerador de Senha - Dev 2 Sprint 2
Gera senhas sequenciais para fila Geral e Prioritário.
"""

# Contadores globais por tipo (G-001, G-002... e P-001, P-002...)
_contador_geral = 0
_contador_prioritario = 0


def gerar_senha(tipo: str) -> str:
    """
    Gera a próxima senha do tipo informado.

    Args:
        tipo: "GERAL" ou "PRIORITARIO".

    Returns:
        Senha no formato "G-001", "G-002", ... ou "P-001", "P-002", ...
    """
    global _contador_geral, _contador_prioritario
    if tipo == "PRIORITARIO":
        _contador_prioritario += 1
        return f"P-{_contador_prioritario:03d}"
    # GERAL (ou qualquer outro)
    _contador_geral += 1
    return f"G-{_contador_geral:03d}"


def resetar_contadores() -> None:
    """Zera os contadores (útil para testes)."""
    global _contador_geral, _contador_prioritario
    _contador_geral = 0
    _contador_prioritario = 0


# Teste rápido
if __name__ == "__main__":
    resetar_contadores()
    print("Teste Gerador de Senha:")
    print(f"  Geral 1: {gerar_senha('GERAL')}")
    print(f"  Geral 2: {gerar_senha('GERAL')}")
    print(f"  Prioritário 1: {gerar_senha('PRIORITARIO')}")
    print(f"  Geral 3: {gerar_senha('GERAL')}")
    assert gerar_senha("GERAL") == "G-004"
    assert gerar_senha("PRIORITARIO") == "P-002"
    print("  OK.")
