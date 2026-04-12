📋 Organizador de Tarefas CLI
📌 Problema

Muitos estudantes e usuários têm dificuldade em organizar tarefas do dia a dia, o que pode levar à perda de prazos, baixa produtividade e falta de acompanhamento das atividades.

💡 Solução

Esta aplicação em linha de comando (CLI) permite gerenciar tarefas de forma simples, possibilitando cadastrar, listar, concluir e remover tarefas, ajudando na organização pessoal e acadêmica.

👥 Público-alvo
Estudantes
Pessoas com dificuldade de organização
Usuários que preferem ferramentas simples no terminal
Quem precisa de um gerenciador de tarefas leve

⚙️ Funcionalidades:

➕ Adicionar tarefa
📋 Listar tarefas
✅ Marcar tarefa como concluída
❌ Remover tarefa
💾 Persistência em arquivo JSON
🧪 Testes automatizados
🧹 Lint com Ruff
🔁 CI com GitHub Actions

🛠️ Tecnologias utilizadas
    Python 3
    Pytest
    Ruff
    GitHub Actions
    JSON para armazenamento

📁 Estrutura do Projeto
    Organizador-de-Tarefas/
    │
    ├── src/
    │   ├── main.py
    │   └── task_manager.py
    │
    ├── tests/
    │   └── test_tasks.py
    │
    ├── data/
    │   └── tasks.json
    │
    ├── .github/workflows/
    │   └── ci.yml
    │
    ├── requirements.txt
    ├── README.md
    ├── VERSION
    └── .gitignore

▶️ Como executar o projeto
1. Clonar o repositório
git clone https://github.com/JPACouto/Organizador-de-Tarefas.git
cd Organizador-de-Tarefas
2. Instalar dependências
pip install -r requirements.txt
3. Executar aplicação
python src/main.py
🧪 Rodar testes automatizados
pytest

Resultado esperado:

3 passed

🧹 Rodar lint (análise estática)
ruff check .

🔁 Integração Contínua (CI)

O projeto utiliza GitHub Actions para:

Instalar dependências automaticamente
Executar lint
Executar testes automatizados
Validar o código em cada push

Workflow localizado em:

.github/workflows/ci.yml

📸 Evidência de Funcionamento
    🧪 Testes automatizados

    ![Teste 1](./images/imagem%20teste.png)

    ![Teste 2](./images/imagem%20teste2.png)

📦 Versionamento

Este projeto utiliza versionamento semântico:

MAJOR.MINOR.PATCH

Versão atual:

1.0.0

Arquivo:

VERSION
📦 Dependências

Arquivo:

requirements.txt

Conteúdo:

pytest
ruff
👤 Autor

João Pedro Araujo Couto

🔗 Repositório

https://github.com/JPACouto/Organizador-de-Tarefas

📄 Licença

Uso educacional — BootCamp Entrega Inicial

[def]: ./images/tests.png