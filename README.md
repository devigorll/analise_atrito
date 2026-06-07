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

- [x] **Organização e Engenharia de Dados:** Estruturação do pipeline de dados e importação de variáveis demográficas e de performance.
- [x] **Análise Exploratória de Dados (EDA):** Identificação de distribuições de frequência, correlações e padrões iniciais de demissão.
- [ ] **Análise de Sobrevivência:** Modelagem estatística baseada em tempo de casa do colaborador para estimar a curva de retenção.
- [ ] **Automação da Matriz 9-Box:** Cruzamento de dados de avaliação para categorizar os colaboradores dinamicamente.
- [ ] **Geração de Insights de Negócio:** Cruzamento do risco de atrito com o potencial do funcionário para sugerir planos de retenção.

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
├── data/               # Bases de dados (anonimizadas)
├── notebooks/          # Jupyter Notebooks ordenados por etapas de análise
│   ├── 01_eda_limpeza.ipynb
│   ├── 02_analise_sobrevivencia.ipynb
│   └── 03_matriz_9box.ipynb
├── src/                # Scripts auxiliares para automação (.py)
├── .gitignore          # Proteção para não subir arquivos pesados ou confidenciais
└── README.md           # Documentação principal
