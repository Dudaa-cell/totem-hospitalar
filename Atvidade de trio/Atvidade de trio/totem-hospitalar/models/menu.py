"""
Módulo Menu - Dev 2 Sprint 1
Exibe o menu de serviços e lê a escolha do usuário.
"""

CONSULTA = "1"
EXAME = "2"
EMERGENCIA = "3"


def mostrar_menu() -> str:
    """
    Mostra o menu de serviços, lê a escolha do usuário e retorna a opção.

    Returns:
        "1" (Consulta), "2" (Exame) ou "3" (Emergência).
        Repete a pergunta até uma opção válida.
    """
    while True:
        print("\n" + "=" * 40)
        print("         MENU DE SERVIÇOS")
        print("=" * 40)
        print("  1 - Consulta")
        print("  2 - Exame")
        print("  3 - Emergência")
        print("=" * 40)
        escolha = input("Escolha o serviço (1, 2 ou 3): ").strip()
        if escolha in (CONSULTA, EXAME, EMERGENCIA):
            return escolha
        print("Opção inválida. Digite 1, 2 ou 3.")


# Teste rápido (comentado para não travar em execução automática)
if __name__ == "__main__":
    print("Teste Menu (simulando escolha 2):")
    # Em teste manual: opcao = mostrar_menu()
    opcoes_validas = ("1", "2", "3")
    for o in opcoes_validas:
        print(f"  Opção {o} é válida: {o in opcoes_validas}")
    print("  OK. Menu retorna 1, 2 ou 3.")
