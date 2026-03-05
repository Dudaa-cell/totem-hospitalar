"""
Totem Hospitalar - Arquivo principal (Integração pelo Líder)
Fluxo: cadastrar paciente → menu → classificar → gerar senha (ou alerta emergência) → imprimir ticket.
"""

from models.paciente import Paciente
from models.classificador import classificar
from models.triagem import eh_emergencia, nome_servico
from models.menu import mostrar_menu
from models.gerador_senha import gerar_senha
from models.impressora import imprimir_ticket, imprimir_alerta_emergencia


def cadastrar_paciente() -> Paciente:
    """Lê nome, idade e PCD do usuário e retorna um Paciente."""
    print("\n--- Cadastro do Paciente ---")
    nome = input("Nome: ").strip() or "Não informado"
    while True:
        try:
            idade = int(input("Idade: ").strip())
            if idade < 0 or idade > 150:
                print("Idade deve ser entre 0 e 150.")
                continue
            break
        except ValueError:
            print("Digite um número válido para a idade.")
    pcd = input("PCD (S/N): ").strip().upper() or "N"
    if pcd not in ("S", "N"):
        pcd = "N"
    return Paciente(nome=nome, idade=idade, pcd=pcd)


def main() -> None:
    print("=" * 42)
    print("    BEM-VINDO AO TOTEM HOSPITALAR")
    print("=" * 42)

    while True:
        # 1) Cadastrar paciente
        paciente = cadastrar_paciente()

        # 2) Mostrar menu e ler escolha
        opcao = mostrar_menu()
        servico_nome = nome_servico(opcao)

        # 3) Se Emergência: alerta e não gera senha
        if eh_emergencia(opcao):
            imprimir_alerta_emergencia()
            print("Atendimento de emergência registrado. Sem senha.")
        else:
            # 4) Classificar (GERAL ou PRIORITARIO)
            classificacao = classificar(paciente)
            # 5) Gerar senha (G-xxx ou P-xxx)
            senha = gerar_senha(classificacao)
            # 6) Imprimir ticket
            imprimir_ticket(
                nome=paciente.nome,
                servico=servico_nome,
                senha=senha,
            )

        # Continuar ou sair
        saida = input("Atender outro paciente? (S/N): ").strip().upper() or "S"
        if saida == "N":
            print("\nTotem encerrado. Até logo!")
            break


if __name__ == "__main__":
    main()
