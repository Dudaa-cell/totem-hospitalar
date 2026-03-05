# Totem Hospitalar

Projeto em trio: totem de autoatendimento para hospitais (cadastro de paciente, menu de serviços, classificação prioritária e geração de senhas).

## Estrutura

```
totem-hospitalar/
├── main.py              # Fluxo principal (Líder)
├── models/
│   ├── __init__.py
│   ├── paciente.py       # Classe Paciente (Dev 1)
│   ├── classificador.py  # PRIORITARIO / GERAL (Dev 1)
│   ├── triagem.py       # Emergência não gera senha (Dev 1)
│   ├── menu.py          # Menu Consulta/Exame/Emergência (Dev 2)
│   ├── gerador_senha.py # Senhas G-001, P-001... (Dev 2)
│   └── impressora.py    # Ticket e alerta emergência (Dev 2)
└── README.md
```

## Como rodar

Na pasta do projeto:

```bash
python main.py
```

Requisito: Python 3.10+ (ou ajustar tipagem em `impressora.py` se for 3.9).

## Regras de negócio

- **Prioritário:** idade ≥ 60 ou PCD = "S". Senha tipo `P-001`, `P-002`...
- **Geral:** demais casos. Senha tipo `G-001`, `G-002`...
- **Emergência:** não gera senha; exibe alerta para ir à recepção.

## Desenvolvimento

Cada módulo pode ser testado sozinho, por exemplo:

```bash
python -m models.paciente
python -m models.classificador
python -m models.gerador_senha
```

---

## Fluxo Git (trio)

### Líder (1 vez)
1. Criar repositório no GitHub: **totem-hospitalar**
2. Adicionar os colegas como colaboradores
3. Clonar com GitHub Desktop
4. Criar pasta `models/`, `models/__init__.py`, `main.py`, `README.md` → Commit "Estrutura inicial" → Push na `main`

### Dev 1 (cada sprint em uma branch)
- **Sprint 1:** `feat-paciente` → `models/paciente.py` → Commit "Cria classe Paciente" → Push → PR → após merge: Fetch/Pull
- **Sprint 2:** `feat-classificador` → `models/classificador.py` → Commit → Push → PR → Fetch/Pull
- **Sprint 3:** `feat-triagem` → `models/triagem.py` → Commit → Push → PR → Fetch/Pull

### Dev 2 (cada sprint em uma branch)
- **Sprint 1:** `feat-menu` → `models/menu.py` → Commit → Push → PR → Fetch/Pull
- **Sprint 2:** `feat-senha` → `models/gerador_senha.py` → Commit → Push → PR → Fetch/Pull
- **Sprint 3:** `feat-impressora` → `models/impressora.py` → Commit → Push → PR → Fetch/Pull

### Líder (integração)
- Após todos os PRs mergeados: abrir `main.py`, importar tudo, montar o fluxo em loop, testar `python main.py`.
