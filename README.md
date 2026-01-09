# 🤖 Chatbot Orientador Técnico – Ciência de Dados

Chatbot orientador técnico especializado em **Ciência de Dados**, **Machine Learning** e **carreira em tecnologia**, utilizando a API do **Google Gemini**.

O projeto foi desenvolvido com foco em **modularidade e reutilização**, permitindo que a lógica central do chatbot seja facilmente integrada em diferentes contextos, como:

- Execução via CLI
- APIs (FastAPI, Flask, etc.)
- Aplicações web
- Serviços serverless

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python chatbot.py
```
---

# 📌 Objetivo

Fornecer **orientação técnica estruturada, realista e fundamentada** para profissionais que desejam:
- Migrar para Ciência de Dados
- Evoluir tecnicamente na área
- Identificar lacunas de conhecimento
- Construir trilhas de aprendizado sólidas

O chatbot foi projetado para:
- Adaptar a linguagem ao nível técnico do usuário
- Priorizar fundamentos técnicos sólidos
- Questionar premissas frágeis ou superficiais
- Evitar respostas genéricas ou motivacionais
---

# 📂 Estrutura do Projeto
```bash
.
├── chatbot.py              # Lógica principal do chatbot
├── prompts.py              # System prompt e instruções do modelo
├── requirements.txt        # Dependências do projeto
├── .env                    # Variáveis de ambiente (API Key)
└── README.md
```
---

# ⚙️ Pré-requisitos
- Python 3.9 ou superior
- Conta no Google AI Studio
- Chave de API do Google Gemini
---

# 🔐 Variáveis de Ambiente
- Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
```bash
GEMINI_API_KEY=SEU_TOKEN_DO_GEMINI_AQUI
```
---

# 📦 Instalação
```bash
pip install -r requirements.txt
```
---

# ▶️ Execução Local (CLI)
```bash
python chatbot.py
```
---

# 🧠 Arquitetura e Design
- A lógica do chatbot é **independente do meio de execução**
- O comportamento do modelo é definido em prompts.py, facilitando ajustes, versionamento e experimentação
- O projeto pode ser facilmente adaptado para:
    - APIs REST
    - Interfaces web
    - Aplicações serverless
---

# 🔌 Integração com APIs (Visão Geral)
A lógica presente em **chatbot.py** pode ser reutilizada diretamente em frameworks como FastAPI ou Flask, expondo o chatbot como um endpoint HTTP.
- Esta implementação não está incluída neste repositório e deve ser realizada conforme o contexto da aplicação consumidora.
---

# 📄 Licença

Este projeto é disponibilizado para fins educacionais e de estudo.
Adapte conforme suas necessidades.


