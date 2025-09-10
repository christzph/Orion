
---
🇧🇷
# Orion - Assistente Virtual 🤖

Um assistente de voz pessoal, chamado **Orion**, que evoluiu de uma interface de linha de comando em Python para também contar com uma **interface web interativa**.

Ele utiliza a **API Gemini do Google** para responder a perguntas complexas e possui **comandos locais** para tarefas rápidas, com a flexibilidade de interagir por **voz ou texto**, seja pelo **terminal (CLI)** ou pela **interface gráfica no navegador**.

---

## ✨ Funcionalidades

* **Interação Flexível:** Escolha entre     comandos de voz (microfone) ou texto (teclado).
* **Inteligência Artificial:** Integrado com a API Gemini para respostas inteligentes e contextuais.
* **Comandos Locais:** Responde a perguntas básicas como "que horas são?" e "que dia é hoje?" de forma instantânea.
* **Interface de Console (CLI):** Experiência leve e organizada direto no terminal.
* **Interface Web:** Agora também disponível em HTML, CSS e Javascript, com backend em Node.js.
* **Fácil Expansão:** Código modularizado, permitindo adicionar novas funcionalidades de forma prática.

---

## 📋 Pré-requisitos

Antes de começar, garanta que você tem o seguinte instalado:

* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/en/download/)
* [Git](https://git-scm.com/downloads)

---

## 🚀 Instalação e Configuração

Clone o repositório e entre na pasta principal:

```bash
git clone https://github.com/christzph/Orion.git
cd Orion
```

---

### 🔹 Executando a versão CLI (Python)

Os arquivos da versão em Python estão agora na pasta `cli/`.

**1. Acesse a pasta da versão CLI:**

```bash
cd cli
```

**2. Crie e ative um ambiente virtual:**

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate

# Ative o ambiente (Linux/macOS)
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Configure sua chave da API Gemini:**
Renomeie o arquivo de configuração e adicione sua chave de API.

```bash
# No Windows (CMD):
rename config.py.example config.py

# No Linux/macOS ou Windows (PowerShell):
mv config.py.example config.py
```

Edite o arquivo `config.py` e cole sua chave na variável `GEMINI_API_KEY`.

**5. Execute a versão CLI:**

```bash
python -m src.main
```

---

### 🔹 Executando a versão Web (Node.js + HTML/CSS/JS)

**1. Acesse a pasta backend:**

```bash
cd backend
```

**2. Inicie o servidor do Orion:**

```bash
node server.js
```

**3. Abra a interface Web:**
Localize e abra o arquivo `index.html` no seu navegador.

---

## ▶️ Resumo dos Modos de Execução

* **Terminal (CLI - Python):**

  ```bash
  cd cli
  python -m src.main
  ```
* **Interface Web (Node.js + HTML/CSS/JS):**

  ```bash
  cd backend
  node server.js
  ```

  Em seguida, abra `index.html` no navegador.

---

🇺🇸

---

# Orion - Virtual Assistant 🤖

**Orion** is a personal voice assistant that has evolved from a **command-line interface (CLI) in Python** to now also featuring a **modern web interface**.

It leverages the **Google Gemini API** to answer complex questions and supports **local commands** for quick tasks, with the flexibility of interacting through **voice or text** — either via the **terminal (CLI)** or a **browser-based interface**.

---

## ✨ Features

* **Flexible Interaction:** Choose between voice commands (microphone) or text (keyboard).
* **Artificial Intelligence:** Powered by Google Gemini API for smart, contextual answers.
* **Local Commands:** Instantly responds to quick queries like "what time is it?" or "what day is it today?".
* **Console Interface (CLI):** Lightweight, organized experience directly in the terminal.
* **Web Interface:** Built with HTML, CSS, and JavaScript, powered by a Node.js backend.
* **Easy Expansion:** Modular codebase, designed for scalability and new features.

---

## 📋 Requirements

Make sure you have the following installed before running Orion:

* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/en/download/)
* [Git](https://git-scm.com/downloads)

---

## 🚀 Installation & Setup

Clone the repository and enter the main folder:

```bash
git clone https://github.com/christzph/Orion.git
cd Orion
```

---

### 🔹 Running the CLI Version (Python)

The Python CLI version is now located inside the `cli/` folder.

**1. Navigate to the CLI folder:**

```bash
cd cli
```

**2. Create and activate a virtual environment:**

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on Linux/macOS
source venv/bin/activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Configure your Gemini API Key:**
Rename the config file and insert your API key.

```bash
# On Windows (CMD):
rename config.py.example config.py

# On Linux/macOS or Windows (PowerShell):
mv config.py.example config.py
```

Edit `config.py` and paste your key into the variable `GEMINI_API_KEY`.

**5. Run the CLI version:**

```bash
python -m src.main
```

---

### 🔹 Running the Web Version (Node.js + HTML/CSS/JS)

**1. Navigate to the backend folder:**

```bash
cd backend
```

**2. Start the Orion server:**

```bash
node server.js
```

**3. Open the Web Interface:**
Locate and open `index.html` in your browser.

---

## ▶️ Execution Summary

* **Terminal (CLI - Python):**

  ```bash
  cd cli
  python -m src.main
  ```
* **Web Interface (Node.js + HTML/CSS/JS):**

  ```bash
  cd backend
  node server.js
  ```

  Then open `index.html` in your browser.

---