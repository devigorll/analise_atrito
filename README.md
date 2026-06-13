# 📊 People Analytics: Análise de Atrito e Planejamento de Sucessão

![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)
![Linguagem](https://img.shields.io/badge/Language-Python-blue)
![Área](https://img.shields.io/badge/Area-People%20Analytics-purple)

Este projeto aplica técnicas avançadas de Ciência de Dados e Estatística para antecipar a evasão de talentos (*turnover/atrito*) e otimizar o planejamento de sucessão nas empresas. A abordagem combina a modelagem preditiva de sobrevivência com a automação da clássica **Matriz 9-Box** para identificar profissionais de alto potencial em risco de saída.

---

## 📌 Índice

- [Contexto do Negócio](#-contexto-do-negócio)
- [Funcionalidades e Etapas Tecnológicas](#-funcionalidades-e-etapas-tecnológicas)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Estrutura de Storytelling e Resultados](#-estrutura-de-storytelling-e-resultados)
- [Autores](#-autores)

---

## 💼 Contexto do Negócio

A perda de talentos-chave gera custos altíssimos de recrutamento, perda de histórico institucional e queda na produtividade das equipes. Este projeto responde a três perguntas críticas para a gestão de Recursos Humanos:
1. **Quem** tem maior probabilidade de deixar a empresa a curto/médio prazo?
2. **Quando** essa evasão tem maior probabilidade de acontecer (*Análise de Sobrevivência*)?
3. **Como** proteger nossos futuros líderes através de uma alocação inteligente na *Matriz 9-Box* (Desempenho vs. Potencial)?

---

## ⚙️ Funcionalidades e Etapas Tecnológicas

O projeto é executado seguindo um roteiro técnico rigoroso dividido em etapas práticas:

## ⚙️ Funcionalidades e Etapas Tecnológicas

Como parte da minha formação e desenvolvimento em Ciência de Dados, o projeto foi estruturado de forma prática e incremental através dos seguintes notebooks:

- [x] **01. Tratamento de Dados (Organização e Engenharia):** Higienização da base original da IBM, tradução de features e estruturação do pipeline inicial de importação de variáveis demográficas e de performance.
- [x] **02. Análise Exploratória (EDA):** Investigação detalhada de distribuições de frequência, correlações e identificação de padrões iniciais envolvidos na demissão de colaboradores.
- [x] **03. Diagnóstico Estatístico Visual (Automação da Matriz 9-Box):** Cruzamento de dados de avaliação e performance para categorizar os funcionários dinamicamente, gerando os primeiros insights visuais e testes estatísticos.
- [x] **04. Análise de Sobrevivência e Insights de Negócio:** Aplicação de modelagem estatística baseada no tempo de casa para estimar a curva de retenção. Cruzamento do risco de atrito com o potencial do funcionário (9-Box) para sugerir planos estratégicos de retenção de talentos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas & NumPy** (Manipulação e engenharia de atributos)
- **Matplotlib & Seaborn** (Visualizações gráficas de alta qualidade)
- **Lifelines** (Biblioteca Python especializada em Análise de Sobrevivência)
- **Scikit-Learn** (Modelagem estatística e algoritmos preditivos)

---

## 📁 Estrutura do Repositório

```text
ANALISE_ATRITO/
├── data/
│   ├── tabela_base_traduzida.csv                 # Base de dados tratada e traduzida
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv     # Base de dados original (IBM HR Data)
├── notebooks/
│   ├── 01_tratamento_dados.ipynb                 # Limpeza e preparação dos dados
│   ├── 02_analise_exploratoria.ipynb             # Análise exploratória descritiva (EDA)
│   ├── 03_diagnostico_estatistico_visual.ipynb   # Visualizações e testes de hipóteses
│   └── 04_analise_sobrevivencia.ipynb            # Curvas de Kaplan-Meier e riscos proporcionais
├── src/
│   └── main.py                                   # Script principal para automação do pipeline
├── venv/                                         # Ambiente virtual (ignorado no Git)
├── .gitignore                                    # Restrições de upload (arquivos locais e venv)
├── README.md                                     # Documentação principal do projeto
└── requirements.txt                              # Dependências e bibliotecas do projeto