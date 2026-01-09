# Chatbot Orientador Técnico – Ciência de Dados

Este projeto apresenta um **chatbot orientador técnico** voltado à área de Ciência de Dados, Machine Learning e carreira em tecnologia, com foco em **diagnóstico de nível técnico**, **identificação de lacunas conceituais** e **proposição de trilhas de aprendizado realistas**.

Diferente de assistentes genéricos, o chatbot foi projetado para atuar de forma **crítica e estruturada**, priorizando fundamentos técnicos e evitando recomendações superficiais baseadas apenas em ferramentas ou tendências.

---

## Objetivo

Apoiar profissionais que desejam migrar ou evoluir em Ciência de Dados a partir de orientação técnica mais próxima da realidade do mercado, abordando questões como:

- Avaliação do nível técnico real do usuário  
- Identificação de lacunas conceituais relevantes  
- Correção de premissas frágeis ou ilusões de competência  
- Definição de trilhas de aprendizado em curto, médio e longo prazo  
- Priorização de fundamentos (estatística, ML, programação) antes de ferramentas

O chatbot **não substitui mentoria humana** e **não tem caráter motivacional**, sendo utilizado como apoio estruturado à tomada de decisão sobre aprendizado e evolução técnica.

---

## Escopo de Atuação

- Ciência de Dados  
- Machine Learning  
- Estatística Aplicada  
- Programação (principalmente Python)  
- Desenvolvimento de carreira técnica em tecnologia  

---

## Arquitetura e Design

- A lógica de negócio do chatbot é desacoplada do meio de execução  
- O comportamento do modelo é definido explicitamente via prompt versionado  
- A implementação atual utiliza a API do Google Gemini  
- O projeto foi desenhado para facilitar reutilização em diferentes contextos, como:
  - Execução via linha de comando (CLI)
  - APIs REST (FastAPI, Flask)
  - Aplicações web
  - Serviços serverless

---

## Estrutura do Projeto

```text
.
├── chatbot.py        # Orquestração da conversa e interação com o modelo
├── prompts.py        # Definição do comportamento e escopo do orientador
├── requirements.txt  # Dependências do projeto
├── .env              # Variáveis de ambiente (não versionado)
└── README.md
```

## Pré-requisitos
- Python 3.9 ou superior
- Conta no Google AI Studio
- Chave de API do Google Gemini
---

## Variáveis de Ambiente
```bash
GEMINI_API_KEY=SEU_TOKEN_DO_GEMINI_AQUI
```
---

## Execução Local (CLI)
```bash
pip install -r requirements.txt
python chatbot.py
```
---

## Extensões Futuras
- Exposição via API REST
- Interface web
- Persistência de histórico de interação
- Avaliação quantitativa da qualidade das recomendações

Essas extensões não fazem parte deste repositório, pois o foco do projeto é o **desenho do comportamento do orientador**, e não a camada de apresentação.

---

## Licença

Projeto disponibilizado para fins educacionais e experimentais.



