# Orion - Assistente Virtual em Python 🤖
Um assistente de voz pessoal, chamado Orion, construído em Python. Ele utiliza a API Gemini do Google para responder a perguntas complexas e possui comandos locais para tarefas rápidas, com a flexibilidade de interagir tanto por voz quanto por texto.

## ✨ Funcionalidades

-   **Interação Flexível:** Escolha entre comandos de voz (microfone) ou texto (teclado).
-   **Inteligência Artificial:** Integrado com a API Gemini para respostas inteligentes e contextuais.
-   **Comandos Locais:** Responde a perguntas básicas como "que horas são?" e "que dia é hoje?" de forma instantânea.
-   **Interface de Console:** Design limpo e organizado no terminal para uma melhor experiência de uso.
-   **Fácil Expansão:** O código é modularizado, facilitando a adição de novas funcionalidades.

## 📋 Pré-requisitos

Antes de começar, garanta que você tem o seguinte instalado:
-   [Python 3.10+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads)

## 🚀 Instalação e Configuração
Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

**1. Clone o Repositório:**
Abra seu terminal ou Git Bash e execute:
```bash
git clone [https://github.com/seu-usuario/Orion.git](https://github.com/seu-usuario/Orion.git)
cd Orion
```
*(Lembre-se de substituir `seu-usuario` pelo seu nome de usuário do GitHub)*

**2. Crie e Ative um Ambiente Virtual:**
Isso isola as dependências do projeto e é uma prática recomendada.
```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate

# Ative o ambiente (Linux/macOS)
source venv/bin/activate
```

**3. Instale as Dependências:**
O arquivo `requirements.txt` contém todas as bibliotecas que o Orion precisa.
```bash
pip install -r requirements.txt
```

**4. Configure sua Chave de API:**
Você precisará de uma chave de API da Gemini, que pode ser obtida gratuitamente no [Google AI Studio](https://aistudio.google.com/).

```bash
# Renomeie o arquivo de exemplo de configuração.
# No Windows (CMD):
rename config.py.example config.py
# No Linux/macOS ou Windows (PowerShell):
mv config.py.example config.py
```
-   Após renomear, abra o novo arquivo `config.py` e **cole sua chave de API** na variável `GEMINI_API_KEY`.

## ▶️ Como Executar
**Pelo Terminal:**
Certifique-se de que seu ambiente virtual (`venv`) está ativado e execute o seguinte comando na pasta raiz `Orion/`:
```bash
python -m src.main
```
