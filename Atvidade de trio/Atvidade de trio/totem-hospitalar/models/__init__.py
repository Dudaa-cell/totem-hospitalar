"""
Pacote models - Totem Hospitalar
Exporta classes e funções dos módulos do sistema.
"""

from models.paciente import Paciente
from models.classificador import classificar
from models.triagem import eh_emergencia, nome_servico, SERVICO_CONSULTA, SERVICO_EXAME, SERVICO_EMERGENCIA
from models.menu import mostrar_menu
from models.gerador_senha import gerar_senha, resetar_contadores
from models.impressora import imprimir_ticket, imprimir_alerta_emergencia

__all__ = [
    "Paciente",
    "classificar",
    "eh_emergencia",
    "nome_servico",
    "SERVICO_CONSULTA",
    "SERVICO_EXAME",
    "SERVICO_EMERGENCIA",
    "mostrar_menu",
    "gerar_senha",
    "resetar_contadores",
    "imprimir_ticket",
    "imprimir_alerta_emergencia",
]
